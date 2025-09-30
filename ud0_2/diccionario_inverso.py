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