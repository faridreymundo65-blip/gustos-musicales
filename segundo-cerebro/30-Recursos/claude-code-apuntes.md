---
titulo: Apuntes de Claude Code
fecha: 2026-09-15
tipo: nota
estado: activo
tags: [ia, automatizacion, curso]
---

# Apuntes de Claude Code

Cuaderno del curso. Cada concepto, con el ejemplo real de este repositorio para
no quedarse en la teoría.

## Memoria: CLAUDE.md
Se carga solo al abrir cada sesión. Todo lo que tengas que explicar dos veces va
ahí. Ver `CLAUDE.md` en la raíz del repo.

## Ventana de contexto
Lo que la IA "tiene en la cabeza" ahora mismo. Es finita: cuanta más basura
metes, peor razona. Sesión nueva por cada tarea distinta, y la información
permanente en archivos, no en el chat. Ver `docs/03-contexto-y-memoria.md`.

## Skills
Un proceso que repites, escrito una vez y ejecutado siempre igual. Viven en
`.claude/skills/<nombre>/SKILL.md`. Ver `docs/04-skills.md`.

## Subagentes
Trabajadores especializados con su propia ventana de contexto. Sirven para
paralelizar y para no ensuciar la conversación principal. Viven en
`.claude/agents/`. Ver `docs/06-subagentes.md`.

## MCP
El enchufe universal: conecta herramientas externas (n8n, Notion, bases de datos)
a Claude Code sin escribir integraciones. Ver `docs/05-mcp.md`.

## Loops y Goals
Tareas que se repiten solas cada X tiempo sin que tú estés delante.
Ver `docs/07-loops-y-goals.md`.

## Ideas para probar
- [ ] 
