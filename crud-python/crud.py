"""CRUD de alumnos en consola (Python + MySQL)."""

from mysql.connector import Error

from conexion import conectar


def crear():
    """CREATE: inserta un alumno nuevo."""
    matricula = input("Matricula: ").strip()
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    edad = input("Edad: ").strip()
    carrera = input("Carrera: ").strip()

    conexion = conectar()
    if not conexion:
        return
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO alumnos (matricula, nombre, apellido, edad, carrera) "
            "VALUES (%s, %s, %s, %s, %s)",
            (matricula, nombre, apellido, edad, carrera),
        )
        conexion.commit()
        print(f"Alumno registrado con id {cursor.lastrowid}")
    except Error as e:
        print(f"No se pudo registrar: {e}")
    finally:
        conexion.close()


def leer():
    """READ: muestra todos los alumnos."""
    conexion = conectar()
    if not conexion:
        return
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT id, matricula, nombre, apellido, edad, carrera "
            "FROM alumnos ORDER BY id"
        )
        filas = cursor.fetchall()
        if not filas:
            print("No hay alumnos registrados.")
            return
        print(f"\n{'ID':<4}{'MATRICULA':<12}{'NOMBRE':<15}{'APELLIDO':<15}{'EDAD':<6}CARRERA")
        print("-" * 70)
        for id_, matricula, nombre, apellido, edad, carrera in filas:
            print(f"{id_:<4}{matricula:<12}{nombre:<15}{apellido:<15}{edad:<6}{carrera}")
        print()
    except Error as e:
        print(f"No se pudo consultar: {e}")
    finally:
        conexion.close()


def actualizar():
    """UPDATE: modifica los datos de un alumno por su id."""
    id_ = input("Id del alumno a modificar: ").strip()
    nombre = input("Nuevo nombre: ").strip()
    apellido = input("Nuevo apellido: ").strip()
    edad = input("Nueva edad: ").strip()
    carrera = input("Nueva carrera: ").strip()

    conexion = conectar()
    if not conexion:
        return
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "UPDATE alumnos SET nombre = %s, apellido = %s, edad = %s, carrera = %s "
            "WHERE id = %s",
            (nombre, apellido, edad, carrera, id_),
        )
        conexion.commit()
        if cursor.rowcount:
            print("Alumno actualizado.")
        else:
            print("No existe un alumno con ese id.")
    except Error as e:
        print(f"No se pudo actualizar: {e}")
    finally:
        conexion.close()


def eliminar():
    """DELETE: borra un alumno por su id."""
    id_ = input("Id del alumno a eliminar: ").strip()
    if input(f"Seguro que deseas eliminar el id {id_}? (s/n): ").strip().lower() != "s":
        print("Cancelado.")
        return

    conexion = conectar()
    if not conexion:
        return
    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM alumnos WHERE id = %s", (id_,))
        conexion.commit()
        if cursor.rowcount:
            print("Alumno eliminado.")
        else:
            print("No existe un alumno con ese id.")
    except Error as e:
        print(f"No se pudo eliminar: {e}")
    finally:
        conexion.close()


MENU = """
===== CRUD DE ALUMNOS =====
1. Registrar alumno
2. Mostrar alumnos
3. Actualizar alumno
4. Eliminar alumno
5. Salir
"""


def main():
    opciones = {"1": crear, "2": leer, "3": actualizar, "4": eliminar}
    while True:
        print(MENU)
        opcion = input("Elige una opcion: ").strip()
        if opcion == "5":
            print("Hasta luego.")
            break
        accion = opciones.get(opcion)
        if accion:
            accion()
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
