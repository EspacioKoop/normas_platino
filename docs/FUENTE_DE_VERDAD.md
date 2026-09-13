# GitHub como fuente de verdad y memoria recuperable

[Inicio](../README.md) · [Cooperación](COOPERACION_AUTONOMA.md) · [Planificación y entregas](PLANIFICACION_Y_ENTREGAS.md)

## Norma platino

**Los repositorios de GitHub son la fuente de toda la verdad del proyecto.** Su código, documentos versionados, issues, comentarios, reservas, PR, revisiones y evidencias deben permitir saber dónde quedó cada cosa: qué está hecho, qué se estaba haciendo, qué se terminó, qué queda por hacer y cuál es el siguiente paso. Una persona o agente debe poder retomar el trabajo aunque se pierda por completo el contexto del chat, cambie el modelo o desaparezca la sesión anterior.

Cada proyecto identifica su repositorio canónico y enlaza sus fuentes desde README y AGENTS. Si abarca varios repositorios, el plan enlaza el responsable de cada componente, sin duplicar su estado ni mezclar dominios. Esta norma no cambia la autoridad humana, los permisos ni las fronteras de privacidad; tampoco convierte una afirmación escrita en evidencia de que algo funciona.

Los chats, la memoria de una IA, las notas locales y los tableros externos son canales de apoyo, **no una fuente de verdad alternativa**. Las decisiones, autorizaciones y cambios de alcance relevantes se trasladan de forma saneada al issue o documento canónico antes de ejecutar el trabajo afectado. No se copian conversaciones privadas. Tener una orden no equivale a tener una reserva ni amplía los permisos concedidos.

## Dónde queda cada cosa

- **Código y documentos:** archivos versionados y commits publicados. Una modificación que sólo existe en un checkout local no está recuperable desde GitHub.
- **Prioridad, alcance global y dependencias:** plan maestro y roadmap, enlazando las tareas sin duplicar su historial operativo.
- **Trabajo hecho, en curso y pendiente; decisiones y bloqueos:** issue canónico de cada tarea, con su checkpoint vigente y enlaces a los anteriores.
- **Responsable y titularidad de archivos:** registro único de reservas. El checkpoint enlaza el CLAIM y su estado; no crea un registro paralelo.
- **Candidato, revisión e integración:** rama, SHA, PR, revisiones y controles sobre ese candidato. Una rama publicada o un PR cerrado no demuestran integración.
- **Producto distribuido o desplegado:** release, artefactos y evidencia autorizada del despliegue cuando proceda. Ni HEAD ni un PR fusionado prueban publicación o despliegue.

Projects, si se adopta, refleja estas fuentes conforme al esquema real. Un README, wiki o tablero desactualizado no prevalece sobre los hechos comprobados. Ante una discrepancia, contrasta commits, estado remoto, decisiones vigentes y pruebas; corrige el resumen afectado con referencia a la evidencia, conservando el historial. No elijas una versión sólo por ser la más reciente ni borres un pendiente para cuadrar el relato. Si sigue sin poder resolverse o requiere una decisión de autoridad, registra la contradicción y bloquea sólo el alcance afectado.

## Cuándo actualizar

El responsable del trabajo mantiene el issue canónico actualizado al completar un bloque significativo, cambiar el estado o tomar una decisión; y **antes de pausar, ceder el trabajo, cerrar la sesión o terminar la tarea**. Si se prevé una pérdida de contexto o compactación, deja primero el checkpoint. No esperes al final de una sesión larga: una interrupción inesperada puede perder lo no publicado.

Publica los commits recuperables tras revisar privacidad y enlázalos desde el checkpoint. El trabajo incompleto puede quedar en una rama o PR borrador autorizado, identificado como tal, nunca como entrega terminada. Si algo no puede publicarse, registra de forma saneada qué falta y su límite de recuperación; no des por respaldado un cambio local ni subas datos privados para cumplir esta norma.

Actualiza el plan o roadmap cuando cambien sus prioridades, alcance o estado integrado; el registro cuando cambie la reserva; y el PR cuando cambien el candidato o su evidencia. Enlaza el checkpoint desde esas fuentes cuando sea pertinente, sin copiar todo el estado en cada una. Un relevo, bloqueo, revisión o conclusión de «ya estaba hecho» también deja constancia en la tarea, para que el siguiente agente no repita la investigación. No se exige comentar cada acción mecánica.

## Checkpoint mínimo de tarea

