class Cuenta:
    def __init__(self):
        self.saldo = 0

    def mostrarSaldo(self):
        print(f"Saldo actual: {self.saldo}€")
    
    def ingresar(self, val):
        self.saldo += val
        print(f"Has ingresado {val}€ correctamente")

    def retirar(self, val):
        if val > self.saldo:
            print("Fondos insuficientes")
        else:
            self.saldo -= val
            print(f"Has retirado {val}€ correctamente")

cuenta = Cuenta()

def mostrar_saldo():
    cuenta.mostrarSaldo()

def ingresar():
    cantidad = float(input("Introduce la cantidad: "))
    cuenta.ingresar(cantidad)

def retirar():
    cantidad = float(input("Introduce la cantidad: "))
    cuenta.retirar(cantidad)

menu_cuenta = [
    (1, "Mostrar saldo", mostrar_saldo),
    (2, "Ingresar", ingresar),
    (3, "Retirar", retirar)
]

def menu_cuenta_bancaria():
    from utils import utilBran
    utilBran.ejecutar_menu(menu_cuenta)