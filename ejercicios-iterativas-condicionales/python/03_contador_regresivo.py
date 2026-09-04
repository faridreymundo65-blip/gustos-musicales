"""Ejercicio Basico 3: Contador regresivo.

Imprime una cuenta regresiva desde el numero ingresado hasta 0.
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
    n = leer_entero_positivo("Ingrese un numero entero positivo: ")

    print("\nCuenta regresiva:")
    for i in range(n, -1, -1):
        print(i)

    print("Despegue!")


if __name__ == "__main__":
    main()
