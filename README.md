Proyecto práctico para la implementación del ciclo completo de gestión de incidencias y observabilidad de software en Python.

## Objetivo
Aplicar técnicas de depuración, registro de eventos (logs) y gestión de incidencias para evidenciar el flujo: **Detección → Registro → Asignación → Resolución → Cierre**.

## Metodología
1. **Detección**: Análisis y *debugging* en VS Code para identificar errores.
2. **Registro**: Implementación de `logging` (INFO, WARNING, ERROR, CRITICAL) persistiendo en `app.log`.
3. **Gestión**: Registro de incidencias en Jira/Sentry clasificadas por severidad.
4. **Matriz de Impacto**: Clasificación técnica de incidencias.
5. **Resolución**: Corrección del código y actualización del tablero.

## Tecnologías Utilizadas
* **Lenguaje**: Python 3.x
* **Entorno**: Visual Studio Code (Depuración activa)
* **Gestión de Proyectos**: Jira / Sentry
* **Control de Versiones**: Git / GitHub

## Estructura del Repositorio
* `/src`: Código fuente base y corregido.
* `/logs`: Archivos de registro de eventos.
* `/evidencias`: Capturas de consola, *tracebacks* y tableros.

---
*Desarrollado como parte de la Maestría en Ingeniería de Software (UNEMI).*