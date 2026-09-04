"""Ejercicio Intermedio 5: Juego de adivinanza con pistas.

El usuario debe adivinar un numero secreto entre 1 y 100. En cada intento
fallido el programa indica si el numero buscado es mayor o menor.
"""

import random

MINIMO = 1
MAXIMO = 100


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Valor invalido: debe ingresar un numero entero.")


def main():
    secreto = random.randint(MINIMO, MAXIMO)
    intentos = 0
    acerto = False

    print(f"Adivine el numero secreto entre {MINIMO} y {MAXIMO}.")

    while not acerto:
        intento = leer_entero("Su intento: ")

        if intento < MINIMO or intento > MAXIMO:
            print(f"El numero debe estar entre {MINIMO} y {MAXIMO}.")
            continue

        intentos += 1

        if intento == secreto:
            acerto = True
        elif intento < secreto:
            print(f"El numero buscado es MAYOR que {intento}")
        else:
            print(f"El numero buscado es MENOR que {intento}")

    print(f"\nCorrecto! El numero era {secreto}")
    print(f"Lo lograste en {intentos} intento(s).")


if __name__ == "__main__":
    main()
