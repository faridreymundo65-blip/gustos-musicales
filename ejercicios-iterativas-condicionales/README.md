# Ejercicios sobre el uso de estructuras iterativas y condicionales

Resolución de los 10 ejercicios del documento *"Ejercicios sobre el uso de
estructuras iterativas y condicionales"*. Cada ejercicio está resuelto dos veces:

- **Pseudocódigo para PSeInt** en `pseint/` (archivos `.psc`)
- **Programa en Python** en `python/` (archivos `.py`)

Ambas versiones siguen la misma lógica, así el pseudocódigo se puede leer al
lado del código para comparar estructura por estructura.

## Índice de ejercicios

### Nivel básico (estructuras iterativas)

| # | Ejercicio | PSeInt | Python | Estructura usada |
|---|-----------|--------|--------|------------------|
| 1 | Tabla de multiplicar | [01](pseint/01_tabla_multiplicar.psc) | [01](python/01_tabla_multiplicar.py) | `Para` / `for` |
| 2 | Suma de los primeros N números | [02](pseint/02_suma_primeros_n.psc) | [02](python/02_suma_primeros_n.py) | `Para` / `for` con acumulador |
| 3 | Contador regresivo | [03](pseint/03_contador_regresivo.psc) | [03](python/03_contador_regresivo.py) | `Para` con paso -1 / `range` descendente |
| 4 | Acumulado hasta cero | [04](pseint/04_acumulado_hasta_cero.psc) | [04](python/04_acumulado_hasta_cero.py) | `Repetir-Hasta Que` / `while True` + `break` |
| 5 | Impresión de patrones simples | [05](pseint/05_patron_asteriscos.psc) | [05](python/05_patron_asteriscos.py) | Ciclos anidados |

### Nivel intermedio (iterativas + condicionales)

| # | Ejercicio | PSeInt | Python | Estructura usada |
|---|-----------|--------|--------|------------------|
| 6 | Clasificador de pares e impares | [06](pseint/06_clasificador_pares_impares.psc) | [06](python/06_clasificador_pares_impares.py) | `Para` + `Si/SiNo` anidado |
| 7 | Validación de contraseña (3 intentos) | [07](pseint/07_validacion_password.psc) | [07](python/07_validacion_password.py) | `Mientras` con doble condición |
| 8 | Números primos en un rango | [08](pseint/08_primos_en_rango.psc) | [08](python/08_primos_en_rango.py) | `Para` + `Mientras` anidado |
| 9 | Promedio con filtrado de notas | [09](pseint/09_promedio_con_filtrado.psc) | [09](python/09_promedio_con_filtrado.py) | `Mientras` con centinela negativo |
| 10 | Juego de adivinanza con pistas | [10](pseint/10_juego_adivinanza.psc) | [10](python/10_juego_adivinanza.py) | `Mientras` + `Si/SiNo Si` |

## Cómo ejecutar

### PSeInt

1. Abrir PSeInt.
2. `Archivo > Abrir` y seleccionar el archivo `.psc` deseado de la carpeta `pseint/`.
3. Ejecutar con **F9** (o el botón ▶).

> Los algoritmos usan el perfil de sintaxis flexible de PSeInt. Si el perfil
> configurado es estricto (`Configurar > Opciones del lenguaje`), basta con
> activar "Permitir asignar valores en la declaración" y usar el perfil
> *Flexible* para que corran sin cambios.

### Python

Requiere Python 3. Desde la carpeta `python/`:

```bash
python3 01_tabla_multiplicar.py
```

Cada programa es independiente y se ejecuta desde la terminal.

## Notas de implementación

- **Validación de entrada**: los programas en Python usan una función auxiliar
  (`leer_entero`, `leer_entero_positivo`, `leer_real`) que vuelve a preguntar si
  el usuario escribe algo que no es un número, para que el programa no se caiga.
- **Ejercicio 7**: la contraseña predefinida es `python2024` (constante
  `CLAVE_CORRECTA`), con un máximo de 3 intentos.
- **Ejercicio 8**: para decidir si un número es primo solo se prueban divisores
  hasta su raíz cuadrada (`divisor * divisor <= numero`), que es más eficiente
  que recorrer hasta el número completo. Si el usuario invierte el rango
  (inicio > fin), los valores se intercambian automáticamente.
- **Ejercicio 9**: las notas menores a 5 se descartan tanto de la suma como del
  conteo, por lo que el promedio se calcula solo con las notas aprobatorias. Si
  no hubo ninguna, se avisa en vez de dividir entre cero.
- **Ejercicio 10**: en Python el número secreto se genera con
  `random.randint(1, 100)`; en PSeInt con la función `Aleatorio(1, 100)`. Para
  probar siempre con el mismo número, se puede reemplazar por un valor fijo.
