from utils import utilBran
from ud0_4.rectangulo import menu_rectangulo
from ud0_4.cuenta_bancaria import menu_cuenta_bancaria
from ud0_4.empleado import menu_empleado
from ud0_4.libro import menu_biblioteca

menu_objetos = [
    (1, "Clase Rectángulo", menu_rectangulo),
    (2, "Clase Cuenta Bancaria", menu_cuenta_bancaria),
    (3, "Jerarquía de Empleados", menu_empleado),
    (4, "Sistema de biblioteca (clases + composición)", menu_biblioteca)
]

def main():
    utilBran.ejecutar_menu(menu_objetos)

if __name__ == "__main__":
    main()