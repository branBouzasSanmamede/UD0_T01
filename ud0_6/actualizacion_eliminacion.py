from utils.utilBran import ejecutar_menu
from conexion import obtener_db
from alumno import Alumno

db = obtener_db()
coleccion = db["alumnos"]

def listar_alumnos():
    for doc in coleccion.find():
        print(Alumno(doc["nombre"], doc["edad"], doc["nota"]))

def obtener_alumno():
    while True:
        alumno = input("Introduce el alumno")
        doc = coleccion.find_one({"nombre": alumno})
        if doc:
            return doc 
        else:
            print(f"No se encontro el alumno {alumno}")
            listar_alumnos()

def actualizar_nota():
    alumno = obtener_alumno()

    while True:
        try:
            nota = float(input("Introduce la nota: "))
            break
        except ValueError:
            print("Introduce un numero valido!")

    coleccion.update_one(
        {"_id": alumno["_id"]},
        {"$set": {"nota": nota}}
    )
    listar_alumnos()

def eliminar_alumnos():
    coleccion.delete_many({"nota": {"$lt": 5}})
    listar_alumnos()

opciones = [
    (1, "Actualiza la nota", actualizar_nota),
    (2, "Eliminar todos los alumnos", eliminar_alumnos)
]

def main():
    ejecutar_menu(opciones)