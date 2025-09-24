class Rectangulo:
    def __init__(self, alto = 1, ancho = 1):
        self.alto = alto
        self.ancho = ancho

    def calcular_area(self):
        return self.alto * self.ancho
    
    def calcular_perimetro(self):
        return 2 * (self.alto + self.ancho)