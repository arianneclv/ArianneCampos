import random 
long = int(input("Ingrese la longitud querida de la lista: "))
lista = [random.randint(0, 1000) for n in range(long)] #El rango puede ser mayor pero los cubos ya son números exagerados sin utilidad para el usuario.
print(lista)
print(" ")
cubo = [n ** 3 for n in lista]
print(cubo)