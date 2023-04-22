numero=int(input("Ingrese el numero: "))
if numero < 0: #Establecer error en caso de número negativos.
    print("Ingrese valores válidos.")
else:
    factorial = 1
    for i in range(1,numero+1):
        factorial = factorial*i
    print("El factorial es " + str(factorial))
    