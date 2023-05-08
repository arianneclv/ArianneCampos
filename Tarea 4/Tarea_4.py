def contar_caracteres(string):
    letras = 0     
    numeros = 0
    especiales = 0
    
    for caracter in string:    #realiza la idetificación de cada caracter
        if caracter.isalpha():   
            letras += 1
        elif caracter.isdigit():
            numeros += 1
        else:
            especiales += 1
    
    print("Letras =", letras)
    print("Números =", numeros)
    print("Caracteres especiales =", especiales)

contar_caracteres("P@#yn26at^&i5ve")
contar_caracteres("hsaioa4$k*7")
contar_caracteres("queso65#@la")
contar_caracteres("Fang2001^^h")
contar_caracteres("Voldemort#$$k78")

def contar_aparicion(string):
    aparicion = {} #se crea un diccionario 
    
    for caracter in string: #identifica las apariciones de cada letra en el string
        if caracter in aparicion:
            aparicion[caracter] += 1
        else:
            aparicion[caracter] = 1
    
    print(aparicion)

contar_aparicion("papaya")
contar_aparicion("timothee")
contar_aparicion("zendaya")
contar_aparicion("florence")
contar_aparicion("fang")

def eliminar_elemento(lista, elemento): #Se crea comando de eliminar
    lista_sin_elemento = [valor for valor in lista if valor != elemento]
    return lista_sin_elemento #Da la lista con el elemento ya eliminado

lista1 = [20, 30, 40, 20, 5, 100, 5, 20] #Lista creada
elemento1 = 20 #Elemento a eliminar
resultado1 = eliminar_elemento(lista1, elemento1) #Comando de eliminar
print(resultado1) 

lista2 = ["perro", "gato", "sombrero", "gato", "zanahoria"]
elemento2 = "gato"
resultado2 = eliminar_elemento(lista2, elemento2)
print(resultado2) 

lista1 = [50, 70, 60, 80, 30, 90, 10, 20]
elemento1 = 60
resultado1 = eliminar_elemento(lista1, elemento1)
print(resultado1) 

lista2 = ["manzana", "fresa", "pera", "banano", "piña"]
elemento2 = "banano"
resultado2 = eliminar_elemento(lista2, elemento2)
print(resultado2) 

lista1 = ["Harry", "Niall", "Louis", "Zayn", "Liam"]
elemento1 = "Zayn"
resultado1 = eliminar_elemento(lista1, elemento1)
print(resultado1) 

lista2 = ["Costa Rica", "Nicaragua", "Panama", "Guatemala", "Rusia"]
elemento2 = "Rusia"
resultado2 = eliminar_elemento(lista2, elemento2)
print(resultado2) 

lista1 = ["Fang", "Urian", "Luna", "Lolo"]
elemento1 = "Lolo"
resultado1 = eliminar_elemento(lista1, elemento1)
print(resultado1) 

lista2 = ["Dipper", "Mabel", "Tala", "Stan"]
elemento2 = "Tala"
resultado2 = eliminar_elemento(lista2, elemento2)
print(resultado2) 

def convertir_secuencia(input_usuario):
    valores = input_usuario.split(",") #Indica que debe ser separado por una coma.
    lista = [int(valor) for valor in valores]
    tupla = tuple(lista)
    print("Lista:", lista)
    print("Tupla:", tupla)
input_usuario = input("Ingrese una secuencia de números los cuales se encuentren separados por comas: ")
convertir_secuencia(input_usuario)
#Ejemplos a utilizar: 2, 4, 5, 6 ; 7, 9, 10, 23, 53 ; 03, 09, 23, 10 ; 84, 34, 56, 90


