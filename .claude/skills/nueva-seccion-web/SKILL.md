---
name: nueva-seccion-web
description: Añade una sección nueva al sitio Gustos Musicales (nuevo género, bloque de artistas, playlists, sección de contenido). Úsala cuando pidan ampliar, agregar contenido o crear un apartado nuevo en el sitio principal.
---

# Añadir una sección al sitio Gustos Musicales

El sitio se alimenta de datos, no de HTML escrito a mano. Casi siempre la tarea
es editar un array en `js/script.js`, no tocar `index.html`.

## Caso A: añadir un género musical

Es el caso más común y **solo requiere editar datos**.

1. Añade el objeto al array `genres` al principio de `js/script.js`:
   ```js
   {
     id: "bachata",
     icon: "🪘",
     name: "Bachata",
     description: "Guitarra dominicana y romanticismo para bailar pegado.",
     artists: ["Juan Luis Guerra", "Romeo Santos", "Aventura", "Prince Royce"],
   },
   ```
2. No hace falta nada más: la cuadrícula de géneros, los filtros de artistas y
   el desplegable del formulario se generan solos desde ese array.
3. Añade el género a alguna pregunta del test (`quizQuestions`) para que pueda
   salir como resultado. Si no aparece en ningún `scores`, nunca ganará.

## Caso B: añadir preguntas al test

Añade objetos a `quizQuestions` con esta forma exacta:
```js
{
  question: "¿Texto de la pregunta?",
  options: [
    { text: "Opción visible", scores: { rock: 2, hiphop: 1 } },
  ],
}
```
La barra de progreso se recalcula sola con el número de preguntas.

## Caso C: sección completamente nueva

1. En `index.html`, añade un `<section id="...">` dentro de `<main>`, siguiendo el
   patrón existente: un `div.section-title` con `<h2>` y `<p>`, y luego el contenido.
2. Añade el enlace en la navegación (`ul.nav-links`).
3. Estilos al final de `css/style.css`, usando siempre `var(--...)` de `:root`.
4. Si la sección tiene datos repetidos, decláralos como array en `js/script.js` y
   genera el HTML con `createElement`, igual que hacen `genres` y los artistas.

## Verificación

```bash
bash scripts/servir.sh
```
Comprueba: la sección aparece, el enlace del menú salta a ella, se ve bien a
375px, el test sigue funcionando de principio a fin y la consola no tiene errores.
