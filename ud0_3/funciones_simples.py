def es_par(n):
    return n % 2 == 0

def funciones_simples():
    n = int(input("Introduce el numero: "))
    print(f"Entrada --> {n}")
    print(f"Salida --> {es_par(n)}")