lista = [1, 2, 3, 3, 2, 4, 6]
norepetidos = [] #Lista en blaco sobre la que se trabaja los comandos para eliminar los repetidos en lista.
for n in range(len(lista)-1, -1, -1):
    if lista[n] not in norepetidos:
        norepetidos.append(lista[n])
    else:
        lista.remove(lista[n])
print(norepetidos) 
  