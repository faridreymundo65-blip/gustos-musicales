# 6. Subagentes: un equipo trabajando en paralelo

Un subagente es un trabajador especializado con **su propia ventana de contexto**.
Recibe un encargo, trabaja por su cuenta y te devuelve solo el resultado.

## Por qué importa

Dos razones, y la segunda es la buena:

1. **Paralelismo**: varios agentes trabajando a la vez en cosas distintas.
2. **Contexto limpio**: un agente puede leer treinta archivos y devolverte tres
   párrafos. Esos treinta archivos nunca entran en tu conversación. Tu ventana
   de contexto se mantiene despejada para lo que importa.

La segunda razón es la que hace que las sesiones largas sigan razonando bien.

## Los agentes de este repo

| Agente | Especialidad | Herramientas |
|---|---|---|
| `investigador` | Busca en la web y devuelve un informe con fuentes | Lectura + web |
| `copywriter` | Escribe textos de venta en español | Lectura + edición |
| `revisor-qa` | Encuentra lo roto antes de publicar | Lectura + comandos |
| `organizador-notas` | Ordena y enlaza el segundo cerebro | Lectura + edición |

Fíjate en la columna de herramientas: **cada agente tiene solo lo que necesita**.
El `investigador` no puede editar archivos, y el `revisor-qa` no puede arreglar
nada — solo reportar. Un agente con menos permisos comete menos destrozos.

## Anatomía

`.claude/agents/revisor-qa.md`:

```markdown
---
name: revisor-qa
description: Revisa el sitio antes de publicar buscando enlaces rotos...
tools: Read, Grep, Glob, Bash
model: sonnet
---

Eres el control de calidad. Tu trabajo es...
```

- **`description`**: cuándo llamarlo. Misma lógica que en las skills.
- **`tools`**: la lista mínima. Si lo omites, hereda todas.
- **`model`**: `haiku` para tareas mecánicas y baratas, `sonnet` para el trabajo
  normal, `opus` para razonamiento difícil.
- **Cuerpo**: su rol, su método y sus límites.

## Cómo se usan

Pídelo en lenguaje natural:

> "Lanza el revisor-qa sobre el sitio antes de publicar"

> "Que el investigador analice tres competidores de café por suscripción
> mientras el copywriter reescribe el hero de Cafetal"

El segundo ejemplo es el patrón "ultracode": **dos agentes, dos ventanas de
contexto, a la vez**. El tiempo total es el del más lento, no la suma.

## Cómo repartir bien el trabajo

- Tareas **independientes** entre sí. Si el agente B necesita el resultado de A,
  no hay paralelismo posible: van en orden.
- Encargos **cerrados**: "revisa enlaces, accesibilidad y responsive de
  index.html", no "mejora la web".
- El resultado de un agente es **una propuesta**, no una verdad. Los subagentes
  también se equivocan: revisa antes de aplicar.

## Cuándo NO usarlos

Para una tarea corta que tú mismo haces en dos pasos. Arrancar un agente tiene
un coste fijo: si la tarea es más barata que el arranque, hazla directamente.
