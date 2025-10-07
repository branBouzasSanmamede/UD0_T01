from conexion import obtener_db

def mostrar_colecciones():

    db = obtener_db()
    colecciones = db.list_collection_names()
    print("\n".join(c for c in colecciones) if colecciones else "No hay colecciones")