import random

def conversor_temperaturas():
    t = int(input("Introduce la temperatura en Celsius: "))
    print("Grados Fahrenheit: ", t*1.8 + 32, "\nGrados Kelvin: ", t+273.15)

def par_impar():
    numeros = list(map(int, input("Introduce los numeros separados por espacios: ").split()))
    pares, impares = [], []
    for n in numeros:
        if n%2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    print("Numeros pares: ", pares)
    print("Numeros impares: ", impares)

def frecuencia_caracteres():
    cadena = input("Introduce la cadena: ")
    diccionario = {}
    for c in cadena:
        if c != " ":
            if c in diccionario:
                diccionario[c] += 1
            else:
                diccionario[c] = 1

    for c in sorted(diccionario.keys()):
        if diccionario[c] != 1:
            print(f"{c}: {diccionario[c]} veces")
        else:
            print(f"{c}: {diccionario[c]} vez")

def calculadora():
    n1, n2 = int(input("Introduce el primer numero: ")), int(input("Introduce el segundo numero: "))
    operacion = input("Introduce la operacion (+,-,*,/): ")
    if operacion == "+":
        print(f"La suma es: {n1 + n2}")
    elif operacion == "-":
        print(f"La resta es: {n1 - n2}")
    elif operacion == "*":
        print(f"La multiplicacion es: {n1 * n2}")
    elif operacion == "/":
        if n2 != 0:
            print(f"La division es: {n1 / n2}")
        else:
            print("Division por 0")

def ordenacion_palabras():
    frase = input("Introduce una frase: ")
    print(f"Ordenadas alfabeticamente: {sorted(frase.split())}")
    print(f"Ordenadas por longitud: {sorted(frase.split(), key=len)}")
    print(f"Ordenadas por longitud inversa: {sorted(frase.split(), key=len, reverse=True)}")

def decorador_primo(funcion):
    def envoltura(n):
        def es_primo(n, divisor=2):
            if (1 < n <= 3) or ((divisor * divisor > n) and (n > 1)):
                return True
            elif (n <= 1) or (n % divisor == 0):
                return False
            return es_primo(n, divisor + 1)
        resultado = es_primo(n)
        return funcion(n, resultado)
    return envoltura

@decorador_primo
def num_primo(n, es_primo):
    if es_primo:
        print(f"El numero {n} es primo")
    else:
        print(f"El numero {n} no es primo")

def gestion_notas():
    continuar = ""
    alumnos, notas = [], []
    media, posMax, posMin = 0, 0, 0
    while continuar != "fin":
        continuar = input("Introduce nombre de alumno (escribe fin para salir): ").lower()
        if continuar != "fin":
            alumnos.append(continuar.capitalize())
            notas.append(int(input("Introduce la nota: ")))
    for i in range(len(notas)):
        if notas[i] > notas[posMax]:
            posMax = i
        if notas[i] < notas[posMin]:
            posMin = i
        media += notas[i]
    media /= len(notas)
    print(f"Nota media: {media}")
    print(f"Nota mas alta y alumno: {notas[posMax]} --> {alumnos[posMax]}")
    print(f"Nota mas baja y alumno: {notas[posMin]} --> {alumnos[posMin]}")

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
    print(f"¡ACERSTASTE! El numero era {n}, te llevo {intentos} intentos")

if __name__ == "__main__":
    print("---------------------------------")
    print("Salir 0:")
    print("Opcion 1: Conversor temperaturas")
    print("Opcion 2: Numeros pares/impares")
    print("Opcion 3: Frecuencia de caracteres")
    print("Opcion 4: Calculadora básica")
    print("Opcion 5: Ordenación de palabras")
    print("Opcion 6: Números primos en un rango")
    print("Opcion 7: Gestión de notas")
    print("Opcion 8: Juego de adivinanza")
    print("---------------------------------")
    option = 1
    while option != 0:
        option = int(input("Opcion: "))
        match option:
            case 1:
                conversor_temperaturas()
            case 2:
                par_impar()
            case 3:
                frecuencia_caracteres()
            case 4:
                calculadora()
            case 5:
                ordenacion_palabras()
            case 6:
                num_primo(int(input("Introduce el numero primo: ")))
            case 7:
                gestion_notas()
            case 8:
                juego_adivinanza()
            case other:
                if option != 0:
                    print("Opcion invalida")
    print("Hasta luego!")