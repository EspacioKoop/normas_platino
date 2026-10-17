"""Pruebas para platino.snapshot; sin red, gh ni credenciales."""
import copy
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import platino as p


def base_config():
    return {
        "schema_version": 1,
        "repository": "equipo/demo",
        "milestones": [
            {"title": "v1.0.0", "description": "Primera entrega.", "issues": [10, 20]}
        ]
    }


def sample_repo(full_name="equipo/demo", archived=False):
    return {"full_name": full_name, "archived": archived}


def sample_milestone(number=1, title="v1.0.0", state="open", description="Primera entrega.", due_on=None):
    return {
        "number": number,
        "title": title,
        "state": state,
        "description": description,
        "due_on": due_on
    }


def sample_issue(number=10, state="open", milestone_number=1, is_pr=False):
    item = {
        "number": number,
        "state": state,
        "milestone": {"number": milestone_number} if milestone_number is not None else None
    }
    if is_pr:
        item["pull_request"] = {}
    return item


class FakeGitHub(p.GitHub):
    """Fake GitHub API en memoria para probar snapshot sin red."""

    def __init__(self, repository=None, milestones=None, issues=None):
        super().__init__("equipo/demo")
        self.repository = copy.deepcopy(repository) if repository is not None else sample_repo()
        self.milestones = copy.deepcopy(list(milestones)) if milestones is not None else [sample_milestone()]
        self.issues = copy.deepcopy(dict(issues)) if issues is not None else {
            10: sample_issue(10, "open", 1),
            20: sample_issue(20, "closed", None)
        }
        self.calls = []

    def request(self, method, suffix="", payload=None):
        self.calls.append((method, suffix, copy.deepcopy(payload)))
        if method != "GET":
            raise p.Error("Snapshot solo debe realizar peticiones GET.")
        if not suffix:
            return copy.deepcopy(self.repository)
        if suffix.startswith("/milestones?"):
            page = int(suffix.rsplit("=", 1)[1])
            return copy.deepcopy(self.milestones[(page - 1) * 100:page * 100])
        if suffix.startswith("/issues/"):
            number = int(suffix.rsplit("/", 1)[1])
            if number in self.issues:
                return copy.deepcopy(self.issues[number])
            raise p.Error(f"Issue {number} no encontrado en fake.")
        raise p.Error(f"Endpoint no soportado en fake: {suffix}")


