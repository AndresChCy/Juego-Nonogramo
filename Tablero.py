from Dibujo import Dibujo

class Tablero:
    def __init__(self, solucion):
        self.solucion = solucion
        self.progreso = Dibujo(len(solucion.getMatriz()), len(solucion.getMatriz()[0]))

    def CompararDibujos(self):
        juego = self.solucion.getMatriz()
        usuario = self.progreso.getMatriz()

        for i in range(len(juego)):
            for j in range(len(juego[0])):
                if(usuario[i][j] != juego[i][j]):
                    return False
        return True

    def Compresion(self):
        matriz = self.solucion.getMatriz()
        comprVert = []
        comprHor = []
        aux = []
        count = 0
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if matriz[i][j] == 1:
                    count += 1
                else:
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
                else:
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

    def pintarProgreso(self):
        pass

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
                        f.write(str(matriz[i][j]))
                        if j < len(matriz[i]) - 1:
                            f.write(" ")
                    f.write("\n")