# AGENTS.md — instrucciones para agentes

## Fuentes y alcance

Lee [README.md](README.md), la [guía](docs/COOPERACION_AUTONOMA.md), el [plan maestro #1](https://github.com/EspacioKoop/normas_platino/issues/1), el [registro único #2](https://github.com/EspacioKoop/normas_platino/issues/2), sus comentarios y el issue concreto antes de editar. Estos números pertenecen exclusivamente a normas_platino.

Este repositorio documenta reglas comunitarias. Conserva lo existente, usa español de España y ejemplos adaptables. No conviertas Atlas ni contratos arquitectónicos del juego de referencia en obligaciones generales. El README debe permitir a un agente encontrar todas las fuentes y adaptar las normas sin memoria de chat.

## Ciclo obligatorio

1. Comprueba rama, checkout, cambios locales, plan, reservas y PR existentes. Elige el pendiente prioritario libre dentro del alcance autorizado.
2. Publica en #2, antes de modificar archivos:

   `CLAIM issue=#N agent=<nombre> branch=agent/N-slug files=<rutas> goal=<objetivo>`

3. Relee inmediatamente todas las reservas. La activa anterior por fecha de GitHub gana; en empate, el ID de comentario menor. Si hay solape, no edites: coordina o libera y reclama otro bloque.
4. Usa rama `agent/N-slug` y checkout propios desde la base actual. No alteres cambios desconocidos ni ramas ajenas. Commits pequeños y pushes frecuentes, previa revisión de privacidad y estado remoto.
5. Subdivide únicamente si archivos y criterios son independientes. README.md, AGENTS.md y la guía son archivos compartidos: reserva sus rutas y acuerda un único escritor o una secuencia explícita. No sobrescribas trabajo ajeno al resolver conflictos.
6. Comprueba enlaces locales, coherencia normativa, bloques de código, ejemplos, `git diff --check` y ausencia de secretos. Revisa que ninguna afirmación de estado exceda la evidencia. Este repositorio no tiene CI configurada: indícalo, no inventes checks verdes. Si se establecen checks exigidos, deben pasar para el SHA actual.
7. Abre PR hacia `main`, enlaza el issue y registra `PR_READY` en #2 con PR, SHA, pruebas y límites. No libera la reserva ni autoriza merge.
8. Integra sólo con autorización explícita y controles satisfechos. Prohibidos force-push, reescritura compartida y push directo a `main`. La inicialización vacía autorizada del repositorio no es una excepción reutilizable.
9. Verifica el resultado remoto; actualiza el plan coordinadamente y publica `RELEASE`. Al abandonar, deja checkpoint antes de liberar. Al pausar, publica estado, SHA, próximos pasos y reserva explícita: no caduca por silencio.
10. Relee plan y reservas y selecciona otro bloque libre si el mandato sigue vigente. Si no hay trabajo autorizado, informa del cierre sin inventar tareas ni crear automatización persistente.

## Seguridad y entrega

No publiques tokens, cookies, claves, contraseñas, datos personales, infraestructura privada ni información de otros dominios. Revisa también diffs, logs, capturas, adjuntos y descripciones de PR. Una autorización para este repositorio no permite modificar otros ni ampliar credenciales o permisos.

El PR incluye alcance, documentos modificados, requisitos cumplidos, comprobaciones reales, limitaciones y reversión mediante otro PR si fuese necesaria. `Closes #N` sólo para cierre completo; `Refs #N` para entrega parcial. No cierres criterios por una intención, un placeholder o una revisión pendiente.
