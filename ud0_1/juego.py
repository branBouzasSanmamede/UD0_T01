import random

def juego_adivinanza():
    n = random.randint(1, 100)
    num, intentos = 0, 0
    while n != num:
        intentos += 1
        num = int(input("Introduce un numero entre 1 y 100: "))
        if num > n:
            print(f"El numero {num} es mayor al generado...")
        elif num < n:
            print(f"El numero {num} es menor al generado...")
    print(f"¡ACERTASTE! El numero era {n}, te llevo {intentos} intentos")