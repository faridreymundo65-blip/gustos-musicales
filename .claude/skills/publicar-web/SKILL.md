---
name: publicar-web
description: Publica este proyecto en internet con Vercel. Úsala cuando el usuario quiera desplegar, publicar, subir a producción, poner online el sitio o la landing, o cuando pregunte por la URL pública del proyecto.
---

# Publicar la web en Vercel

SOP de despliegue. Este proyecto es estático puro: no hay build, Vercel sirve
los archivos tal cual. Todo el despliegue sale del directorio raíz del repo.

## Antes de publicar (obligatorio)

1. Levanta el sitio en local y compruébalo:
   ```bash
   bash scripts/servir.sh
   ```
   Abre `http://localhost:8000/` y revisa: nada roto, sin errores en la consola
   del navegador, y que a 375px de ancho se vea correctamente.
2. Confirma que no hay secretos a punto de subirse:
   ```bash
   git status --short
   ```
   Si aparecen `.env`, `.mcp.json` o cualquier clave, **detente** y avisa al usuario.
3. Commitea lo que falte, con mensaje en español.

## Publicar

```bash
npx vercel login      # solo la primera vez
npx vercel            # despliegue de previsualización (URL temporal)
npx vercel --prod     # despliegue a producción
```

- El primer `vercel` pregunta el alcance, el nombre del proyecto y el directorio.
  Acepta el directorio raíz (`./`) y **no** configures ningún framework: es "Other".
- `vercel.json` ya define URLs limpias, cabeceras de seguridad y caché de assets.
  No hace falta tocarlo.

## Después de publicar

1. Abre la URL que devuelve Vercel y verifica en el sitio real: navegación, test
   de géneros, filtros de artistas y formulario.
2. Prueba también `/landing-page/`.
3. Dale al usuario la URL de producción en claro, en una línea.
4. Anota el despliegue en `segundo-cerebro/10-Proyectos/` (fecha, URL y qué cambió).

## Errores frecuentes

| Síntoma | Causa | Solución |
|---|---|---|
| 404 en la raíz | Vercel apunta a un subdirectorio | Vuelve a enlazar con `npx vercel --cwd .` |
| CSS no carga | Ruta absoluta `/css/...` en el HTML | Usa rutas relativas: `css/style.css` |
| Cambios que no aparecen | Se desplegó preview, no producción | Repite con `--prod` |
| Pide login en cada comando | Sesión no guardada | `npx vercel login` otra vez |
