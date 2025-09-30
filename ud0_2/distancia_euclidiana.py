import math

def distanciaEuclidiana():
    print("Introduce las coordenadas del primer punto: ")
    x1 = int(input("X1: "))
    y1 = int(input("Y1: "))
    print("Introduce las coordenadas del segundo punto: ")
    x2 = int(input("X2: "))
    y2 = int(input("Y2: "))
    e = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(f"La distancia euclidiana es: {e}")