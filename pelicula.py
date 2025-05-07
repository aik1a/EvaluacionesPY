class Película:

    def __init__(self, titulo, director, duración):
        self.titulo = titulo
        self.director = director
        self.duración = duración

    def setDuracion(self, nuevaDuracion):
        self.duración = nuevaDuracion

    def getDuracion(self):
        return self.duración

    def __str__(self):
        return "Pelicula: " + self.titulo + " Dirigida por " + self.director
