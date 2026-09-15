---
titulo: Gustos Musicales
fecha: 2026-09-15
tipo: proyecto
estado: activo
cliente: propio
fecha-fin: 
tags: [proyecto, web]
---

# Gustos Musicales

## Objetivo
Un sitio web publicado donde cualquiera pueda explorar géneros musicales y
descubrir el suyo con un test de 5 preguntas.

## Estado actual
Sitio funcionando en local: 8 géneros, test de 5 preguntas, filtros de artistas,
formulario de contacto y paleta oscura aplicada. Falta desplegar a producción.

## Siguientes pasos
- [ ] Desplegar en Vercel con la skill `publicar-web`
- [ ] Pasar el subagente `revisor-qa` antes de publicar
- [ ] Añadir más géneros latinos (bachata, cumbia)

## Decisiones tomadas
| Fecha | Decisión | Por qué |
|---|---|---|
| 2026-09 | Sin frameworks, HTML/CSS/JS puro | Carga rápida y se despliega sin build |
| 2026-09 | Los datos viven en arrays de `js/script.js` | Añadir un género es editar 6 líneas |
| 2026-09 | Paleta oscura con dorado y rosa | Coherente con la temática musical nocturna |

## Enlaces
- Repositorio: https://github.com/faridreymundo65-blip/gustos-musicales
- URL en producción: (pendiente)
- Relacionado: [[claude-code-apuntes]]
