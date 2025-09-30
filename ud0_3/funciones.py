from utils import utilBran
from ud0_3.funciones_simples import funciones_simples
from ud0_3.funcion_retorno import funcion_retorno
from ud0_3.functools_reduce import functools_reduce
from ud0_3.utilidades import saludar

menu_funciones = [
    (1, "Funciones simples", funciones_simples),
    (2, "Funciones con retorno múltiple", funcion_retorno),
    (3, "Uso de functools.reduce", functools_reduce),
    (4, "Módulos propios", saludar)
]

def main():
    utilBran.ejecutar_menu(menu_funciones)

if __name__ == "__main__":
    main()