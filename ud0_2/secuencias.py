from utils import utilBran
from ud0_2.diccionario import diccionario
from ud0_2.distancia_euclidiana import distanciaEuclidiana
from ud0_2.diccionario_inverso import diccionarioInverso
from ud0_2.lista_diccionarios import agenda

menu_secuencias = [
    (1, "Diccionario de frecuencias de palabras", diccionario),
    (2, "Tuplas y coordenadas", distanciaEuclidiana),
    (3, "Diccionario inverso", diccionarioInverso),
    (4, "Lista de diccionarios (agenda)", agenda)
]

def main():
    utilBran.ejecutar_menu(menu_secuencias)

if __name__ == "__main__":
    main()