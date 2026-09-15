---
name: capturar-nota
description: Guarda una idea, aprendizaje, reunión, contacto o recurso en el segundo cerebro de Obsidian con la plantilla correcta y los enlaces adecuados. Úsala cuando digan "guarda esto", "anótalo", "apunta esta idea" o pidan documentar algo en las notas.
---

# Capturar una nota en el segundo cerebro

El vault vive en `segundo-cerebro/` y sigue el método PARA. Una nota que no está
enlazada es una nota perdida: **siempre** se conecta con algo.

## 1. Decidir dónde va

| Tipo de contenido | Carpeta |
|---|---|
| Idea suelta, sin procesar aún | `00-Inbox/` |
| Algo con fecha de fin y objetivo | `10-Proyectos/` |
| Responsabilidad continua (clientes, finanzas, salud) | `20-Areas/` |
| Material de referencia, apuntes, recursos | `30-Recursos/` |
| Terminado o ya irrelevante | `40-Archivo/` |

Si dudas entre dos, va a `00-Inbox/`. Ya se moverá al procesarla.

## 2. Crear la nota

Copia la plantilla que corresponda desde `segundo-cerebro/90-Plantillas/`:

- `plantilla-nota.md` — idea o apunte general
- `plantilla-proyecto.md` — proyecto con objetivo y fecha
- `plantilla-cliente.md` — ficha de cliente
- `plantilla-reunion.md` — acta de reunión con acuerdos

Nombre del archivo: `AAAA-MM-DD-titulo-en-minusculas.md`. Para fichas de cliente
o proyecto, usa el nombre propio: `cafetal.md`.

## 3. Rellenar bien el frontmatter

```yaml
---
titulo: Título legible
fecha: 2026-09-15
tipo: nota | proyecto | cliente | reunion
estado: activo | en-pausa | terminado
tags: [tema, cliente, canal]
---
```

## 4. Enlazar (esto es lo que hace que funcione)

- Enlaza con `[[nombre-de-la-nota]]` a cada nota relacionada que ya exista.
- Añade la nota al mapa de contenido `segundo-cerebro/MOC-Inicio.md` si abre un
  tema nuevo.
- Antes de crear una nota, **busca si ya existe** una sobre el tema:
  ```bash
  grep -ril "<tema>" segundo-cerebro/
  ```
  Si existe, amplíala en vez de duplicarla. Dos notas sobre lo mismo valen menos
  que una buena.

## 5. Cerrar

Resume al usuario en una línea qué guardaste y dónde, con la ruta del archivo.
