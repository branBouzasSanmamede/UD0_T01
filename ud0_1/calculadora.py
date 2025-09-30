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