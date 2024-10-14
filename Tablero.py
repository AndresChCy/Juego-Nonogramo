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
        pass

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

    def guardarProgreso(self):
        pass