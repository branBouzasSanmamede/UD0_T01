import usuario, tarea, json

def menuFicheros():
    print("-----------------------------------------")
    print("Salir 0:")
    print("Opcion 1: Contador de líneas")
    print("Opcion 2: Registro de usuarios en archivo")
    print("Opcion 3: Exportación a JSON")
    print("Opcion 4: Lectura de JSON")
    print("-----------------------------------------")
    return int(input("Opcion: "))

def continuar_input():
    return bool(int(input("¿Continuar? (0-No, Otro numero-Si)")))

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

def registro():
    usuarios = []
    continuar = True
    while continuar:
        nombre = input("Introduce nombre: ")
        correo = input("Introduce correo: ")
        usuarios.append(usuario.Usuario(nombre, correo))
        continuar = continuar_input()

    with open("registro.txt", "a") as file:
        for u in usuarios:
            file.write(str(u) + "\n")

def exportarJSON():
    try:
        with open("tareas.json", "r") as file:
            tareasJSON = json.load(file)
    except (json.JSONDecodeError):
        tareasJSON = []

    tareas = []
    continuar = True
    while continuar:
        titulo = input("Introduce titulo: ")
        estado = int(input("Introduce estado (0-pendiente, 1-completado): "))
        while estado not in [0,1]:
            print("Estado invalido!")
            estado = int(input("Introduce estado (0-pendiente, 1-completado): "))
        tareas.append(tarea.Tarea(titulo, estado))
        continuar = continuar_input()
    tareasJSON.extend([t.toJSON() for t in tareas])

    with open("tareas.json", "w") as file:
        json.dump(tareasJSON, file, indent=2)

def lecturaJSON():
    try:
        with open("tareas.json", "r") as file:
            tareasJSON = json.load(file)
    except (json.JSONDecodeError):
        tareasJSON = []

    tareas_pendientes = [t for t in tareasJSON if t.get("estado") == "pendiente"]
    if tareas_pendientes:
        for tarea in tareas_pendientes:
            print(tarea)
    else:
        print("No hay tareas pendientes")

def main():
    option = menuFicheros()
    while option != 0:
        match option:
            case 1:
                contador()
            case 2:
                registro()
            case 3:
                exportarJSON()
            case 4:
                lecturaJSON()
            case other:
                if option != 0:
                    print("Opcion invalida")
        option = menuFicheros()
    print("Hasta luego!")

if __name__ == "__main__":
    main()