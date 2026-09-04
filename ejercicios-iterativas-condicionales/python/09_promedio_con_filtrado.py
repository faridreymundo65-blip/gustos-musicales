"""Ejercicio Intermedio 4: Calculadora de promedio con filtrado.

Lee calificaciones hasta que se ingresa un numero negativo. Las notas
menores a 5 (reprobatorias) se ignoran en la suma y en el conteo.
"""

NOTA_MINIMA_APROBATORIA = 5


def leer_real(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Valor invalido: debe ingresar un numero.")


def main():
    suma = 0.0
    contadas = 0
    ignoradas = 0

    print("Ingrese las calificaciones. Un numero negativo finaliza el ingreso.")

    nota = leer_real("Calificacion: ")
    while nota >= 0:
        if nota >= NOTA_MINIMA_APROBATORIA:
            suma += nota
            contadas += 1
        else:
            ignoradas += 1
            print("  (Nota reprobatoria: no se toma en cuenta)")

        nota = leer_real("Calificacion: ")

    print("\n--- Resultados ---")
    print(f"Notas consideradas: {contadas}")
    print(f"Notas ignoradas:    {ignoradas}")

    if contadas > 0:
        promedio = suma / contadas
        print(f"Promedio (solo notas >= {NOTA_MINIMA_APROBATORIA}): {promedio:.2f}")
    else:
        print("No se ingresaron notas aprobatorias, no hay promedio.")


if __name__ == "__main__":
    main()
