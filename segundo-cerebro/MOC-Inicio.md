---
titulo: Mapa de contenido — Inicio
fecha: 2026-09-15
tipo: moc
estado: activo
tags: [indice]
---

# 🧠 Segundo cerebro

Punto de entrada al vault. Si una nota importa, se enlaza desde aquí o desde
otro mapa de contenido. Lo que no está enlazado, no existe.

## Estructura (método PARA)

| Carpeta | Qué guarda | Pregunta que responde |
|---|---|---|
| `00-Inbox/` | Todo lo que entra sin clasificar | "Luego lo ordeno" |
| `10-Proyectos/` | Objetivo concreto + fecha de fin | ¿En qué estoy trabajando? |
| `20-Areas/` | Responsabilidades continuas | ¿Qué debo mantener siempre? |
| `30-Recursos/` | Material de consulta | ¿Dónde estaba aquello? |
| `40-Archivo/` | Terminado o irrelevante | Historial |
| `90-Plantillas/` | Plantillas de notas | — |

## Proyectos activos

- [[gustos-musicales]] — sitio web sobre géneros musicales con test interactivo
- [[cafetal]] — landing de café de especialidad por suscripción

## Áreas

- Clientes
- Aprendizaje de automatización con IA
- Finanzas

## Recursos

- [[claude-code-apuntes]] — lo aprendido del curso, módulo a módulo

## Rutina de mantenimiento

**Cada semana** (10 minutos, lanza el subagente `organizador-notas`):
1. Vaciar `00-Inbox/`.
2. Actualizar el estado de los proyectos activos.
3. Archivar lo terminado.
4. Enlazar las notas huérfanas.
