"""Conexion unica a MySQL para el CRUD de alumnos."""

import mysql.connector
from mysql.connector import Error

CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "TU_PASSWORD",   # <-- cambia esto por tu contrasena de MySQL
    "database": "escuela",
    "port": 3306,
}


def conectar():
    """Devuelve una conexion abierta, o None si falla."""
    try:
        conexion = mysql.connector.connect(**CONFIG)
        if conexion.is_connected():
            return conexion
    except Error as e:
        print(f"Error al conectar con MySQL: {e}")
    return None


if __name__ == "__main__":
    con = conectar()
    if con:
        print("Conexion exitosa a la base de datos 'escuela'")
        con.close()
