import random

def original():
    long = int(input("Ingrese la longitud deseada de la lista: "))
    lista = [random.randint(0, 1000) for _ in range(long)]
    print(lista)
    print(" ")

    cubo = [n ** 3 for n in lista]
    print(cubo)
#Reescrtio El programa genera una lista aleatoria según la longitud establecida por el usuario e imprime esta como el cubo de la misma.
def funcional():
    long = int(input("Ingrese la longitud deseada de la lista: "))
    lista = list(map(lambda _: random.randint(0, 1000), range(long)))
    print(lista)
    print(" ")

    cubo = list(map(lambda n: n ** 3, lista)) #map permite aplicar el lamda a cada elemento de la lista, el lambda permite el calular cada cubo de la lista por medio de la expresión lambda n: n ** 3, lista 
    print(cubo)

print("Llamado de prueba (función original):")
original()

print("\nLlamado de prueba (función reescrita con programación funcional):")
funcional()
