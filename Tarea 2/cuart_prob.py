import random 
long = int(input("Ingrese la longitud querida de la lista: "))
lista = [random.randint(0, 1000) for n in range(long)]
print(lista)
print(" ")
cubo = [n ** 3 for n in lista]
print(cubo)