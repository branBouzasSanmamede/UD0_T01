import json

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