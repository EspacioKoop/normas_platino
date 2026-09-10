# Normas Platino

**Cooperación autónoma entre agentes, sin colisiones ni pérdida de trabajo.**

Este repositorio contiene un protocolo reutilizable: los agentes eligen trabajo prioritario, reservan un alcance independiente, producen una entrega comprobada y la presentan mediante PR. Autonomía no significa permiso ilimitado ni integración sin autorización.

## Empieza aquí

1. Lee este README para conocer el mapa y la adaptación.
2. Lee [AGENTS.md](AGENTS.md): instrucciones para contribuir **a este repositorio**.
3. Consulta la [guía de cooperación](docs/COOPERACION_AUTONOMA.md): procedimiento, estados y plantillas copiables.
4. En el proyecto donde vayas a trabajar, localiza su plan maestro, registro único de reservas, instrucciones locales y pruebas canónicas **antes de editar**.

## Mapa del repositorio

- [README.md](README.md): propósito, navegación y adopción.
- [AGENTS.md](AGENTS.md): contrato operativo local para agentes.
- [docs/COOPERACION_AUTONOMA.md](docs/COOPERACION_AUTONOMA.md): protocolo comunitario completo y ejemplos.
- [Plan maestro #1](https://github.com/EspacioKoop/normas_platino/issues/1): prioridad, alcance, criterios y checkpoint de este proyecto.
- [Registro único #2](https://github.com/EspacioKoop/normas_platino/issues/2): reservas, coordinación, pausas y liberaciones.
- [Issues](https://github.com/EspacioKoop/normas_platino/issues): tareas y aceptación.
- [Pull requests](https://github.com/EspacioKoop/normas_platino/pulls): entregas, revisión y evidencia.

El plan determina **qué va primero**; el registro determina **quién puede editar qué**. Los issues concretan el trabajo y los PR acreditan su entrega. No mantengas una segunda cola o registro contradictorios en un chat.

## Adoptarlo en otro repositorio

1. Conserva y lee su documentación, licencias e instrucciones existentes. Integra estas normas; no reemplaces contratos locales a ciegas.
2. Identifica o crea, con autorización, **un plan maestro y un único registro de reservas por proyecto**. Enlázalos desde su README y AGENTS.md. No reutilices los números de este repositorio ni los del juego.
3. Define responsables, prioridad, dependencias, criterios de aceptación, rama base, pruebas canónicas, archivos compartidos y autoridad de merge.
4. Copia y adapta la ficha siguiente. Sustituye todos los campos antes de publicarla.
5. Incorpora el ciclo de la guía mediante PR y prueba su aplicación con una tarea pequeña. No hace falta implantar un bot ni un servicio.

```text
Proyecto: <organización/repositorio>
Instrucciones: <AGENTS.md y documentos locales>
Plan maestro: <URL canónica>
Registro único de reservas: <URL canónica>
Coordinación: <responsable y límites de autoridad>
Rama base: <rama protegida>
Prioridad y aceptación: <regla y ubicación>
Archivos compartidos: <rutas y propietario/secuencia de edición>
Pruebas canónicas: <comandos y workflows reales>
Autorización de merge: <quién autoriza y dónde queda registrada>
Fronteras de datos: <qué puede publicarse y qué queda privado>
Límites de autonomía: <objetivos, recursos, duración y condiciones de parada>
```

Los proyectos concretan su arquitectura y controles adicionales. No pueden interpretar una reserva como autorización para publicar secretos, ignorar una denegación, sobrescribir a otros o saltarse pruebas. Si dos instrucciones son incompatibles, detén el alcance afectado y pide resolución a la autoridad del proyecto.

## Reglas esenciales

- Escoge el pendiente prioritario libre y reserva **antes** de editar.
- Publica `CLAIM`, relee inmediatamente: gana la reserva activa anterior.
- Subdivide sólo con archivos y criterios independientes; coordina archivos compartidos.
- Trabaja en rama y checkout propios; commits pequeños y pushes frecuentes.
- Entrega funcionalidad real, pruebas proporcionales y CI exigida verde.
- Abre PR, registra `PR_READY` y espera autorización para integrar.
- Pausa con estado, SHA y próximos pasos; libera explícitamente con `RELEASE` al abandonar. El silencio no hace caducar reservas.
- Al acabar, relee plan/reservas y escoge otro bloque libre dentro del mandato vigente.
- Sin force-push, push directo a `main`, pérdida de trabajo ajeno ni filtración de secretos.

## Procedencia y alcance

Basado en las fuentes públicas de **espaciokooplagunakRemake**:

- [AGENTS.md](https://github.com/VaroTv7/espaciokooplagunakRemake/blob/main/AGENTS.md): contrato de colaboración.
- [Issue #1](https://github.com/VaroTv7/espaciokooplagunakRemake/issues/1): plan maestro y checkpoint validado.
- [Issue #7](https://github.com/VaroTv7/espaciokooplagunakRemake/issues/7): registro y acuerdos reales de reservas.
- [Conjunto de issues](https://github.com/VaroTv7/espaciokooplagunakRemake/issues): contexto público del trabajo.

Se generaliza el método, no las decisiones del juego: **Atlas/cosmografía es una reserva específica de ese proyecto**, no una norma comunitaria. Tampoco se imponen Godot, Foundry, su arquitectura, sus rutas, números de issue o la excepción histórica de integración directa del coordinador. Aquí la integración ordinaria siempre pasa por PR autorizado.

## Estado y contribuciones

Repositorio documental: no contiene un coordinador automático ni un sistema de bloqueo técnico. El protocolo requiere que sus participantes respeten y comprueben el registro. No hay CI configurada actualmente; validación local no equivale a CI verde. Los proyectos que lo adopten deben identificar sus checks reales y exigirlos antes de integrar.

Las mejoras se proponen mediante issue, reserva y PR conforme a [AGENTS.md](AGENTS.md). No se cambia la licencia ni la autoría de proyectos que adopten estas normas.
