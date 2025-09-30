from utils import utilBran
from ud0_5.contador import contador
from ud0_5.registro import registro
from ud0_5.exportar_json import exportarJSON
from ud0_5.lectura_json import lecturaJSON

menu_ficheros = [
    (1, "Contador de líneas", contador),
    (2, "Registro de usuarios en archivo", registro),
    (3, "Exportación a JSON", exportarJSON),
    (4, "Lectura de JSON", lecturaJSON)
]

def main():
    utilBran.ejecutar_menu(menu_ficheros)

if __name__ == "__main__":
    main()