Publica una actualización en el issue canónico, con datos reales y enlaces. Los marcadores siguientes son una plantilla, no evidencia; sustituye cada uno o indica `no aplica`, `ninguno` o `no verificado` con motivo.

```markdown
## Checkpoint de continuidad
- Fecha de actualización y responsable: <fecha con zona horaria; persona/agente>
- Tarea y objetivo vigente: <issue canónico; alcance y aceptación>
- Estado: <pendiente / en curso / bloqueado / listo para revisión / integrado / terminado>
- Hecho: <resultados completados y enlaces; distinguir implementación de integración>
- En curso: <punto exacto donde se detuvo el trabajo; ninguno si no hay trabajo activo>
- Pendiente: <pasos restantes y criterios de aceptación aún abiertos>
- Bloqueos y dependencias: <causa; quién o qué puede resolverla>
- Decisiones y autorización vigente: <acuerdo saneado, límites y referencia>
- Artefactos: <repositorio, rama, SHA completo publicado y PR; ninguno si no existen>
- Cambios no publicados: <detalle saneado, conservación autorizada y límites de recuperación; o ninguno>
- Evidencia: <comprobaciones realizadas, resultado, SHA, entorno, enlaces y límites>
- Reserva: <URL del CLAIM; retenida, liberada o cedida con referencia al registro>
- Siguiente paso: <acción concreta, responsable o rol y condición para continuar>
- No repetir: <trabajo ya resuelto, descartado con motivo o cubierto por otra entrega>
```

Usa `sha=none` si no hay commit publicado. Separa explícitamente **implementado**, **probado localmente**, **listo para revisión**, **integrado**, **publicado**, **desplegado** y **playtest humano** cuando sean aplicables. «Terminado» exige toda la aceptación cumplida y la integración verificada cuando corresponda. Un PR abierto, una revisión pendiente, CI verde o una casilla marcada no satisfacen por sí solos los demás criterios. Los controles automáticos de documentos no prueban el cumplimiento real de esta rutina.

## Recuperar el trabajo sin contexto previo

1. Abre el repositorio canónico y lee README, AGENTS y la revisión de normas adoptada. Sigue sus enlaces a plan, roadmap y registro de reservas; no reconstruyas el proyecto sólo desde el chat o la memoria.
2. Localiza la tarea y lee su checkpoint, decisiones, comentarios pertinentes, dependencias y PR enlazados. Lee el registro completo de reservas, incluida su paginación. Comprueba también si existe una entrega equivalente antes de iniciar otra.
3. Contrasta el checkpoint con el estado remoto actual: rama base y SHA, ramas publicadas, PR, revisiones, checks e integración. Un checkpoint histórico no certifica el HEAD actual. Inspecciona aparte los cambios locales sin sobrescribirlos.
4. Reconstruye qué está hecho, qué sigue en curso, qué falta, qué bloquea y el siguiente paso. Lo desconocido queda como **no verificado**; investiga en las fuentes o pregunta por la decisión que realmente falte, sin inventar progreso ni repetir trabajo por defecto.
5. Confirma mandato y titularidad. Reanudar exige conservar la reserva; una reserva liberada requiere nuevo CLAIM y relectura. La pérdida de contexto o el silencio no ceden archivos ajenos. Registra cualquier corrección del estado y continúa sólo el bloque autorizado.

Si GitHub no está disponible, conserva un checkpoint local seguro con la última revisión conocida y lo pendiente de publicar. Declara que el estado remoto no está comprobado: no adquieras reservas, no publiques ni integres a ciegas. Limita la actividad a trabajo independiente ya autorizado que no requiera coordinación remota actual. Al recuperar acceso, reconcilia primero los cambios y reservas remotos y publica el relevo pendiente antes de retomar el trabajo compartido.

## Privacidad y conservación

«Fuente de toda la verdad» se refiere a la verdad **del proyecto dentro de su dominio autorizado**. No obliga a publicar secretos, datos personales, infraestructura privada ni información de otros proyectos, aunque el repositorio sea privado. Guarda los datos protegidos en su destino autorizado; en GitHub deja sólo el estado o referencia saneada que pueda compartirse, y declara las dependencias de acceso sin exponer ubicaciones sensibles.

GitHub como fuente canónica no equivale a un backup completo: un clon Git no conserva por sí solo issues, comentarios, revisiones ni todos los artefactos. La copia de seguridad de esos recursos necesita un alcance y destino autorizados; esta norma no crea servicios, crons ni exportaciones automáticas.
