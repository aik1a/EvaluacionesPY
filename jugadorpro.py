class JugadorPro:

    def __init__(self, nombre, edad, nivel):
        self.nombre = nombre
        self.edad = edad
        self.nivel = nivel

    def setnombre(self, nuevoNombre):
        self.nombre = nuevoNombre 

    def getnombre(self):
        return self.nombre

    def setedad(self, nuevaEdad):
        self.edad = nuevaEdad

    def getedad(self):
        return self.edad

    def setnivel(self, nuevoNivel):
        self.nivel = nuevoNivel

    def getnivel(self):
        return self.nivel

    def __str__(self):
        return "Jugador: " + self.nombre + " nivel actual: " + (self.nivel)
