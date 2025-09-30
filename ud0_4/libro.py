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

l1 = Libro("Don Quijote", "Cervantes")
l2 = Libro("El señor de los anillos", "J.R.R. Tolkien")
l3 = Libro("Harry Potter y la piedra filosofal", "J.K. Rowling")
l4 = Libro("La Odisea", "Homero")
l5 = Libro("Drácula", "Bram Stoker")
biblioteca = Biblioteca([l1, l2, l3, l4, l5])

def listar():
    biblioteca.listar_libros()

def agregar():
    titulo = input("Introduce el titulo: ")
    autor = input("Introduce el autor: ")
    l = Libro(titulo, autor)
    biblioteca.agregar_libro(l)

def buscar():
    titulo = input("Introduce el titulo: ")
    biblioteca.buscar_libro(titulo)

menu_libro = [
    (1, "Listar", listar),
    (2, "Añadir", agregar),
    (3, "Buscar", buscar)
]

def menu_biblioteca():
    from utils import utilBran
    utilBran.ejecutar_menu(menu_libro)