from conexion import obtener_db
from alumno import Alumno

def recuperar_alumnos():
    db = obtener_db()
    coleccion = db["alumnos"]
    resultados = coleccion.find()
    for r in resultados:
        if r["nota"] >= 7:
            alumno = Alumno(r["nombre"], r["edad"], r["nota"])
            print(alumno)