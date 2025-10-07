class Alumno():
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota

    def to_dict(self):
        return {"nombre": self.nombre, "edad": self.edad, "nota": self.nota}
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Nota: {self.nota}"