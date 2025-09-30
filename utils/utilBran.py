def mostrar_menu(opciones):
    lineas = []
    max_len = 0 
    opt_salir = f"Opcion 0: Salir"
    for num, desc, _ in opciones:
        linea = f"Opcion {num}: {desc}"
        lineas.append(linea)
        if len(linea) > max_len:
            max_len = len(linea)
    
    if len(opt_salir) > max_len:
        max_len = len(opt_salir)

    separador = "-" * max_len

    print(separador)
    print(opt_salir)
    for l in lineas:
        print(l)
    print(separador)

    return int(input("Opcion: "))

def ejecutar_menu(opciones):
    opt = mostrar_menu(opciones)
    while opt != 0:
        for num, _, func in opciones:
            if opt == num:
                func()
                break
        else:
            print("Opcion invalida!")
        
        opt = mostrar_menu(opciones)
    print("Hasta luego!")