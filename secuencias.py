import menu, math

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

def distanciaEuclidiana():
    print("Introduce las coordenadas del primer punto: ")
    x1 = float(input("X1: "))
    y1 = int(input("Y1: "))
    print("Introduce las coordenadas del segundo punto: ")
    x2 = float(input("X2: "))
    y2 = int(input("Y2: "))
    e = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(f"La distancia euclidiana es: {e}")

def diccionarioInverso():
    d1 = {
        "marca": "Mazda",
        "modelo": "MX-5",
        "cc": 2000, 
        "cilindros": 4,
        "potencia": 190,
        "puertas": 2
    }
    print(f"Diccionario original: {d1}")
    d2 = {}
    for clave, valor in d1.items():
        d2[valor] = clave
    print(f"Diccionario nuevo: {d2}")

def nuevoContacto():
    nombre = input("Introduce el nombre: ")
    tel = int(input("Introduce el telefono: "))
    return nombre, tel

def buscarContacto(contactos):
    nombre = input("Introduce el nombre: ")
    if nombre in contactos:
        print(f"{nombre} --> {contactos[nombre]}")
    else:
        print("Contacto no encontrado!")

def verContactos(contactos):
    if contactos:
        for contacto, tel in contactos.items():
            print(f"{contacto} --> {tel}")
    else:
        print("Aun no hay contactos")

def listaDiccionarios():
    contactos = {}
    option = 1
    while option != 0:
        option = menu.menuContactos()
        match option:
            case 1:
                nombre, tel = nuevoContacto()
                contactos[nombre] = tel
                print(f"Contacto añadido: {nombre} --> {tel}")
            case 2:
                buscarContacto(contactos)
            case 3:
                verContactos(contactos)
            case other:
                if option != 0:
                    print("Opcion invalida")
    print("Agenda cerrada!")

if __name__ == "__main__":
    option = 1
    while option != 0:
        option = menu.menuSecuencias()
        match option:
            case 1:
                diccionario()
            case 2:
                distanciaEuclidiana()
            case 3:
                diccionarioInverso()
            case 4:
                listaDiccionarios()
            case other:
                if option != 0:
                    print("Opcion invalida")
    print("Hasta luego!")