import numpy
from abc import ABC , abstractmethod

class Pintable(ABC):
    @abstractmethod
    def pintar(self, x, y,color):
        pass

    @abstractmethod
    def getProgreso(self):
        pass

class Dibujo(Pintable):
    
    def __init__(self , x ,y):
        self.boceto = numpy.zeros((x, y))

    def pintar(self, x, y,color):
        self.boceto[x][y] = color

    def comprimir(self, x, y, color):
        pass
    def getProgreso(self):
        return self.boceto
    def cargarMatriz(self,directorio):
        with open(directorio, 'r') as f:
            datos = f.readlines()

        matriz = []
        for linea in datos:
            # Eliminamos el salto de línea y dividimos por espacios (o puedes usar otro separador)
            matriz.append(linea.strip().split())
        self.boceto = numpy.zeros((len(matriz),len(matriz[0])))
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                self.pintar(i,j,(int)(matriz[i][j]))
