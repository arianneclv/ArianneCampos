numero=int(input("Ingrese el numero: "))
if numero < 0:
    print("Ingrese valores mayores a 0.")
else:
    for n1 in range (1, numero+1): #Creación de primer bucle
        print ("") #Salto de línea para que los bucles se observen en líneas separadas
        for n2 in range (1, n1+1): #Creación de segundo bucle
            print(n2, end=" ") #end para indicar cuando termina a línea
