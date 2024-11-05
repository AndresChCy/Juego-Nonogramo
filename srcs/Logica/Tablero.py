
from srcs.Logica.Dibujo import Dibujo, Pintable


class Tablero(Pintable):
    def __init__(self, solucion):
        self.solucion = solucion
        self.progreso = Dibujo(len(solucion.getProgreso()), len(solucion.getProgreso()[0]))

    def CompararDibujos(self):
        juego = self.solucion.getProgreso()
        usuario = self.progreso.getProgreso()

        for i in range(len(juego)):
            for j in range(len(juego[0])):
                if(usuario[i][j] != juego[i][j]):
                    if (usuario[i][j] >= 0 and juego[i][j] >= 0):
                        return False
                    elif(usuario[i][j] < 0 and juego[i][j] == 1):
                        return False
        return True

    def Compresion(self):
        matriz = self.solucion.getProgreso()
        comprVert = []
        comprHor = []
        aux = []
        count = 0
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if matriz[i][j] == 1:
                    count += 1
                elif count != 0:
                    aux.append(count)
                    count = 0
            if aux == []:
                aux.append(count)
                count = 0
            elif count != 0:
                aux.append(count)
                count = 0
            comprVert.append(aux)
            aux = []
        count = 0
        for i in range(len(matriz[0])):
            for j in range(len(matriz)):
                if matriz[j][i] == 1:
                    count += 1
                elif count != 0:
                    aux.append(count)
                    count = 0
            if aux == []:
                aux.append(count)
                count = 0
            elif count != 0:
                aux.append(count)
                count = 0
            comprHor.append(aux)
            aux = []
        return comprVert, comprHor

    def pintar(self, x, y, color):
        self.progreso.pintar(x,y,color)

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

    def getProgreso(self):
        return self.progreso.getProgreso()
    def getSolucion(self):
        return self.solucion.getProgreso()

    def reiniciar(self):
        self.progreso = Dibujo(len(self.solucion.getProgreso()), len(self.solucion.getProgreso()[0]))

