from pymongo import MongoClient
from utils.utilBran import MONGO_URI

def obtener_db(nombre_db="testdb"):
    try:
        cliente = MongoClient(MONGO_URI)
    except Exception as e:
        print(f"Error al conectar con MongoDB: {e}")
    
    return cliente[nombre_db]