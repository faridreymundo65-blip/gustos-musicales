# Ruta del curso — de cero a agentes autónomos

Esta carpeta convierte el curso en algo que puedes ejecutar. Cada guía explica un
pilar y te dice **qué archivo de este repositorio** lo implementa, para que veas
el concepto funcionando en vez de leerlo en abstracto.

Ningún módulo pide saber programar. Pide leer con atención y probar.

## Orden recomendado

| # | Guía | Qué consigues | Ya construido aquí |
|---|---|---|---|
| 1 | [Ecosistema de IA](01-ecosistema-ia.md) | Saber qué herramienta usar para cada cosa | — |
| 2 | [Despliegue en Vercel](02-despliegue-vercel.md) | Tu web en internet, con URL real | `vercel.json`, skill `publicar-web` |
| 3 | [Contexto y memoria](03-contexto-y-memoria.md) | Que la IA recuerde entre sesiones | `CLAUDE.md` |
| 4 | [Skills](04-skills.md) | Tus procesos convertidos en agentes expertos | `.claude/skills/` (5 skills) |
| 5 | [MCP](05-mcp.md) | Conectar herramientas externas | `.mcp.json.example` |
| 6 | [Subagentes](06-subagentes.md) | Varios agentes trabajando en paralelo | `.claude/agents/` (4 agentes) |
| 7 | [Loops y Goals](07-loops-y-goals.md) | Automatizaciones que corren solas 24/7 | `.claude/settings.json` (hook) |
| 8 | [Segundo cerebro](08-segundo-cerebro.md) | Base de conocimiento conectada | `segundo-cerebro/` |

## Proyectos prácticos

| Proyecto | Estado | Dónde está |
|---|---|---|
| 1. Sitio web con test interactivo | ✅ hecho | `index.html`, `css/`, `js/` |
| 2. Landing page de cliente | ✅ hecho | `landing-page/` |
| 3. Memoria persistente del proyecto | ✅ hecho | `CLAUDE.md` |
| 4. Skills de procesos repetibles | ✅ hecho | `.claude/skills/` |
| 5. Equipo de subagentes | ✅ hecho | `.claude/agents/` |
| 6. Conexión MCP a herramientas | ⚙️ plantilla lista | `.mcp.json.example` |
| 7. Automatización recurrente | ⚙️ hook listo | `.claude/settings.json` |
| 8. Segundo cerebro en Obsidian | ✅ hecho | `segundo-cerebro/` |

Los marcados ⚙️ necesitan **tus** credenciales o tu decisión de qué automatizar:
son los dos puntos donde el curso no puede avanzar sin ti.

## Cómo estudiar esto

1. Lee la guía del pilar.
2. Abre el archivo del repo que la implementa y léelo entero.
3. Cambia algo pequeño y comprueba el efecto.
4. Anota lo aprendido en `segundo-cerebro/30-Recursos/claude-code-apuntes.md`.

El paso 4 es el que separa "hice un curso" de "sé hacerlo".
