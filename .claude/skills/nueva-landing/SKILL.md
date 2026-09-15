---
name: nueva-landing
description: Crea una landing page completa para un cliente o producto nuevo, siguiendo la estructura de landing-page/. Úsala cuando pidan una landing, una página de ventas, una web de captación o una página para un cliente nuevo.
---

# Crear una landing page nueva

SOP para producir una landing de cliente con la misma calidad que
`landing-page/` (el ejemplo "Cafetal"), pero sin copiar su estilo.

## 1. Recoger el brief

Antes de escribir una línea de código, necesitas estos datos. Si falta alguno,
pregúntalo — no lo inventes:

- Nombre del negocio y a qué se dedica.
- A quién le vende (público objetivo concreto, no "todo el mundo").
- La oferta y el precio.
- Qué acción quieres que haga el visitante (comprar, agendar, escribir).
- Tono: cercano, técnico, premium, divertido.
- Colores o referencias visuales, si las tiene.

## 2. Crear la estructura

```bash
mkdir -p <nombre-cliente>/{css,js}
```

Archivos: `<nombre-cliente>/index.html`, `css/style.css`, `js/script.js`.
Cada landing es independiente: **no comparte CSS con el resto del repo**.

## 3. Secciones de la landing (en este orden)

1. **Header** con logo y navegación ancla + un botón de acción visible.
2. **Hero**: una promesa clara en el `<h1>`, subtítulo que explica cómo se cumple,
   y el botón principal. Nada de "Bienvenido a nuestra web".
3. **Cómo funciona**: 3 pasos numerados.
4. **Producto / servicio**: tarjetas con lo que se ofrece.
5. **Precios o planes**: máximo 3 opciones, con una destacada.
6. **Prueba social**: testimonios o datos reales. Si el cliente no tiene, deja el
   bloque preparado con un comentario HTML y **avísale** — no inventes reseñas.
7. **Preguntas frecuentes**: 4 a 6, respondiendo objeciones reales de compra.
8. **Cierre** con el mismo botón de acción del hero.
9. **Footer** con contacto y aviso legal.

## 4. Reglas técnicas

- HTML semántico, `lang="es"`, meta `description` escrita para buscadores.
- Paleta como variables CSS en `:root`. Ningún color literal suelto.
- Tipografías desde Google Fonts con `preconnect`.
- Menú hamburguesa funcional en móvil.
- Responsive obligatorio a 375px.
- Sin librerías externas: HTML, CSS y JS puro.

## 5. Verificar antes de entregar

```bash
bash scripts/servir.sh
```
Abre `http://localhost:8000/<nombre-cliente>/` y comprueba: todos los enlaces
ancla saltan a su sección, el menú móvil abre y cierra, el formulario responde,
y la consola del navegador está limpia.

Después, publica con la skill `publicar-web`.
