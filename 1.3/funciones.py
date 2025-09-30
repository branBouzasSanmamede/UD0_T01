from functools import reduce
import utilidades

def menuFunciones():
    print("----------------------------------------")
    print("Salir 0:")
    print("Opcion 1: Funciones simples")
    print("Opcion 2: Funciones con retorno múltiple")
    print("Opcion 3: Uso de functools.reduce")
    print("Opcion 4: Módulos propios")
    print("----------------------------------------")
    return int(input("Opcion: "))

def es_par(n):
    return n % 2 == 0

def min_max_media(nums):
    if len(nums) > 0:
        return min(nums), max(nums), (sum(nums) / len(nums))
    else:
        print("No existen numeros")
        return None

def pedir_nums(parada = "x"):
    nums = []
    while True:
        entrada = input(f"Introduce un numero ('{parada}' para parar): ")
        if entrada == parada:
            break
        try:
            n = int(entrada)
            nums.append(n)
        except ValueError:
            print("Entrada no valida")
    return nums

def funciones_simples():
    n = int(input("Introduce el numero: "))
    print(f"Entrada --> {n}")
    print(f"Salida --> {es_par(n)}")

def funcion_retorno():
    nums = pedir_nums()
    print(f"Entrada --> {nums}")
    resultado = min_max_media(nums)
    if resultado:
        print(f"Salida --> {resultado}")

def functools_reduce():
    nums = pedir_nums()
    print(f"Entrada --> {nums}")
    if nums:
        print(f"Salida --> {reduce(lambda x, y: x * y, nums)}")
    else:
        print("No se ingresaron numeros")

def main():
    option = 1
    while option != 0:
        option = menuFunciones()
        match option:
            case 1:
                funciones_simples()
            case 2:
                funcion_retorno()
            case 3:
                functools_reduce()
            case 4:
                utilidades.saludar("Ana")
            case other:
                if option != 0:
                    print("Opcion invalida")
    print("Hasta luego!")

if __name__ == "__main__":
    main()