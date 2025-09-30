class Tarea:
    def __init__(self, titulo, estado):
        self.titulo = titulo
        self.estado = "pendiente" if estado == 0 else "completada"

    def toJSON(self):
        return {"titulo": self.titulo, "estado": self.estado}