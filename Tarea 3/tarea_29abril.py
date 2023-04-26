class Numeros:
  
  def suma(self): #Necesito que esto se logre con N números 
     numero1=int(input("Ingrese el primer número: "))
     numero2=int(input("Ingrese el segundo número: "))
     resultado = numero1 + numero2
     print("El resultado de la suma es igual a " + str(resultado))
      
  def resta(self):
     numero1=int(input("Ingrese el primer número: "))
     numero2=int(input("Ingrese el segundo número: "))
     resultado = numero1 - numero2
     print("El resultado de la resta es igual a " + str(resultado))
  
  def division(self):
     numero1=int(input("Ingrese el primer número: "))
     numero2=int(input("Ingrese el segundo número: "))
     resultado = numero1//numero2
     print("El resultado de la división es igual a " + str(resultado))

  def multiplicacion(self):
     numero1=int(input("Ingrese el primer número: "))
     numero2=int(input("Ingrese el segundo número: "))
     resultado = numero1*numero2
     print("El resultado de la multiplicación es igual a " + str(resultado))   

  def factorial(self):
    try:
        numero=int(input("Ingrese el numero: "))
        if numero < 0:
          print("El factorial es " + str(numero))
        else:
          factorial = 1
          for i in range(1,numero+1):
            factorial = factorial*i
          print("El factorial es " + str(factorial))
    except:
      print("Ingrese valores válidos.")


  def controlador(self):
    salir = False
    while (salir == False):
      seleccion = input("Seleccione una opción del menú:\n1. Suma\n2. Resta\n3. Factorial de un número\n4. Salir\nOpción: ")
      if (seleccion == "1"):
        self.suma()
      elif (seleccion == "2"):
        self.resta()
      elif (seleccion == "3"):
        self.factorial()
      elif (seleccion == "4"):
        salir = True
      else:
        print("Por favor seleccione una opción válida.")
    print("Gracias por usar el programa.")

miInstancia = Numeros()
miInstancia.controlador()