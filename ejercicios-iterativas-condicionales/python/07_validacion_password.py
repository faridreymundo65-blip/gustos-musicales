"""Ejercicio Intermedio 2: Validacion de contrasena con intentos limitados.

Permite un maximo de 3 intentos para ingresar la contrasena correcta.
"""

CLAVE_CORRECTA = "python2024"
MAX_INTENTOS = 3


def main():
    intentos = 0
    acceso = False

    while intentos < MAX_INTENTOS and not acceso:
        intento = input("Ingrese la contrasena: ")
        intentos += 1

        if intento == CLAVE_CORRECTA:
            acceso = True
        else:
            restantes = MAX_INTENTOS - intentos
            if restantes > 0:
                print(f"Contrasena incorrecta. Le quedan {restantes} intento(s).")

    if acceso:
        print("Acceso concedido. Bienvenido!")
    else:
        print(f"Acceso bloqueado: se agotaron los {MAX_INTENTOS} intentos.")


if __name__ == "__main__":
    main()
