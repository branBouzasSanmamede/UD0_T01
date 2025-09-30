from utils import utilBran
from ud0_1 import algoritmia
from ud0_2 import secuencias
from ud0_3 import funciones
from ud0_4 import programacion_objetos
from ud0_5 import fichero
from ud0_6 import conexion_mongo
from ud0_7 import proyecto

menu_principal = [
    (1, "Algoritmia e interacción con el usuario", algoritmia.main),
    (2, "Secuencias y diccionarios", secuencias.main),
    (3, "Funciones", funciones.main),
    (4, "Programación Orientada a Objetos", programacion_objetos.main),
    (5, "Lectura y escritura de ficheros (texto y JSON)", fichero.main),
    (6, "Conexión con MongoDB", conexion_mongo.main),
    (7, "Proyecto", proyecto.main),
]

def main():
    utilBran.ejecutar_menu(menu_principal)

if __name__ == "__main__":
    main()