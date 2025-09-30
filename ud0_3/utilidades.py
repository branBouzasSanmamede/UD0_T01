def saludar():
    nombre = input("Introduce el nombre: ")
    print(f"Hola, {nombre}")

def pedir_nums(parada = "x"):
    nums = []
    while True:
        entrada = input(f"Introduce un numero ('{parada}' para parar): ")
        if entrada == parada:
            break
        try:
            n = int(entrada)
            nums.append(n)
        except ValueError:
            print("Entrada no valida")
    return nums