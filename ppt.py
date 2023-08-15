class Participante:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ""
    def eleccion(self):
        self.choice = input ("{name}, selecciona piedra, papel o tijera:" .format(name = self.name))
        print("{name} selecciona {choice}".format(name=self.name, choice = self.choice))
        
class Ronda:
    def __init__(self, p1, p2):
        p1.eleccion()
        p2.eleccion()
    def comparaSeleccion(self):
        print("implement")
    def puntosGanados(self):
        print("implement")
class Game:
    def __init__(self):
        self.finJuego = False
        self.participante = Participante("Spok")
        self.segundoParticipante = Participante("kirk")
    def start(self):
        ronda_juego = Ronda(self.participante, self.segundoParticipante)
    def checkEndCondition(self):
        print("implement")
    def determineWinner(self):
        print("implement")
game = Game()
game.start()