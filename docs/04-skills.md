# 4. Skills: convertir tus procesos en agentes expertos

Una skill es un procedimiento tuyo (un SOP) escrito una vez y ejecutado siempre
con la misma calidad. Es la diferencia entre explicar cómo publicar la web cada
vez y decir `/publicar-web`.

## Anatomía

Una skill es una carpeta con un archivo:

```
.claude/skills/publicar-web/SKILL.md
```

```markdown
---
name: publicar-web
description: Publica este proyecto en internet con Vercel. Úsala cuando el
  usuario quiera desplegar, publicar o poner online el sitio.
---

# Instrucciones paso a paso...
```

- **`name`**: el nombre. También se invoca escribiendo `/publicar-web`.
- **`description`**: lo más importante del archivo. Claude decide con esta línea
  si la skill aplica a lo que le acabas de pedir. Tiene que decir **qué hace** y
  **cuándo usarla**, con las palabras que tú usarías de verdad.
- **Cuerpo**: el procedimiento. Concreto, con comandos reales y criterios de
  verificación.

## Las skills de este repo

| Skill | Qué hace |
|---|---|
| `publicar-web` | Verifica, despliega en Vercel y confirma en producción |
| `nueva-landing` | Crea una landing de cliente completa, desde el brief |
| `nueva-seccion-web` | Añade géneros, preguntas o secciones al sitio principal |
| `reporte-cliente` | Redacta el reporte periódico a partir del trabajo real |
| `capturar-nota` | Guarda una nota bien clasificada y enlazada en el vault |

Léelas: son el mejor ejemplo de cómo escribir las tuyas.

## Cómo escribir una buena skill

1. **Hazlo primero a mano.** No escribas el SOP de algo que nunca has hecho.
2. **Apunta lo que decidiste**, no solo lo que tecleaste. El valor está en los
   criterios: qué revisar, qué hacer si falla, cuándo parar.
3. **Incluye los comandos exactos**, copiables.
4. **Termina con la verificación.** Una skill sin comprobación final produce
   trabajo que parece terminado y no lo está.
5. **Di explícitamente qué NO hacer.** "No inventes testimonios" evita más
   problemas que diez párrafos de buenas intenciones.

## Cuándo crear una

A la tercera vez que repites algo. Antes de eso, todavía no sabes cuál es el
proceso bueno; después, ya estás perdiendo tiempo.

## Errores típicos

| Error | Consecuencia |
|---|---|
| `description` vaga ("ayuda con la web") | Nunca se activa sola |
| SOP de 40 pasos | Nadie lo mantiene y queda desactualizado |
| Sin criterio de verificación | Trabajo a medias que parece terminado |
| Datos sensibles escritos dentro | Se suben al repo con el resto |
