import numpy

class Dibujo:
    
    def __init__(self , x ,y):
        self.boceto = numpy.zeros((x, y))

    def pintar(self, x, y,color):
        self.boceto[x][y] = color

    def comprimir(self, x, y, color):
        pass
    def getMatriz(self):
        return self.boceto
    def cargarMatriz(self,matriz):
        self.boceto = matriz
