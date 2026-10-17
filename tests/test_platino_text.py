"""Pruebas unitarias para la función text() del módulo platino."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import platino as p


class TextFunctionTests(unittest.TestCase):
    def test_exact_limit(self):
        """Verifica que un texto con longitud exactamente igual al límite es válido."""
        self.assertTrue(p.text("a" * 10, 10))

    def test_above_limit(self):
        """Verifica que un texto que excede el límite no es válido."""
        self.assertFalse(p.text("a" * 11, 10))

    def test_below_limit(self):
        """Verifica que un texto con longitud inferior al límite es válido."""
        self.assertTrue(p.text("a" * 9, 10))

    def test_none_value(self):
        """Verifica que pasar None devuelve False."""
        self.assertFalse(p.text(None, 10))

    def test_non_text_types(self):
        """Verifica que tipos de datos distintos de str devuelven False."""
        for val in (123, 12.3, True, False, ["texto"], {"clave": "valor"}, b"bytes"):
            with self.subTest(val=val):
                self.assertFalse(p.text(val, 10))

    def test_multiline_false(self):
        """Verifica el comportamiento de multiline=False con y sin saltos de línea."""
        self.assertTrue(p.text("Hola mundo", 20, multiline=False))
        self.assertFalse(p.text("Hola\nmundo", 20, multiline=False))

    def test_multiline_true(self):
        """Verifica el comportamiento de multiline=True con y sin saltos de línea."""
        self.assertTrue(p.text("Hola mundo", 20, multiline=True))
        self.assertTrue(p.text("Hola\nmundo", 20, multiline=True))

    def test_empty_and_whitespace_strings(self):
        """Verifica que cadenas vacías o compuestas solo por espacios son rechazadas."""
        self.assertFalse(p.text("", 10))
        self.assertFalse(p.text("   ", 10))

    def test_untrimmed_strings(self):
        """Verifica que cadenas con espacios o saltos de línea al inicio o final son rechazadas."""
        self.assertFalse(p.text(" hola", 10))
        self.assertFalse(p.text("hola ", 10))
        self.assertFalse(p.text("\nhola", 10, multiline=True))
        self.assertFalse(p.text("hola\n", 10, multiline=True))

    def test_control_characters_and_del(self):
        """Verifica que caracteres de control y DEL (\x7f) no son permitidos."""
        self.assertFalse(p.text("hola\x00mundo", 20))
        self.assertFalse(p.text("hola\x1fmundo", 20))
        self.assertFalse(p.text("hola\x7fmundo", 20))
        self.assertFalse(p.text("hola\ttab", 20, multiline=True))


if __name__ == "__main__":
    unittest.main()
