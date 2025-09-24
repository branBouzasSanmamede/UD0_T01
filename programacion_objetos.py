import rectangulo, cuenta_bancaria, empleado, libro

def menuObjetos():
    print("------------------------------------------------------")
    print("Salir 0:")
    print("Opcion 1: Clase Rectángulo")
    print("Opcion 2: Clase Cuenta Bancaria")
    print("Opcion 3: Jerarquía de Empleados")
    print("Opcion 4: Sistema de biblioteca (clases + composición)")
    print("------------------------------------------------------")
    return int(input("Opcion: "))

def menuCuenta():
    print("-----------------------")  
    print("Salir: 0")  
    print("Opcion 1: Mostrar saldo")  
    print("Opcion 2: Ingresar")  
    print("Opcion 3: Retirar")  
    print("-----------------------") 
    return int(input("Opcion: "))

def menuLibro():
    print("-----------------------")  
    print("Salir: 0")  
    print("Opcion 1: Listar")  
    print("Opcion 2: Añadir")  
    print("Opcion 3: Buscar")  
    print("-----------------------") 
    return int(input("Opcion: "))

def main():
    option = 1
    while option != 0:
        option = menuObjetos()
        match option:
            case 1:
                alto = int(input("Introduce el alto: "))
                ancho = int(input("Introduce el ancho: "))
                rect = rectangulo.Rectangulo(alto, ancho)
                print(f"Area: {rect.calcular_area()}")
                print(f"Perimetro: {rect.calcular_perimetro()}")
            case 2:
                cuenta = cuenta_bancaria.Cuenta()
                opcionCuenta = menuCuenta()
                while opcionCuenta != 0:
                    if opcionCuenta == 1:
                        cuenta.mostrarSaldo()
                    elif opcionCuenta == 2:
                        cantidad = float(input("Introduce la cantidad: "))
                        cuenta.ingresar(cantidad)
                    elif opcionCuenta == 3:
                        cantidad = float(input("Introduce la cantidad: "))
                        cuenta.retirar(cantidad)
                    else:
                        print("Opcion invalida")
                    opcionCuenta = menuCuenta()
            case 3:
                e1 = empleado.Empleado("Pepito", 2000)
                e2 = empleado.Gerente("Pepe", 1500, "Marketing")
                e3 = empleado.Programador("Manolo", 3000, "Python")
                print(e1)
                print(e2)
                print(e3)
            case 4:
                l1 = libro.Libro("Don Quijote", "Cervantes")
                l2 = libro.Libro("El señor de los anillos", "J.R.R. Tolkien")
                l3 = libro.Libro("Harry Potter y la piedra filosofal", "J.K. Rowling")
                l4 = libro.Libro("La Odisea", "Homero")
                l5 = libro.Libro("Drácula", "Bram Stoker")
                biblioteca = libro.Biblioteca([l1, l2, l3, l4, l5])
                opcionLibro = menuLibro()
                while opcionLibro != 0:
                    if opcionLibro == 1:
                        biblioteca.listar_libros()
                    elif opcionLibro == 2:
                        titulo = input("Introduce el titulo: ")
                        autor = input("Introduce el autor: ")
                        l = libro.Libro(titulo, autor)
                        biblioteca.agregar_libro(l)
                    elif opcionLibro == 3:
                        titulo = input("Introduce el titulo: ")
                        biblioteca.buscar_libro(titulo)
                    else:
                        print("Opcion invalida")
                    opcionLibro = menuLibro()
            case other:
                if option != 0:
                    print("Opcion invalida")
    print("Hasta luego!")

if __name__ == "__main__":
    main()