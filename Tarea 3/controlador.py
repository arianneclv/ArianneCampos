from mate import *

def registrar_operacion(operacion, numeros, resultado): #Operación para registrar las operaciones realizadas
    registro = operacion + ": " + " ".join(map(str, numeros)) + " = " + str(resultado)
    with open("registro_operaciones.txt", "a") as archivo:
        archivo.write(registro + "\n")

def menu(): #Menú el cudal visualiza el usuario
    print("Tarea Calculadora")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Factorial")
    print("6. Potencia")
    print("7. Salir")

while True:
    menu()
    opcion = int(input("Seleccione una opción: "))
    import mate
    if opcion == 1:
        mate.suma()
    elif opcion == 2:
        mate.resta()
    elif opcion == 3:
        mate.multiplicacion()
    elif opcion == 4:
        mate.division()
    elif opcion == 5:
        mate.factorial()
    elif opcion == 6:
        mate.potencia()
    elif opcion == 7:
        print("Gracias por usar la aplicación.")
        break
    else: #Otro número fuera de los indicados debe mostrar al usuario un error.
        print("Por favor seleccione una opción válida.")