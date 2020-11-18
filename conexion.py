import mysql.connector

bd = mysql.connector.connect(user='edgar', password='12345678', database='nopalito')

cursor = bd.cursor()

def get_usuarios():
    consulta = "SELECT * FROM usuario"

    cursor.execute(consulta)
    usuarios = []
    for row in cursor.fetchall():
        usuario = {
            'Id' : row[0],
            'Nombre': row[1],
            'Apellidos':row[2],
            'Contraseña':row[3]
        }
        usuarios.append(usuario)
    return usuarios

def existe_usuario(nombre):
    query = "SELECT COUNT(*) FROM usuario WHERE nombre = %s"
    cursor.execute(query, (nombre,))

    if cursor.fetchone()[0] == 1:
        return True
    else:
        return False

import hashlib
def crear_usuario(nombre, apellidos, password):
    if existe_usuario(nombre):
        return False
    else:
        h = hashlib.new('sha256', bytes(password, 'utf-8'))
        h = h.hexdigest()
        insertar = "INSERT INTO usuario(nombre, apellidos, contraseña) VALUES(%S, %s, %s)"
        cursor.execute(insertar, (nombre, apellidos, password))
        bd.commit()

        return True
