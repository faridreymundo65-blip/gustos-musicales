"""Control de carga de un montacargas — versión corregida.

Mejoras sobre la versión original:
  1. El peso 0 funciona como centinela para cerrar la carga.
  2. Una caja rechazada ya no cancela todo el proceso.
  3. Valida la entrada: rechaza pesos negativos y texto no numérico.
  4. Informa la capacidad disponible y por cuántos kg se excede una caja.
  5. El resumen final incluye cajas rechazadas y capacidad sin usar.
"""

CAPACIDAD_MAX = 1000


def leer_peso(disponible):
    """Pide un peso hasta que el usuario ingrese un número >= 0."""
    while True:
        try:
            texto = input(f"Peso de la caja en kg (0 para terminar) [libre: {disponible} kg]: ")
        except EOFError:
            print("\nEntrada cerrada. Se cierra la carga.")
            return 0

        try:
            peso = float(texto)
        except ValueError:
            print("Entrada inválida: escriba un número, por ejemplo 12.5")
            continue

        if peso < 0:
            print("Peso inválido: debe ser un número positivo.")
            continue

        return peso


def main():
    total_peso = 0
    cajas_aceptadas = 0
    cajas_rechazadas = 0
    continuar = True

    print(f"=== Control de carga (capacidad: {CAPACIDAD_MAX} kg) ===")

    while continuar:
        disponible = CAPACIDAD_MAX - total_peso
        peso = leer_peso(disponible)

        if peso == 0:
            # El operario decide cerrar la carga
            continuar = False

        elif total_peso + peso <= CAPACIDAD_MAX:
            total_peso += peso
            cajas_aceptadas += 1
            print(f"Caja aceptada. Total: {total_peso} kg")

            if total_peso == CAPACIDAD_MAX:
                print("Capacidad máxima alcanzada. Se cierra la carga.")
                continuar = False

        else:
            cajas_rechazadas += 1
            exceso = (total_peso + peso) - CAPACIDAD_MAX
            print(f"¡ALERTA! Excede capacidad por {exceso} kg. Caja rechazada.")
            print(f"Puede intentar con una caja de hasta {disponible} kg.")
            # No se corta el proceso: quizá la siguiente caja sí quepa

    print("--- Resumen de la carga ---")
    print(f"Carga total: {total_peso} kg en {cajas_aceptadas} cajas.")
    print(f"Cajas rechazadas: {cajas_rechazadas}")
    print(f"Capacidad sin usar: {CAPACIDAD_MAX - total_peso} kg")


if __name__ == "__main__":
    main()
