"""Ejercicio Intermedio 1: Clasificador de numeros pares e impares.

Cuenta cuantos numeros ingresados son pares, impares y cuantos son cero.
"""


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Valor invalido: debe ingresar un numero entero.")


def leer_entero_positivo(mensaje):
    while True:
        valor = leer_entero(mensaje)
        if valor > 0:
            return valor
        print("Debe ingresar al menos un numero.")


def main():
    cantidad = leer_entero_positivo("Cuantos numeros desea ingresar? ")

    pares = 0
    impares = 0
    ceros = 0

    for i in range(1, cantidad + 1):
        numero = leer_entero(f"Numero {i}: ")

        if numero == 0:
            ceros += 1
        elif numero % 2 == 0:
            pares += 1
        else:
            impares += 1

    print("\n--- Resumen ---")
    print(f"Pares:   {pares}")
    print(f"Impares: {impares}")
    print(f"Ceros:   {ceros}")


if __name__ == "__main__":
    main()
