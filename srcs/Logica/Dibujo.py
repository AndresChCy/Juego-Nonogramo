import numpy
from abc import ABC , abstractmethod

class Pintable(ABC):
    @abstractmethod
    def pintar(self, x, y,color):
        pass

    @abstractmethod
    def getProgreso(self):
        pass

    def reiniciar(self):
        pass


class Dibujo(Pintable):
    
    def __init__(self , x ,y):
        self.boceto = numpy.zeros((x, y),dtype=int)
        self.undo = []
        self.rUndo = []

    def pintar(self, x, y,color):
        if color != self.getProgreso()[x][y]:
            self.undo.append([x, y,self.boceto[x][y]])
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

    def getUndo(self):
        if len(self.undo) == 0:
            return
        cima = self.undo.pop()
        color = self.getProgreso()[cima[0]][cima[1]]
        self.rUndo.append([cima[0],cima[1],color])
        self.boceto[cima[0]][cima[1]] = cima[2]


    def getRUndo(self):
        if len(self.rUndo) == 0:
            return
        cima = self.rUndo.pop()
        self.pintar(cima[0],cima[1],cima[2])


