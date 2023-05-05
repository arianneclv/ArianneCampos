def contar_caracteres(string):
    letras = 0
    numeros = 0
    especiales = 0
    
    for caracter in string:
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

def contar_apariciones(string):
    apariciones = {}
    
    for caracter in string:
        if caracter in apariciones:
            apariciones[caracter] += 1
        else:
            apariciones[caracter] = 1
    
    print(apariciones)

contar_apariciones("papaya")
contar_apariciones("timothee")
contar_apariciones("zendaya")
contar_apariciones("florence")
contar_apariciones("fang")

def eliminar_elemento(lista, elemento):
    lista_sin_elemento = [valor for valor in lista if valor != elemento]
    return lista_sin_elemento

lista1 = [20, 30, 40, 20, 5, 100, 5, 20]
elemento1 = 20
resultado1 = eliminar_elemento(lista1, elemento1)
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

def convertir_secuencia(input_usuario):
    valores = input_usuario.split(",")
    lista = [int(valor) for valor in valores]
    tupla = tuple(lista)
    print("Lista:", lista)
    print("Tupla:", tupla)
input_usuario = input("Ingrese una secuencia de números los cuales se encuentren separados por comas: ")
convertir_secuencia(input_usuario)
#Ejemplos a utilizar: 2, 4, 5, 6 ; 7, 9, 10, 23, 53 ; 03, 09, 23, 10 ; 84, 34, 56, 90


