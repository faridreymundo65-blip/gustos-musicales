# Trabajo Final de Curso — PIAD-221

**Algoritmos y Programación para Desarrollo de Software** · Tecnologías de la Información

**Tema:** Sistema de Gestión de Inventario y Registro de Ventas para una Microempresa
(aplicación de consola en Python).

> Los datos personales del informe (nombres, ID, instructor, sección, fecha, ciudad)
> están marcados como `[COLOCAR ...]` tanto en la carátula del documento Word como en
> la cabecera del archivo `.py`, para completarlos antes de la entrega.

## Contenido del entregable

| Carpeta / archivo | Descripción |
|---|---|
| `codigo/sistema_inventario.py` | **Entregable principal.** Aplicación de consola: 1 538 líneas, 51 funciones documentadas. |
| `codigo/datos/` | Archivos de texto generados por el programa (inventario, ventas y bitácora de errores). |
| `documento/PIAD-221_Trabajo_Final.docx` | Informe completo (72 páginas) para editar y entregar. |
| `documento/PIAD-221_Trabajo_Final.pdf` | Copia en PDF del informe, lista para imprimir. |
| `diagramas/` | Figuras A–E: arquitectura modular, flujo del menú, modelo de datos, manejo de excepciones y flujo de venta. |
| `capturas/` | 17 capturas de pantalla de la ejecución real del programa. |

## Ejecución

```bash
cd codigo
python sistema_inventario.py      # en Linux/macOS: python3 sistema_inventario.py
```

Requiere Python 3.8 o superior. No usa librerías externas: solo `os`, `sys` y `datetime`.
La carpeta `datos/` se crea automáticamente en la primera ejecución.

## Cumplimiento de las condiciones del caso práctico

1. **Programación modular** — 51 funciones en 5 capas (configuración, persistencia,
   validación, lógica de negocio e interfaz), sin programación lineal ni monolítica.
2. **Manejo robusto de excepciones** — 20 bloques `try` (32 `except` y 9 `finally`) que
   capturan `ValueError`, `FileNotFoundError`, `PermissionError`, `OSError`, `KeyError`,
   `UnicodeDecodeError` y `KeyboardInterrupt`.
3. **Persistencia en texto plano** — 6 operaciones de disco, todas con `with open(...)`
   y los modos `r` (carga), `w` (inventario) y `a` (ventas y bitácora).

Menú interactivo con `while` + `if-elif-else` y opción de salida, inventario como lista
de diccionarios, ventas como diccionario anidado, descuento por volumen e IGV del 18 %.

## Índice del informe Word

El índice es un campo automático de Word con su resultado ya calculado. Si se modifica
el documento, basta con hacer clic derecho sobre el índice → **Actualizar campos**.
