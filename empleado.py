class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def __str__(self):
        return f"Empleado: {self.nombre}, Sueldo: {self.sueldo}€"

class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.departamento = departamento

    def __str__(self):
        return f"Gerente --> Departamento: {self.departamento}, {super().__str__()}"

class Programador(Empleado):
    def __init__(self, nombre, sueldo, lenguaje):
        super().__init__(nombre, sueldo)
        self.lenguaje = lenguaje

    def __str__(self):
        return f"Programador --> Lenguaje: {self.lenguaje}, {super().__str__()}"