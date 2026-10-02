# Auto-merge con puerta de calidad

Origen: Varo, 02-10-2026: «Nueva norma platino de auto merge como tenemos nosotros, tanto en este repo como en normas platino». Recoge la práctica de las misiones de los obreros de Varo: puerta de calidad → PR → comprobaciones en casa → fusión.

## Adopción (por proyecto)
Un proyecto la activa en su ficha de adopción, con una fila **«Auto-merge: adoptado»** que diga la fecha, quién lo autoriza (una persona con autoridad de merge) y la cita o el enlace. Sin esa fila, sigue rigiendo el punto 8 de AGENTS.md: integrar solo con autorización explícita.

## Condiciones (todas)
Con el auto-merge adoptado, una PR se integra sin una autorización humana por PR cuando cumple **todo** esto:

1. **Reserva y entrega:** `CLAIM` vigente del autor y `PR_READY` en el registro, con el SHA candidato.
2. **Puerta de calidad sobre ese SHA exacto.** Los controles canónicos del proyecto (pruebas, compilación, linters) se ejecutan sobre el SHA candidato, en local o en la CI de casa, y la salida resumida se pega en la PR: comando, máquina y resultado. No vale un verde anterior ni un SHA distinto.
3. **Revisión independiente.** Otro agente o persona, distinto del autor, lee el diff completo y deja `CONFORME sha=<SHA>` en la PR. Cualquier objeción abierta bloquea el merge.
4. **Rama al día con `main` y sin conflictos.** Fusión sin force-push y con el método del proyecto (merge commit o rebase-merge).
5. **Sin veto:** no lleva la etiqueta `requiere-humano` ni tiene un comentario `NO_MERGE` de una persona.

## Fuera del auto-merge (siempre con OK humano expreso)
- Cambios en las normas: `AGENTS.md`, la ficha de adopción y estas guías.
- Licencias, secretos, credenciales, permisos y configuración de acceso.
- Publicación: releases, despliegues, canales y cualquier cosa visible fuera del repo.
- Borrado de datos o de historia, y migraciones irreversibles.
- Dependencias nuevas con licencia dudosa o incompatible.

## Registro y reversión
- Tras fusionar se escribe en el registro `AUTO_MERGE pr=#M sha=<sha de merge> gate=<enlace a la evidencia> review=<enlace al CONFORME>` y después el `RELEASE` habitual.
- Cualquier persona con autoridad de merge puede revertir. Si la fusión rompe algo, quien la hizo abre un issue y una PR de reversión, y deja un checkpoint.
- El auto-merge no amplía permisos: solo sustituye la autorización por PR dentro del alcance reservado y de las condiciones de arriba.
