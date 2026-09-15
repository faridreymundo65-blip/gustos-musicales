# 7. Loops, hooks y automatización que corre sola

Hasta aquí, todo empieza porque tú escribes algo. Este módulo quita ese requisito.

Hay tres mecanismos distintos y conviene no confundirlos.

## 1. Hooks: reaccionar a un evento

Un hook es un comando que se dispara solo cuando pasa algo dentro de Claude Code.
No lo ejecuta la IA: lo ejecuta el programa. Por eso es fiable.

Este repo ya tiene uno funcionando en `.claude/settings.json`: cada vez que se
escribe o edita un archivo, se anota en `.claude/registro-cambios.log`.

```json
"hooks": {
  "PostToolUse": [
    {
      "matcher": "Write|Edit",
      "hooks": [{ "type": "command", "command": "..." }]
    }
  ]
}
```

Míralo funcionando:
```bash
cat .claude/registro-cambios.log
```

Eventos útiles:

| Evento | Cuándo se dispara | Ejemplo |
|---|---|---|
| `PostToolUse` | Tras usar una herramienta | Formatear o registrar lo editado |
| `PreToolUse` | Antes, y puede bloquear | Impedir tocar archivos protegidos |
| `SessionStart` | Al abrir sesión | Cargar el estado del proyecto |
| `Stop` | Al terminar una respuesta | Avisarte de que ya está |

Para crear o cambiar hooks, pídeselo a Claude Code: hay una skill (`update-config`)
que conoce el formato exacto. Revisa siempre el comando antes de aceptarlo.

## 2. Loops: repetir cada X tiempo

Un loop ejecuta la misma instrucción cada cierto intervalo, dentro de la sesión:

```
/loop 30m revisa si hay issues nuevos en el repositorio y resume los que pueda resolver
/loop 1h /reporte-cliente
```

Sin intervalo, el propio modelo decide cada cuánto volver, según lo que esté
esperando. Sirve para vigilar algo que cambia: un despliegue, un proceso largo,
una cola de trabajo.

**Un loop consume presupuesto cada vez que se despierta.** Ajusta el intervalo a
lo que realmente cambia: vigilar cada 5 minutos algo que cambia una vez al día es
tirar dinero.

## 3. Tareas programadas: correr sin ti delante

Para lo que debe ocurrir aunque tengas el ordenador cerrado —un resumen cada
lunes, una revisión diaria— se usan las tareas programadas de Claude Code en la
web (Routines): se definen con una expresión cron y arrancan una sesión nueva en
la nube cada vez que toca.

Diferencia clave con un loop: el loop vive dentro de tu sesión actual; la tarea
programada abre una sesión nueva, así que **su instrucción tiene que explicarse
sola**. No puede dar por supuesto nada de una conversación anterior.

## Goals: el objetivo por encima del paso

La idea que cierra el módulo: en vez de encadenar pasos, describes el estado al
que quieres llegar y dejas que el agente decida cómo.

> "El objetivo es que el sitio esté publicado y sin errores. Revisa con
> `revisor-qa`, arregla lo crítico, publica con `publicar-web` y dime la URL."

Para que esto funcione sin supervisión hacen falta tres cosas, y las tres ya
están en este repo: **memoria** (`CLAUDE.md`), **procesos escritos**
(`.claude/skills/`) y **verificación** (`revisor-qa`). Sin verificación no hay
autonomía, solo confianza ciega.

## Antes de dejar algo corriendo solo

1. Que haya funcionado **a mano** al menos una vez.
2. Que tenga una verificación automática de que salió bien.
3. Que no toque nada irreversible sin preguntar (borrar, enviar, cobrar, publicar
   en nombre de alguien).
4. Que sepas **cómo pararlo**.
