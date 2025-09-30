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