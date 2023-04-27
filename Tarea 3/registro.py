def registrar_operacion(operacion, numeros, resultado): #Operación para registrar las operaciones realizadas
    registro = operacion + ": " + " ".join(map(str, numeros)) + " = " + str(resultado)
    with open("registro_operaciones.txt", "a") as archivo:
        archivo.write(registro + "\n")
