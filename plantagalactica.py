class PlantaGalactica:
    def __init__(self, nombreEspecie, planeta_origen, altura):
        self.nombreEspecie = nombreEspecie
        self.planeta_origen = planeta_origen
        self.altura = altura

    def setAltura(self, nuevaAltura):
        self.altura = nuevaAltura

    def getaltura(self):
        return self.altura

    def __str__(self):
        return ("Planta " + self.nombreEspecie) + (" desde " + self.planeta_origen)


# Errores Corregidos
"""



        -Errorres de tabulacion en todo el documento
        -Errores de nomenclatura en variables y funciones las cuales generaban errores de sintaxis
        -Faltaba el self en la funcion setAltura y getaltura
        - Faltaban parentesis en funciones Self
        - Faltaban " dos puntos " tras los parentesis


"""