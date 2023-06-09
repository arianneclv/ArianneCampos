import random


class Carta:
    def __init__(self, palo, valor): #establecer clase carta
        self.palo = palo
        self.valor = valor

    def __str__(self):  
        return f"{self.valor} de {self.palo}" #devolver valor


class Baraja:    #establecer clase baraja
    palos = ["♠", "♦", "♥", "♣"]    #sīmbolos de cartas
    valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] #valores de las cartas

    def __init__(self):
        self.cartas = []
        self.crear_baraja()

    def crear_baraja(self):   #acción de crear la baraja para el usuario
        for palo in self.palos:
            for valor in self.valores:
                carta = Carta(palo, valor)
                self.cartas.append(carta)

    def mezclar(self):    #mezclar la baraja
        random.shuffle(self.cartas)   #random permite esta acción aleactoriamente

    def sacar_carta(self):    
        return self.cartas.pop()  #devolcer una carta especifica para el juego


class Mano:       #establecer la mano del jugador por medio de diferentes acciones
    def __init__(self):
        self.cartas = []

    def agregar_carta(self, carta):
        self.cartas.append(carta)   #se utiliza append para agregar una sola cosa a la lista

    def obtener_valor(self):
        valor = 0
        num_ases = 0
        for carta in self.cartas:
            if carta.valor == "A":
                valor += 11
                num_ases += 1
            elif carta.valor in ["K", "Q", "J"]:
                valor += 10
            else:
                valor += int(carta.valor)

        while valor > 21 and num_ases > 0:
            valor -= 10
            num_ases -= 1

        return valor

    def __str__(self):
        mano_str = ""
        for carta in self.cartas:
            mano_str += str(carta) + " "
        return mano_str


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = Mano()

    def agregar_carta_a_mano(self, carta):   #agregar una carta a la mano del jugador
        self.mano.agregar_carta(carta)

    def __str__(self):
        return f"Mano de {self.nombre}: {self.mano}"


class JuegoBlackjack:  #clase que permite el inicio del juego, se establecen todas las situaciones a pasar en el juego
    def __init__(self):   #se ut
        self.baraja= Baraja()
        self.baraja.mezclar()
        self.jugador = Jugador("Jugador")
        self.casa = Jugador("Casa")
        self.terminado = False

    def repartir_cartas_iniciales(self): 
        for _ in range(2):
            self.jugador.agregar_carta_a_mano(self.baraja.sacar_carta())
            self.casa.agregar_carta_a_mano(self.baraja.sacar_carta())

    def jugar(self):
        self.repartir_cartas_iniciales()
        self.mostrar_estado_juego()

        while not self.terminado:
            eleccion = input("¿Quieres [P]edir otra carta o [S]Parar? ").upper()

            if eleccion == "P":
                self.jugador.agregar_carta_a_mano(self.baraja.sacar_carta())
                self.mostrar_estado_juego()

                valor_jugador = self.jugador.mano.obtener_valor()
                if valor_jugador > 21:
                    self.terminado = True
                    print("Te has pasado de 21. ¡Has perdido!")
            elif eleccion == "S":
                self.terminado = True
                self.jugar_turno_casa()
                self.mostrar_resultado()
            else:
                print("Entrada inválida. Por favor, intenta de nuevo.")

    def jugar_turno_casa(self):
        while self.casa.mano.obtener_valor() < 19:
            self.casa.agregar_carta_a_mano(self.baraja.sacar_carta())

    def mostrar_estado_juego(self):
        print(f"\nMano de la Casa: {self.casa.mano.cartas[0]} [Carta Oculta]")
        print(self.jugador)
        print(f"Valor de la Mano del Jugador: {self.jugador.mano.obtener_valor()}")

    def mostrar_resultado(self):
        valor_jugador = self.jugador.mano.obtener_valor()
        valor_casa = self.casa.mano.obtener_valor()

        print(f"\nMano de la Casa: {self.casa.mano}")
        print(f"Valor de la Mano de la Casa: {valor_casa}")
        print(self.jugador)
        print(f"Valor de la Mano del Jugador: {valor_jugador}")

        if valor_jugador > 21:   #establecer lo que vaya a pasar dependiendo de la situación y valores obtenidos
            print("Te has pasado de 21. ¡Has perdido!")
        elif valor_casa > 21:
            print("La Casa se ha pasado de 21. ¡Has ganado!")
        elif valor_jugador > valor_casa:
            print("¡Has ganado!")
        elif valor_jugador < valor_casa:
            print("¡Has perdido!")
        else:
            print("¡Es un empate!")



juego = JuegoBlackjack()
juego.jugar()
