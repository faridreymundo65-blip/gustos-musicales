# 3. Contexto y memoria: que la IA no empiece de cero cada día

Este es el módulo que más cambia tu día a día, y el que más gente se salta.

## La ventana de contexto

La ventana de contexto es todo lo que la IA tiene delante en este momento: tu
petición, los archivos que leyó, los resultados de los comandos y la conversación
previa. Es **finita**.

Dos consecuencias prácticas:

1. **Se llena.** Cuando se acerca al límite, la conversación se resume
   automáticamente y los detalles finos se pierden.
2. **La calidad baja antes de llenarse.** Una sesión con tres tareas distintas
   mezcladas razona peor que una sesión enfocada, aunque quepa todo.

### Cómo cuidarla

| Situación | Qué hacer |
|---|---|
| Cambias de tarea | `/clear` — empieza limpio |
| La sesión va muy larga y quieres seguir | `/compact` — resume y continúa |
| Necesitas que algo se recuerde siempre | Escríbelo en `CLAUDE.md` |
| Vas a leer un archivo enorme | Pide solo la parte que importa |
| Investigación pesada | Delégala a un subagente (ver guía 6) |

La regla: **una sesión, una tarea**. Es gratis abrir otra.

## CLAUDE.md: la memoria que sí persiste

`CLAUDE.md` se carga automáticamente al inicio de **cada** sesión. Es la
diferencia entre un becario nuevo cada mañana y alguien que ya conoce la casa.

En este repo, `CLAUDE.md` guarda: qué es el proyecto, la estructura de carpetas,
los comandos, las convenciones de código, la paleta de colores y las reglas de
git. Nada de eso hay que volver a explicarlo nunca.

### Qué va dentro y qué no

**Sí:**
- Cómo se ejecuta y se prueba el proyecto.
- Convenciones que no se deducen mirando el código.
- Decisiones ya tomadas ("sin frameworks", "todo en español").
- Rutas donde viven las cosas.

**No:**
- Lo que se ve leyendo el código.
- Cosas de una sola vez ("hoy arregla el botón").
- Documentación larga: para eso enlazas a `docs/`.

### Cómo mantenerlo

```
/init    # genera un CLAUDE.md inicial analizando el repositorio
```

Y durante el trabajo, empieza un mensaje con `#` para añadir una regla a la
memoria sin cortar lo que estás haciendo:

```
# los precios siempre se muestran en pesos, con separador de miles
```

**La señal clara**: si tuviste que explicar algo dos veces, no es culpa de la IA.
Es una línea que falta en `CLAUDE.md`.

## Jerarquía de memoria

1. `~/.claude/CLAUDE.md` — tus preferencias, en todos tus proyectos.
2. `CLAUDE.md` del proyecto — se comparte con quien clone el repo.
3. `.claude/settings.local.json` — ajustes tuyos de este proyecto, sin subir.

Lo personal arriba, lo del equipo en el repo. Nunca metas credenciales en
ninguno de los tres.
