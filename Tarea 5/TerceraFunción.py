def original(): #Desplegar patrón triangulo hasta el número ingresado por el usuario.
    numero = int(input("Ingrese el número: "))

    if numero < 0:
        print("Ingrese valores mayores a 0.")
    else:
        for n1 in range(1, numero + 1):
            print("")
            for n2 in range(1, n1 + 1):
                print(n2, end=" ")

def funcional():
    numero = int(input("Ingrese el número: "))

    if numero < 0:
        print("Ingrese valores mayores a 0.")
    else:
        triangulo = lambda n: "\n".join([" ".join(map(str, range(1, i + 1))) for i in range(1, n + 1)])
        print(triangulo(numero))
#Lambda permite agarrar el número ingresado, utiliza map y range para generar fila por fila que contenga del valor 1 al un valor i hasta llegar al valor n ingresado.
#Join permite juntar todas las filas generadas anteriormente en una sola cadena que es imprimida.
print("Llamado de prueba (función original):")
original()

print("\nLlamado de prueba (función reescrita con programación funcional):")
funcional()

