def ordenacion_palabras():
    frase = input("Introduce una frase: ")
    print(f"Ordenadas alfabeticamente: {sorted(frase.split())}")
    print(f"Ordenadas por longitud: {sorted(frase.split(), key=len)}")
    print(f"Ordenadas por longitud inversa: {sorted(frase.split(), key=len, reverse=True)}")

if __name__ == "__main__":
    ordenacion_palabras()