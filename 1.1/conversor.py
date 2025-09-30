def conversor_temperaturas():
    t = int(input("Introduce la temperatura en Celsius: "))
    print("Grados Fahrenheit: ", t*1.8 + 32, "\nGrados Kelvin: ", t+273.15)

if __name__ == "__main__":
    conversor_temperaturas()