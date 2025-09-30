import ud0_5.usuario as usuario
from ud0_5.continuar import continuar_input

def registro():
    usuarios = []
    continuar = True
    while continuar:
        nombre = input("Introduce nombre: ")
        correo = input("Introduce correo: ")
        usuarios.append(usuario.Usuario(nombre, correo))
        continuar = continuar_input()

    with open("registro.txt", "a") as file:
        for u in usuarios:
            file.write(str(u) + "\n")