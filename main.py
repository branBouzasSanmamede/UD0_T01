import algoritmia, secuencias, funciones, programacion_objetos, fichero

def menuGeneral():
    print("--------------------------------------------------------")
    print("Salir 0:")
    print("Opcion 1: Algoritmia e interacción con el usuario")
    print("Opcion 2: Secuencias y diccionarios")
    print("Opcion 3: Funciones")
    print("Opcion 4: Programación Orientada a Objetos")
    print("Opcion 5: Lectura y escritura de ficheros (texto y JSON)")
    print("Opcion 6: Conexión con MongoDB")
    print("Opcion 7: Proyecto")
    print("--------------------------------------------------------")
    return int(input("Opcion: "))

if __name__ == "__main__":
    option = 1
    while option != 0:
        option = menuGeneral()
        match option:
            case 1:
                algoritmia.main()
            case 2:
                secuencias.main()
            case 3:
                funciones.main()
            case 4:
                programacion_objetos.main()
            case 5:
                fichero.main()
            case other:
                if option != 0:
                    print("Opcion invalida")
    print("Hasta luego!")