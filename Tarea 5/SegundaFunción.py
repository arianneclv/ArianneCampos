#Imprimir factorial del número dado por el usuario
def original():
    numero = int(input("Ingrese el número: "))

    if numero < 0:
        print("Ingrese valores válidos.")
    else:
        factorial = 1
        for i in range(1, numero + 1):
            factorial = factorial * i
        print("El factorial es " + str(factorial))

def funcional():
    numero = int(input("Ingrese el número: "))

    factorial = lambda n: 1 if n == 0 else n * factorial(n - 1) #Con la función lambda se define una forma recursiva para el cálculo del factorial, si n es igual a 0 retorna el valor de 1 sino aplica n * factorial(n - 1)

    if numero < 0:
        print("Ingrese valores válidos.")
    else:
        resultado = factorial(numero)
        print("El factorial es " + str(resultado))

print("Llamado de prueba (función original):")
original()

print("\nLlamado de prueba (función reescrita con programación funcional):")
funcional()
