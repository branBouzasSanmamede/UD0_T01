def decorador_primo(funcion):
    def envoltura():
        n = int(input("Introduce el numero: "))
        def es_primo(n, divisor=2):
            if (1 < n <= 3) or ((divisor * divisor > n) and (n > 1)):
                return True
            elif (n <= 1) or (n % divisor == 0):
                return False
            return es_primo(n, divisor + 1)
        resultado = es_primo(n)
        return funcion(n, resultado)
    return envoltura

@decorador_primo
def num_primo(n, es_primo):
    if es_primo:
        print(f"El numero {n} es primo")
    else:
        print(f"El numero {n} no es primo")

if __name__ == "__main__":
    num_primo(int(input("Introduce el numero primo: ")))