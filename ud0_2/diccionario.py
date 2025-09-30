def diccionario():
    frase = input("Introduce una frase: ")
    print(f"Entrada --> {frase}")
    frecuencias = {}
    for palabra in frase.lower().split():
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    print(f"Salida --> {frecuencias}")