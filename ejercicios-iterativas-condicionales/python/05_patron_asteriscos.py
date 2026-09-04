"""Ejercicio Basico 5: Impresion de patrones simples.

Imprime N lineas: la linea i contiene i asteriscos.
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
    n = leer_entero_positivo("Ingrese la cantidad de lineas (N): ")

    print()
    for i in range(1, n + 1):
        # Se arma la linea con un ciclo interno, igual que en el pseudocodigo.
        linea = ""
        for _ in range(i):
            linea += "*"
        print(linea)


if __name__ == "__main__":
    main()
