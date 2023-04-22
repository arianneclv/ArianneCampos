string1 = str(input("Ingrese la primera palabra: "))
string2 = str(input("Ingrese la segunda palabra: "))
if len(string1) == len (string2): #establecer que solo aquellos strings del mismo tamaño puede ser intercalados
    intercalado = "".join(i + j for i, j in zip(string1, string2)) #unir ambos strings y dar la orden de intercarlar
    print(str(intercalado))
else:
    print("Ingrese palabras con el mismo número de letras.")
    