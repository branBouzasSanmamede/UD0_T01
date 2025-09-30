from utils import utilBran

def agenda():
    contactos = {}

    def nuevoContacto():
        nombre = input("Introduce el nombre: ")
        tel = int(input("Introduce el telefono: "))
        contactos[nombre] = tel
        print(f"Contacto añadido: {nombre} --> {tel}")

    def buscarContacto():
        nombre = input("Introduce el nombre: ")
        if nombre in contactos:
            print(f"{nombre} --> {contactos[nombre]}")
        else:
            print("Contacto no encontrado!")

    def verContactos(contactos):
        if contactos:
            for contacto, tel in contactos.items():
                print(f"{contacto} --> {tel}")
        else:
            print("Aun no hay contactos")

    menu_contactos = [
    (1, "Añadir contacto", nuevoContacto),
    (2, "Buscar contacto", buscarContacto),
    (3, "Ver contactos", verContactos)
    ]

    utilBran.ejecutar_menu(menu_contactos)