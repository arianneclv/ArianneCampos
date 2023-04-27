import math #Primeramente realicé el código puesto que se me dificulta el uso de módulos por lo cual primero lo visualizo completamente.
#Programa permite el ingreso de decimales.
def suma(): #Operación suma, debido a que necesita N números se utiliza listas y se pregunta al usuario cuantos números quiere sumar.
    n = int(input("Ingrese la cantidad de números a sumar: ")) #
    numeros = [float(input(f"Ingrese el número {i+1}: ")) for i in range(n)] #Uso de listas debido a que debe permitir la suma de N números.
    resultado = sum(numeros)
    print("El resultado de la suma es:", resultado)
    import registro
    registro.registrar_operacion("Suma", numeros, resultado) #Registra la operación con def registrar_operaciones

def resta():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 - num2
    print("El resultado de la resta es:", resultado)
    import registro #Llama al módulo de registro.
    registro.registrar_operacion("Resta", [num1, num2], resultado)

def multiplicacion(): #Operación multiplicación, debido a que necesita N números se utiliza listas y se pregunta al usuario cuantos números quiere multiplicar.
    n = int(input("Ingrese la cantidad de números a multiplicar: "))
    numeros = [float(input(f"Ingrese el número {i+1}: ")) for i in range(n)] #Uso de lista
    resultado = 1
    for num in numeros:
        resultado *= num
    print("El resultado de la multiplicación es:", resultado)
    import registro
    registro.registrar_operacion("Multiplicación", numeros, resultado) #Registra la operación con def registrar_operaciones

def division():
    num1 = float(input("Ingrese el numerador: "))
    num2 = float(input("Ingrese el denominador: "))
    if num2 == 0: #Indicar al usuario que las divisiones entre cero son errores
        print("Error: No se puede dividir entre cero.")
        registrar_operacion("División", [num1, num2], "Error: División entre cero") #Registra la operación con def registrar_operaciones
    else:
        resultado = num1 / num2
        print("El resultado de la división es:", resultado)
        import registro
        registro.registrar_operacion("División", [num1, num2], resultado) #Registra la operación con def registrar_operaciones

def factorial():
    num = int(input("Ingrese un número: "))
    resultado = math.factorial(num)
    print("El factorial de", num, "es:", resultado)
    import registro
    registro.registrar_operacion("Factorial", [num], resultado) #Registra la operación con def registrar_operaciones

def potencia():
    base = float(input("Ingrese la base: "))
    exponente = float(input("Ingrese el exponente: "))
    resultado = base ** exponente
    print("El resultado de la potencia es:", resultado)
    import registro
    registro.registrar_operacion("Potencia", [base, exponente], resultado) #Registra la operación con def registrar_operaciones