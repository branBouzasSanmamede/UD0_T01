from conexion import obtener_db
from alumno import Alumno

def insertar_documentos():
    db = obtener_db()
    coleccion = db["alumnos"]

    alumnos = [
        Alumno("Pepe", 20, 8.5),
        Alumno("Pepito", 18, 6.3),
        Alumno("Manolo", 40, 4.9),
        Alumno("Juan", 25, 5)
    ]

    documentos = [a.to_dict() for a in alumnos]
    coleccion.insert_many(documentos)