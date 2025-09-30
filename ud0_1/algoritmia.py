from ud0_1.conversor import conversor_temperaturas
from ud0_1.par_impar import par_impar
from ud0_1.frecuencia_caracteres import frecuencia_caracteres
from ud0_1.calculadora import calculadora
from ud0_1.orden_palabras import ordenacion_palabras
from ud0_1.num_primo import num_primo
from ud0_1.gestion_notas import gestion_notas
from ud0_1.juego import juego_adivinanza
from utils import utilBran

menu_algoritmia = [
    (1, "Conversor temperaturas", conversor_temperaturas),
    (2, "Numeros pares/impares", par_impar),
    (3, "Frecuencia de caracteres", frecuencia_caracteres),
    (4, "Calculadora basica", calculadora),
    (5, "Ordenacion de palabras", ordenacion_palabras),
    (6, "Numeros primos en un rango", num_primo),
    (7, "Gestion de notas", gestion_notas),
    (8, "Juego de adivinanza", juego_adivinanza)
]

def main():
    utilBran.ejecutar_menu(menu_algoritmia)

if __name__ == "__main__":
    main()