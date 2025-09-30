from ud0_3.utilidades import pedir_nums

def min_max_media(nums):
    if len(nums) > 0:
        return min(nums), max(nums), (sum(nums) / len(nums))
    else:
        print("No existen numeros")
        return None

def funcion_retorno():
    nums = pedir_nums()
    print(f"Entrada --> {nums}")
    resultado = min_max_media(nums)
    if resultado:
        print(f"Salida --> {resultado}")