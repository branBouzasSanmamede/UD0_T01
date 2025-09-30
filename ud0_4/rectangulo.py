class Rectangulo:
    def __init__(self, alto = 1, ancho = 1):
        self.alto = alto
        self.ancho = ancho

    def calcular_area(self):
        return self.alto * self.ancho
    
    def calcular_perimetro(self):
        return 2 * (self.alto + self.ancho)

def menu_rectangulo():
    alto = int(input("Introduce el alto: "))
    ancho = int(input("Introduce el ancho: "))
    rect = Rectangulo(alto, ancho)
    print(f"Area: {rect.calcular_area()}")
    print(f"Perimetro: {rect.calcular_perimetro()}")