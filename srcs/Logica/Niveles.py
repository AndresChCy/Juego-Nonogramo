import random
import pickle

from os import listdir
from random import randint

from srcs.Logica.Dibujo import Dibujo
from srcs.Logica.Tablero import Tablero


class Niveles:
    def __init__(self):
        self.nivelesPredeterminados = [[],[],[]]
        self.nivelesCreados = [[],[],[]]

       # aux = listdir(path)
       # self.niveles = []
       # for nivel in aux:
       #     archivo = path / nivel
       #     matriz = TextToMatrix.crearMatriz(archivo)
       #     dibujo = Dibujo(0,0)
       #     dibujo.cargarMatriz(matriz)
       #     tablero = Tablero(dibujo)
       #     self.niveles.append(tablero)

    def agregarTableroPredeterminado(self, tablero:Tablero):
        if (tablero == None):
            print("Invalido")
            return
        num_casillas = len(tablero.getProgreso())*len(tablero.getProgreso()[0])
        if num_casillas<=0:
            print("Invalido.")
            return

        if num_casillas<=100:
            self.nivelesPredeterminados[0].append(tablero)
        elif 100<num_casillas<=1000:
            self.nivelesPredeterminados[1].append(tablero)
        elif 1000<num_casillas:
            self.nivelesPredeterminados[2].append(tablero)

    def agregarTableroCreado(self, tablero: Tablero):
        if (tablero == None):
            print("Invalido")
            return
        num_casillas = len(tablero.getProgreso()) * len(tablero.getProgreso()[0])
        if num_casillas<=0:
            print("Invalido.")
            return

        if num_casillas <= 100:
            self.nivelesCreados[0].append(tablero)
        elif 100 < num_casillas <= 1000:
            self.nivelesCreados[1].append(tablero)
        elif 1000 < num_casillas:
            self.nivelesCreados[2].append(tablero)

    def tableroPredeterminadoRandom(self):
        if not any(self.nivelesPredeterminados):
            print("No hay niveles.")
            return

        nivelAleatorio = random.choice(self.nivelesPredeterminados)
        while not nivelAleatorio:
            nivelAleatorio = random.choice(self.nivelesPredeterminados)
            print("...")

        tablero = random.choice(nivelAleatorio)
        return tablero

    def tableroCreadoRandom(self):
        if not any(self.nivelesCreados):
            print("No hay niveles.")
            return

        nivelAleatorio = random.choice(self.nivelesCreados)
        while not nivelAleatorio:
            nivelAleatorio = random.choice(self.nivelesCreados)
            print("...")

        tablero = random.choice(nivelAleatorio)
        return tablero

    def getTableroAleatorio(self):
        listaAleatoria = random.choice((self.nivelesPredeterminados, self.nivelesCreados))
        if not any(listaAleatoria):
            return None

        nivelAleatorio = random.choice(listaAleatoria)
        while not nivelAleatorio:
            nivelAleatorio = random.choice(listaAleatoria)
            print("...")

        tablero = random.choice(nivelAleatorio)
        return tablero

    def GuardarNivelesCreados(self):
        fichero_binario = open("Lista_Niveles_Usuario", "wb")
        pickle.dump(self.nivelesCreados, fichero_binario)
        fichero_binario.close()
        del (fichero_binario)

    def CargarNivelesCreados(self):
        fichero = open("Lista_Niveles_Usuario", "rb")
        self.nivelesCreados = pickle.load(fichero)

    def GuardarNivelesPredeterminados(self):
        fichero_binario = open("Lista_Niveles_Predeterminados", "wb")
        pickle.dump(self.nivelesPredeterminados, fichero_binario)
        fichero_binario.close()
        del(fichero_binario)

    def CargarNivelesPredeterminados(self):
        fichero = open("Lista_Niveles_Predeterminados", "rb")
        self.nivelesPredeterminados = pickle.load(fichero)
        print(self.nivelesPredeterminados)

    def getNivelesBase(self):
        return self.nivelesPredeterminados

    def getNivelesCreados(self):
        return self.nivelesCreados