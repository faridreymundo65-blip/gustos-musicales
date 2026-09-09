import mysql.connector

# configuracion de conexion
conexion = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="matricula"
    # port=3307,   <- descomenta esta linea si tu MySQL usa el puerto 3307
)

cursor = conexion.cursor(dictionary=True)


# funciones del crud
def crear_alumno(codalu, patalu, matalu, nombre, edad, sexo, direc, dist, correo):
    cursor.execute(
        "insert into alumno (cod_alumno, pat_alu, mat_alu, nom_alu, edad_alu, "
        "sexo_alu, direc_alu, dist_alu, correo_alu) "
        "values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        (codalu, patalu, matalu, nombre, edad, sexo, direc, dist, correo)
    )
    conexion.commit()

    print("alumno insertado.!!")


def leer_alumnos():
    cursor.execute(
        "select cod_alumno, pat_alu, mat_alu, nom_alu, edad_alu, sexo_alu, "
        "dist_alu, correo_alu from alumno order by cod_alumno"
    )
    alumnos = cursor.fetchall()

    if not alumnos:
        print("\n No hay alumnos\n")
        return

    print("\n Lista de Alumnos")
    print("-" * 100)
    for a in alumnos:
        print(
            f"{a['cod_alumno']:<10}{a['pat_alu']:<14}{a['mat_alu']:<14}"
            f"{a['nom_alu']:<20}{a['edad_alu']:<5}{a['sexo_alu']:<4}"
            f"{a['dist_alu'] or '':<20}{a['correo_alu'] or ''}"
        )
    print(f"\n Total: {len(alumnos)} alumnos\n")


def buscar_alumno(codalu):
    cursor.execute("select * from alumno where cod_alumno = %s", (codalu,))
    alumno = cursor.fetchone()

    if not alumno:
        print("\n No existe ese alumno\n")
        return

    print()
    for campo, valor in alumno.items():
        print(f" {campo:<12}: {valor}")
    print()


def actualizar_alumno(codalu, patalu, matalu, nombre, edad, sexo, direc, dist, correo):
    cursor.execute(
        "update alumno set pat_alu=%s, mat_alu=%s, nom_alu=%s, edad_alu=%s, "
        "sexo_alu=%s, direc_alu=%s, dist_alu=%s, correo_alu=%s "
        "where cod_alumno=%s",
        (patalu, matalu, nombre, edad, sexo, direc, dist, correo, codalu)
    )
    conexion.commit()

    if cursor.rowcount:
        print("alumno actualizado.!!")
    else:
        print("no existe ese alumno")


def eliminar_alumno(codalu):
    cursor.execute("delete from alumno where cod_alumno = %s", (codalu,))
    conexion.commit()

    if cursor.rowcount:
        print("alumno eliminado.!!")
    else:
        print("no existe ese alumno")


# datos que se piden por teclado
def pedir_datos():
    patalu = input("Apellido paterno: ").upper()
    matalu = input("Apellido materno: ").upper()
    nombre = input("Nombres: ").upper()
    edad = input("Edad: ")
    sexo = input("Sexo (M/F): ").upper()
    direc = input("Direccion: ").upper()
    dist = input("Distrito: ").upper()
    correo = input("Correo: ")
    return patalu, matalu, nombre, edad, sexo, direc, dist, correo


# menu principal
def menu():
    while True:
        print("""
========= CRUD DE ALUMNOS =========
1. Registrar alumno   (INSERT)
2. Listar alumnos     (SELECT)
3. Buscar por codigo  (SELECT)
4. Actualizar alumno  (UPDATE)
5. Eliminar alumno    (DELETE)
6. Salir
""")
        opcion = input("Elige una opcion: ")

        if opcion == "1":
            codalu = input("Codigo (ej. ALU-020): ").upper()
            crear_alumno(codalu, *pedir_datos())

        elif opcion == "2":
            leer_alumnos()

        elif opcion == "3":
            buscar_alumno(input("Codigo del alumno: ").upper())

        elif opcion == "4":
            codalu = input("Codigo del alumno a modificar: ").upper()
            print("Ingresa los nuevos datos:")
            actualizar_alumno(codalu, *pedir_datos())

        elif opcion == "5":
            codalu = input("Codigo del alumno a eliminar: ").upper()
            if input(f"Seguro que deseas eliminar a {codalu}? (s/n): ").lower() == "s":
                eliminar_alumno(codalu)
            else:
                print("cancelado")

        elif opcion == "6":
            cursor.close()
            conexion.close()
            print("hasta luego")
            break

        else:
            print("opcion no valida")


menu()
