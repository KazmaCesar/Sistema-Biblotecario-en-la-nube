# conexion_bd.py
import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",     
            user="u647795385_root",
            password="1Q2w3e4rasd?",
            database="u647795385_BD_biblioteca"
        )
        if conexion.is_connected():
            return conexion
    except Error as e:
        raise ConnectionError(f"Error al conectar con la base de datos: {e}")