class SnapshotTests(unittest.TestCase):
    def test_snapshot_success(self):
        fake = FakeGitHub()
        config = base_config()
        result = p.snapshot(fake, config)

        self.assertIn("milestones", result)
        self.assertIn("issues", result)

        self.assertEqual(len(result["milestones"]), 1)
        self.assertEqual(result["milestones"][0], {
            "number": 1,
            "title": "v1.0.0",
            "description": "Primera entrega.",
            "due_on": None,
            "state": "open"
        })

        self.assertEqual(result["issues"], {
            "10": {"state": "open", "milestone": 1},
            "20": {"state": "closed", "milestone": None}
        })

    def test_snapshot_no_network_requests(self):
        fake = FakeGitHub()
        config = base_config()
        with patch.object(subprocess, "run", side_effect=AssertionError("Acceso a red no permitido")):
            result = p.snapshot(fake, config)
        self.assertIsInstance(result, dict)
        self.assertTrue(all(call[0] == "GET" for call in fake.calls))

    def test_snapshot_pagination(self):
        milestones = [sample_milestone(number=n + 1, title=f"v{n + 1}.0.0") for n in range(101)]
        fake = FakeGitHub(milestones=milestones)
        config = base_config()

        result = p.snapshot(fake, config)
        self.assertEqual(len(result["milestones"]), 101)

        page_calls = [suffix for method, suffix, _ in fake.calls if suffix.startswith("/milestones?")]
        self.assertEqual(len(page_calls), 2)
        self.assertIn("page=1", page_calls[0])
        self.assertIn("page=2", page_calls[1])

    def test_snapshot_repository_validation_failures(self):
        config = base_config()

        # Repositorio con nombre distinto
        fake = FakeGitHub(repository=sample_repo(full_name="otro/repo"))
        with self.assertRaisesRegex(p.Error, "El repositorio remoto no coincide"):
            p.snapshot(fake, config)

        # Repositorio archivado
        fake = FakeGitHub(repository=sample_repo(archived=True))
        with self.assertRaisesRegex(p.Error, "archivado"):
            p.snapshot(fake, config)

        # Respuesta de repositorio inválida
        fake = FakeGitHub(repository="no-es-dict")
        with self.assertRaises(p.Error):
            p.snapshot(fake, config)

    def test_snapshot_milestones_validation_failures(self):
        config = base_config()

        # Milestone listado no es una lista
        fake = FakeGitHub()
        fake.request = lambda method, suffix="", payload=None: (
            sample_repo() if not suffix else "no-es-lista"
        )
        with self.assertRaisesRegex(p.Error, "Listado de milestones incompleto o inválido"):
            p.snapshot(fake, config)

        # Milestone con título con espacios extras (inválido por función text)
        fake = FakeGitHub(milestones=[sample_milestone(title=" v1.0.0 ")])
        with self.assertRaisesRegex(p.Error, "Milestone incompleto o paginación repetida"):
            p.snapshot(fake, config)

        # Milestone con estado no válido
        fake = FakeGitHub(milestones=[sample_milestone(state="invalid")])
        with self.assertRaisesRegex(p.Error, "Milestone incompleto o paginación repetida"):
            p.snapshot(fake, config)

        # Milestone sin campo due_on
        bad_ms = sample_milestone()
        del bad_ms["due_on"]
        fake = FakeGitHub(milestones=[bad_ms])
        with self.assertRaisesRegex(p.Error, "Milestone incompleto o paginación repetida"):
            p.snapshot(fake, config)

        # Número de milestone duplicado
        fake = FakeGitHub(milestones=[sample_milestone(number=1), sample_milestone(number=1, title="v2")])
        with self.assertRaisesRegex(p.Error, "Milestone incompleto o paginación repetida"):
            p.snapshot(fake, config)

    def test_snapshot_excessive_pagination_failure(self):
        config = base_config()
        fake = FakeGitHub()

        def request_page(method, suffix="", payload=None):
            if not suffix:
                return sample_repo()
            if suffix.startswith("/milestones?"):
                page = int(suffix.rsplit("=", 1)[1])
                start_num = (page - 1) * 100 + 1
                return [sample_milestone(number=start_num + i, title=f"m{start_num + i}") for i in range(100)]
            raise p.Error("Endpoint no esperado")

        fake.request = request_page
        with self.assertRaisesRegex(p.Error, "Paginación excesiva"):
            p.snapshot(fake, config)

    def test_snapshot_issue_validation_failures(self):
        config = base_config()

        # Issue no coincide en número
        fake = FakeGitHub(issues={10: sample_issue(number=99), 20: sample_issue(number=20)})
        with self.assertRaisesRegex(p.Error, "Referencia inexistente"):
            p.snapshot(fake, config)

        # Issue es una Pull Request
        fake = FakeGitHub(issues={10: sample_issue(number=10, is_pr=True), 20: sample_issue(number=20)})
        with self.assertRaisesRegex(p.Error, "perteneciente a un PR"):
            p.snapshot(fake, config)

        # Issue estado no válido
        fake = FakeGitHub(issues={10: sample_issue(number=10, state="invalid"), 20: sample_issue(number=20)})
        with self.assertRaisesRegex(p.Error, "Estado de issue incompleto"):
            p.snapshot(fake, config)

        # Issue sin clave milestone
        issue_no_ms = sample_issue(number=10)
        del issue_no_ms["milestone"]
        fake = FakeGitHub(issues={10: issue_no_ms, 20: sample_issue(number=20)})
        with self.assertRaisesRegex(p.Error, "Estado de issue incompleto"):
            p.snapshot(fake, config)

        # Issue milestone con estructura no válida
        bad_issue_ms = sample_issue(number=10)
        bad_issue_ms["milestone"] = "no-es-dict"
        fake = FakeGitHub(issues={10: bad_issue_ms, 20: sample_issue(number=20)})
        with self.assertRaisesRegex(p.Error, "Milestone del issue no válido"):
            p.snapshot(fake, config)


if __name__ == "__main__":
    unittest.main()
