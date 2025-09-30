from functools import reduce
from ud0_3.utilidades import pedir_nums

def functools_reduce():
    nums = pedir_nums()
    print(f"Entrada --> {nums}")
    if nums:
        print(f"Salida --> {reduce(lambda x, y: x * y, nums)}")
    else:
        print("No se ingresaron numeros")