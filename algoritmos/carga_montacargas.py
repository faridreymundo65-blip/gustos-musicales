"""Control de carga de un montacargas — versión original.

Traducción directa del pseudocódigo `CargaMontacargas`.
El bucle solo termina cuando una caja excede la capacidad máxima.
"""

CAPACIDAD_MAX = 1000
total_peso = 0
cajas_aceptadas = 0
continuar = True

while continuar:
    peso = float(input("Ingrese peso de la caja (kg): "))

    if total_peso + peso <= CAPACIDAD_MAX:
        total_peso = total_peso + peso
        cajas_aceptadas = cajas_aceptadas + 1
        print("Caja aceptada.")

    else:
        print("¡ALERTA! Excede capacidad. Caja rechazada.")
        continuar = False

print("Carga total:", total_peso, "kg en", cajas_aceptadas, "cajas.")
