"""Ejercicio Intermedio 3: Numeros primos en un rango.

Recorre el rango indicado por el usuario e imprime solo los numeros primos.
"""


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Valor invalido: debe ingresar un numero entero.")


def es_primo(numero):
    """Devuelve True si numero es primo.

    Basta con probar divisores hasta la raiz cuadrada del numero.
    """
    if numero < 2:
        return False

    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 1

    return True


def main():
    inicio = leer_entero("Ingrese el inicio del rango: ")
    fin = leer_entero("Ingrese el fin del rango: ")

    # Si el usuario invierte el rango, se intercambian los valores.
    if inicio > fin:
        inicio, fin = fin, inicio

    print(f"\nNumeros primos entre {inicio} y {fin}:")

    encontrados = 0
    for numero in range(inicio, fin + 1):
        if es_primo(numero):
            print(numero)
            encontrados += 1

    if encontrados == 0:
        print("No se encontraron numeros primos en el rango.")
    else:
        print(f"Total de primos encontrados: {encontrados}")


if __name__ == "__main__":
    main()
