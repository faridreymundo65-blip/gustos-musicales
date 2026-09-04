"""Ejercicio Basico 2: Suma de los primeros N numeros.

Pide un entero positivo N y suma todos los numeros desde 1 hasta N.
"""


def leer_entero_positivo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print("Valor invalido: debe ingresar un numero entero.")
            continue

        if valor > 0:
            return valor
        print("El numero debe ser mayor que cero.")


def main():
    n = leer_entero_positivo("Ingrese un numero entero positivo (N): ")

    suma = 0
    for i in range(1, n + 1):
        suma += i

    print(f"La suma de los numeros del 1 al {n} es: {suma}")


if __name__ == "__main__":
    main()
