from os import listdir

from srcs.Logica.Dibujo import Dibujo
from srcs.Logica.Tablero import Tablero
from textTomatrix import TextToMatrix

class Niveles:

    def __init__(self,path):
        aux = listdir(path)
        self.niveles = []
        for nivel in aux:
            archivo = path / nivel
            matriz = TextToMatrix.crearMatriz(archivo)
            dibujo = Dibujo(0,0)
            dibujo.cargarMatriz(matriz)
            tablero = Tablero(dibujo)
            self.niveles.append(tablero)

    def getList(self):
        return self.niveles