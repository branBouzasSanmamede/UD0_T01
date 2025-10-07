from utils import utilBran
from conexion_basica import mostrar_colecciones
from insercion_docs import insertar_documentos
from consulta_filtros import recuperar_alumnos
from actualizacion_eliminacion import main

menu_mongo = [
    (1, "Conexión básica", mostrar_colecciones),
    (2, "Inserción de documentos", insertar_documentos),
    (3, "Consulta con filtros", recuperar_alumnos),
    (4, "Actualización y eliminación", main)
]

def main():
    utilBran.ejecutar_menu(menu_mongo)

if __name__ == "__main__":
    main()