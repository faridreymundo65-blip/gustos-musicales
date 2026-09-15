# Gustos Musicales — taller de Claude Code

Repositorio del curso. Contiene dos sitios web reales y toda la infraestructura
de automatización que se construye a lo largo de los módulos: memoria, skills,
subagentes, MCP, automatizaciones y segundo cerebro.

Sin frameworks, sin build, sin dependencias. HTML, CSS y JavaScript puro.

## Empezar

```bash
bash scripts/servir.sh
```

- Sitio principal: http://localhost:8000/
- Landing Cafetal: http://localhost:8000/landing-page/

## Qué hay aquí

| Ruta | Qué es |
|---|---|
| `index.html`, `css/`, `js/` | Sitio "Gustos Musicales": géneros, test interactivo y artistas |
| `landing-page/` | Landing de ejemplo "Cafetal", café por suscripción |
| `CLAUDE.md` | Memoria persistente del proyecto |
| `.claude/skills/` | 5 skills: procesos repetibles convertidos en agentes |
| `.claude/agents/` | 4 subagentes especializados |
| `.claude/settings.json` | Permisos y hook de registro de cambios |
| `.mcp.json.example` | Plantilla para conectar herramientas externas |
| `segundo-cerebro/` | Vault de Obsidian con el método PARA |
| `docs/` | Guías del curso, una por pilar |
| `vercel.json` | Configuración de despliegue |

## Skills disponibles

| Comando | Qué hace |
|---|---|
| `/publicar-web` | Verifica y publica en Vercel |
| `/nueva-landing` | Crea una landing completa desde el brief del cliente |
| `/nueva-seccion-web` | Añade géneros, preguntas o secciones al sitio |
| `/reporte-cliente` | Redacta el reporte periódico desde el trabajo real |
| `/capturar-nota` | Guarda una nota clasificada y enlazada en el vault |

## Subagentes

`investigador` · `copywriter` · `revisor-qa` · `organizador-notas`

Se invocan en lenguaje natural: *"lanza el revisor-qa antes de publicar"*.

## Documentación

Empieza por [`docs/00-ruta-del-curso.md`](docs/00-ruta-del-curso.md): mapea cada
pilar del curso con el archivo de este repositorio que lo implementa.

## Publicar

```bash
npx vercel --prod
```

O conecta el repositorio a Vercel y cada push despliega solo.
Detalles en [`docs/02-despliegue-vercel.md`](docs/02-despliegue-vercel.md).

## Seguridad

`.env`, `.mcp.json` y `.claude/settings.local.json` están en `.gitignore`.
Nunca subas credenciales: en la configuración MCP usa variables (`${API_KEY}`),
nunca la clave escrita en el archivo.
