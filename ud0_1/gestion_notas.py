def gestion_notas():
    continuar = ""
    alumnos, notas = [], []
    media, posMax, posMin = 0, 0, 0
    while continuar != "fin":
        continuar = input("Introduce nombre de alumno (escribe fin para salir): ")
        if continuar.lower() != "fin":
            alumnos.append(continuar.capitalize())
            notas.append(int(input("Introduce la nota: ")))
    if notas:
        for i in range(len(notas)):
            if notas[i] > notas[posMax]:
                posMax = i
            if notas[i] < notas[posMin]:
                posMin = i
            media += notas[i]
        media /= len(notas)
        print(f"Nota media: {media}")
        print(f"Nota mas alta y alumno: {notas[posMax]} --> {alumnos[posMax]}")
        print(f"Nota mas baja y alumno: {notas[posMin]} --> {alumnos[posMin]}")
    else:
        print("No hay notas para procesar")