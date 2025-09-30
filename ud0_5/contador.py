def contador():
    with open("contador.txt", "r") as file:
        lineas = file.readlines()
        palabras, caracteres = 0, 0
        for linea in lineas:
            palabras += len(linea.split())
            caracteres += len(linea.replace(" ", "").replace("\n", "").replace("\t", ""))
        print(f"Numero de lineas: {len(lineas)}")
        print(f"Numero de palabras: {palabras}")
        print(f"Numero de caracteres: {caracteres}")