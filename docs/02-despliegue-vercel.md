# 2. Despliegue: tu web en internet con Vercel

Un proyecto en tu carpeta no existe para nadie más. Este módulo lo pone online.

## Por qué Vercel

Es gratis para proyectos personales, conecta con GitHub y despliega solo en cada
push. Para un sitio estático como este —sin servidor, sin base de datos— es el
camino más corto entre tu carpeta y una URL pública.

## Requisitos

- Cuenta en [vercel.com](https://vercel.com) (con GitHub se crea en un clic).
- Node.js instalado, para poder usar `npx`.

## Opción A: desde la terminal (control total)

```bash
npx vercel login    # solo la primera vez
npx vercel          # despliegue de prueba, te da una URL temporal
npx vercel --prod   # despliegue definitivo
```

En el primer `vercel` te pregunta el directorio (acepta `./`) y el framework:
elige **Other**. Este proyecto no se compila.

## Opción B: conectado a GitHub (recomendado)

1. En Vercel: **Add New → Project → Import Git Repository**.
2. Elige `gustos-musicales`.
3. Framework Preset: **Other**. Root Directory: `./`. Build Command: vacío.
4. Deploy.

A partir de ahí, **cada push despliega solo**. Esto es lo que hace que el
despliegue deje de ser una tarea: se convierte en una consecuencia de trabajar.

## Qué hace `vercel.json`

```json
"cleanUrls": true     → /contacto en vez de /contacto.html
"headers"             → cabeceras de seguridad y caché larga para CSS y JS
```

No necesitas tocarlo salvo que añadas redirecciones o un dominio propio.

## Dominio propio

En el proyecto de Vercel: **Settings → Domains → Add**. Vercel te da los
registros DNS que hay que poner en tu proveedor del dominio. El certificado HTTPS
se genera solo, sin que hagas nada.

## Automatizarlo con Claude Code

La skill `publicar-web` ya tiene todo este proceso escrito, incluida la
verificación previa y la comprobación de que no subes secretos:

```
/publicar-web
```

Ese es el patrón del curso entero: un proceso que hiciste a mano una vez, escrito
en una skill, ejecutado igual de bien la vez cincuenta.
