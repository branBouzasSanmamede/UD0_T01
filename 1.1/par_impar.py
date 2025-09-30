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

if __name__ == "__main__":
    par_impar()