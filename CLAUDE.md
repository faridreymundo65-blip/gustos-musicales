# CLAUDE.md — Memoria del proyecto

Este archivo es la **memoria persistente** de Claude Code en este repositorio.
Se carga automáticamente al inicio de cada sesión, así que lo que esté aquí no
hace falta volver a explicarlo nunca.

> Regla de oro: si algo tuviste que explicar dos veces, va en este archivo.

## Qué es este repositorio

Taller práctico del curso de Claude Code. Contiene dos sitios estáticos reales
y toda la infraestructura de automatización que se construye a lo largo de los
módulos (memoria, skills, subagentes, MCP, loops y segundo cerebro).

No hay framework, ni build, ni dependencias: es HTML + CSS + JavaScript puro.
Se abre en el navegador tal cual y se despliega en Vercel sin compilar nada.

## Estructura

```
index.html, css/, js/        Sitio "Gustos Musicales" (test interactivo de géneros)
landing-page/                Landing de ejemplo "Cafetal" (café por suscripción)
docs/                        Guías del curso, módulo por módulo
.claude/skills/              Skills = procesos repetibles (SOPs) convertidos en agentes
.claude/agents/              Subagentes especializados que trabajan en paralelo
.claude/settings.json        Permisos y hooks del proyecto
.mcp.json.example            Plantilla de conexión a herramientas externas vía MCP
segundo-cerebro/             Vault de Obsidian: notas, proyectos, clientes, plantillas
scripts/                     Utilidades (servidor local de previsualización)
vercel.json                  Configuración de despliegue
```

## Comandos

```bash
bash scripts/servir.sh          # Previsualizar en http://localhost:8000
bash scripts/servir.sh 3000     # Elegir otro puerto
npx vercel --prod               # Desplegar a producción (requiere login previo)
```

No hay tests automatizados. La verificación es visual: abrir la página, revisar
que no haya errores en la consola del navegador y probar en ancho de móvil.

## Convenciones de código

- **Idioma**: todo el contenido visible, los comentarios y los commits van en español.
- **CSS**: los colores y tipografías se definen como variables en `:root`. Nunca
  escribas un color literal (`#d4af37`) en una regla; usa `var(--primary)`.
- **JS**: sin frameworks ni librerías externas. JavaScript moderno (const/let,
  arrow functions, template literals), sin dependencias de npm.
- **Datos**: los géneros, artistas y preguntas del test viven en los arrays del
  principio de `js/script.js`. Para añadir contenido se edita ese array, no el HTML.
- **HTML**: semántico y accesible — `alt` en imágenes, `aria-label` en botones de
  icono, contraste suficiente sobre el fondo oscuro.
- **Responsive**: todo debe verse bien a 375px de ancho. Es obligatorio comprobarlo.

## Paleta del sitio principal

Oscura, elegante y atrevida. Definida en `css/style.css`:

| Variable      | Valor     | Uso                          |
|---------------|-----------|------------------------------|
| `--bg`        | `#07060a` | Fondo principal              |
| `--card`      | `#16121f` | Tarjetas y superficies       |
| `--text`      | `#f5f0e8` | Texto principal              |
| `--primary`   | `#d4af37` | Dorado: acentos y botones    |
| `--accent`    | `#e0115f` | Rosa intenso: énfasis        |
| `--purple`    | `#4b1d8f` | Degradados y fondos suaves   |

La landing `landing-page/` tiene su propia paleta cálida y no comparte estilos
con el sitio principal. Son proyectos independientes.

## Git

- Rama de trabajo actual: `claude/intelligent-fermat-3vhmv0`.
- Commits en español, en imperativo y explicando el *qué*: "Agregar sección de
  playlists", no "cambios varios".
- Nunca subas `.env`, `.mcp.json` con credenciales reales, ni claves de API.

## Cómo trabajar en este repo

1. Antes de crear algo nuevo, mira si ya existe una skill en `.claude/skills/`.
2. Para tareas largas de investigación, delega en los subagentes de `.claude/agents/`.
3. Cuando termines algo que valga la pena recordar, anótalo en `segundo-cerebro/`.
4. Si un proceso lo repites por tercera vez, conviértelo en una skill.
