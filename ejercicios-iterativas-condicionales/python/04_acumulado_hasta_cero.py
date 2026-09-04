"""Ejercicio Basico 4: Acumulado hasta cero.

Suma numeros ingresados por el usuario; el ciclo termina solo con el 0.
"""


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Valor invalido: debe ingresar un numero entero.")


def main():
    total = 0
    cantidad = 0

    print("Ingrese numeros para sumar. Escriba 0 para terminar.")

    while True:
        numero = leer_entero("Numero: ")
        if numero == 0:
            break

        total += numero
        cantidad += 1

    print(f"\nCantidad de numeros sumados: {cantidad}")
    print(f"Total acumulado: {total}")


if __name__ == "__main__":
    main()
