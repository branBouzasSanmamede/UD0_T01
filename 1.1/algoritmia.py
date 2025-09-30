import conversor, par_impar, frecuencia_caracteres, calculadora, orden_palabras, num_primo, gestion_notas, juego
import utilBran

menu_algoritmia = [
    (1, "Conversor temperaturas", conversor.conversor_temperaturas),
    (2, "Numeros pares/impares", par_impar.par_impar),
    (3, "Frecuencia de caracteres", frecuencia_caracteres.frecuencia_caracteres),
    (4, "Calculadora basica", calculadora.calculadora),
    (5, "Ordenacion de palabras", orden_palabras.ordenacion_palabras),
    (6, "Numeros primos en un rango", num_primo.num_primo),
    (7, "Gestion de notas", gestion_notas.gestion_notas),
    (8, "Juego de adivinanza", juego.juego_adivinanza)
]

def main():
    utilBran.ejecutar_menu(menu_algoritmia)

if __name__ == "__main__":
    main()