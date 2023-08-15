class Participante:
    def __init__(self, nombre):
        self.nombre = nombre 
        self.puntos = 0
        self.seleccion = ""
    def eleccion(self):
        self.eleccion = input("{nombre}, selecciona, piedra, papel o tijera:".format(nombre= self.nombre))
        print("{nombre} selecciona {seleccion}".format(nombre=self.nombre, seleccion = self.seleccion))
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




