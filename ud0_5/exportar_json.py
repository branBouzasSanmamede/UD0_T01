import json, ud0_5.tarea as tarea
from ud0_5.continuar import continuar_input

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