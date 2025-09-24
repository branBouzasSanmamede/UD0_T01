class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"- Titulo: {self.titulo}, Autor: {self.autor}"

class Biblioteca:
    def __init__(self, libros):
        self.libros = libros

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro añadido: {libro}")

    def buscar_libro(self, titulo):
        if self.libros:
            for libro in self.libros:
                if libro.titulo.lower() == titulo.lower():
                    print(libro)
                    return
            print(f"Libro no encontrado")
        else:
            print("No hay libros")
    
    def listar_libros(self):
        if self.libros:
            for libro in self.libros:
                print(libro)
        else:
            print("No hay libros")