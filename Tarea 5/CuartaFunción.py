def original(): #Intercalar letras de dos palabras del mismo tamaño.
    string1 = str(input("Ingrese la primera palabra: "))
    string2 = str(input("Ingrese la segunda palabra: "))

    if len(string1) == len(string2):
        intercalado = "".join(i + j for i, j in zip(string1, string2))
        print(str(intercalado))
    else:
        print("Ingrese palabras con el mismo número de letras.")

def funcional():
    string1 = str(input("Ingrese la primera palabra: "))
    string2 = str(input("Ingrese la segunda palabra: "))

    intercalado = lambda s1, s2: "".join(map(lambda x, y: x + y, s1, s2)) if len(s1) == len(s2) else "Ingrese palabras con el mismo número de letras."
    print(intercalado(string1, string2))
#La función lambda intercarlado toma s1 y s2 las cuales son las palabras ingresadas.
#Map y lambda realizan la iteración al mismo tiempo de s1 y s2 y se intercalan si tienen la misma extensión.
#Join une las letras que fueron intercaladas en una sola palabra.
print("Llamado de prueba (función original):")
original()

print("\nLlamado de prueba (función reescrita con programación funcional):")
funcional()
