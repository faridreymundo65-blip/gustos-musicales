# Segundo cerebro

Vault de Obsidian de este taller. Se abre con **Obsidian → Abrir carpeta como
vault** apuntando a `segundo-cerebro/`, o se edita directamente como Markdown:
son archivos de texto normales, sin formato propietario.

Empieza por `MOC-Inicio.md`.

## Cómo se usa

1. **Captura sin pensar**: cualquier idea va a `00-Inbox/`. No te pares a decidir
   dónde. La fricción al capturar es lo que mata el sistema.
2. **Procesa una vez por semana**: vacía el inbox repartiendo cada nota según PARA.
3. **Enlaza siempre**: `[[nombre-de-la-nota]]`. El valor no está en las notas,
   está en las conexiones.
4. **Archiva sin culpa**: lo terminado va a `40-Archivo/`. No se borra.

Desde Claude Code, la skill `capturar-nota` hace los pasos 1 y 3 por ti, y el
subagente `organizador-notas` hace el 2 y el 4.

## Convenciones

- Archivos: `AAAA-MM-DD-titulo-en-minusculas.md`, salvo fichas de cliente o
  proyecto, que llevan su nombre propio (`cafetal.md`).
- Todas las notas empiezan con frontmatter (`titulo`, `fecha`, `tipo`, `estado`,
  `tags`).
- Las plantillas están en `90-Plantillas/`.
