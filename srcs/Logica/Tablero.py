
from srcs.Logica.Dibujo import Dibujo, Pintable
import random

class Tablero(Pintable):

    def __init__(self, solucion):
        self.solucion = solucion
        self.progreso = Dibujo(len(solucion.getProgreso()), len(solucion.getProgreso()[0]))
        self.colors = set()
        self.comprVer,self.comprHor = self.Compresion()
        self.undo = []
        self.rUndo = []


    def CompararDibujos(self):
        juego = self.solucion.getProgreso()
        usuario = self.progreso.getProgreso()

        for i in range(len(juego)):
            for j in range(len(juego[0])):
                if(usuario[i][j] != juego[i][j]):
                    if (usuario[i][j] >= 0 and juego[i][j] >= 0):
                        return False
                    elif(usuario[i][j] < 0 and juego[i][j] >= 1):
                        return False
        return True

    def Compresion(self):
        matriz = self.solucion.getProgreso()
        comprVert = []
        comprHor = []
        aux = []
        count = 0
        color = 0
        for i in range(len(matriz)):
            color = matriz[i][0]
            for j in range(len(matriz[0])):
                if matriz[i][j] == color and color != 0:
                    count += 1
                elif count != 0:
                    aux.append((count,color))
                    self.colors.add(color)
                    count = 0
                    color = matriz[i][j]
                    if color != 0:
                        count += 1
                elif matriz[i][j] != 0:
                    count+=1
                    color = matriz[i][j]
            if aux == []:
                aux.append((count,color))
                count = 0
            elif count != 0:
                aux.append((count,color))
                self.colors.add(color)
                count = 0
            comprVert.append(aux)
            aux = []
        count = 0
        for i in range(len(matriz[0])):
            color = matriz[0][i]
            for j in range(len(matriz)):
                if matriz[j][i] == color and color != 0:
                    count += 1
                elif count != 0:
                    aux.append((count,color))
                    count = 0
                    color = matriz[j][i]
                    if color != 0:
                        count += 1
                elif matriz[j][i] != 0:
                    count += 1
                    color = matriz[j][i]
            if aux == []:
                aux.append((count,color))
                count = 0
            elif count != 0:
                aux.append((count,color))
                count = 0
            comprHor.append(aux)
            aux = []
        return comprVert, comprHor

    def pintar(self, x, y, color):
        if color != self.getProgreso()[x][y]:
            self.undo.append([x, y,self.getProgreso()[x][y]])
            self.progreso.pintar(x,y,color)
            self.rUndo = []
            self.CompararDibujos()

    def cargarProgreso(directorio):
            with open(directorio, 'r') as f:
                datos = f.readlines()

            matriz = []
            for linea in datos:
                # Eliminamos el salto de línea y dividimos por espacios (o puedes usar otro separador)
                matriz.append(linea.strip().split())
            return matriz

    def guardarProgreso(self, matriz, directorio):
            with open(directorio, "w") as f:
                for i in range(len(matriz)):
                    for j in range(len(matriz[i])):
                        f.write(str((int)(matriz[i][j])))
                        if j < len(matriz[i]) - 1:
                            f.write(" ")
                    f.write("\n")

    def pista(self):
        juego = self.solucion.getProgreso()
        usuario = self.progreso.getProgreso()
        i = random.randint(0, len(juego)-1)
        j = random.randint(0, len(juego[0])-1)
        while(True):
            if juego[i][j] != usuario[i][j]:
                self.pintar(i,j,juego[i][j])
                break
            else:
                i = random.randint(0, len(juego)-1)
                j = random.randint(0, len(juego[0])-1)

    def getProgreso(self):
        return self.progreso.getProgreso()
    def getSolucion(self):
        return self.solucion.getProgreso()
    def getCompresiones(self):
        return self.comprVer,self.comprHor

    def getColors(self):
        return self.colors

    def reiniciar(self):
        self.progreso = Dibujo(len(self.solucion.getProgreso()), len(self.solucion.getProgreso()[0]))

    def getUndo(self):
        if len(self.undo) == 0:
            return
        cima = self.undo.pop()
        color = self.getProgreso()[cima[0]][cima[1]]
        self.rUndo.append([cima[0],cima[1],color])
        self.progreso.pintar(cima[0],cima[1],cima[2])
        print("lol")

    def getRUndo(self):
        if len(self.rUndo) == 0:
            return
        cima = self.rUndo.pop()
        self.undo.append([cima[0], cima[1], self.getProgreso()[cima[0]][cima[1]]])
        self.progreso.pintar(cima[0],cima[1],cima[2])


