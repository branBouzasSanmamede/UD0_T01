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