numero=int(input("Ingrese el numero: "))
if numero < 0:
    print("Ingrese valores válidos.")
else:
    Factorial = 1
    for i in range(1,numero+1):
        Factorial = Factorial*i
    print("El factorial es " + str(Factorial))