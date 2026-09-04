"""Ejercicio Basico 1: Tabla de multiplicar.

Solicita un numero entero al usuario y muestra su tabla del 1 al 10.
"""


def leer_entero(mensaje):
    """Lee un entero desde teclado repitiendo hasta que el dato sea valido."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Valor invalido: debe ingresar un numero entero.")


def main():
    numero = leer_entero("Ingrese un numero entero: ")

    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


if __name__ == "__main__":
    main()
