import os
import unittest

from srcs.Logica.Dibujo import Dibujo
from srcs.Logica.Niveles import Niveles
from srcs.Logica.Tablero import Tablero


class almacenar_test(unittest.TestCase):
    def setUp(self):
        self.niveles = Niveles()

    def test_agregarTableroPredeterminado(self):
        #Tablero Nulo (No se agrega)
        tablero_nulo = None
        self.niveles.agregarTableroPredeterminado(tablero_nulo)
        self.assertEqual(self.niveles.nivelesPredeterminados, [[], [], []])

        #Tablero 100 casillas (Agregado en la primera lista)
        dibujo = Dibujo(10,10)
        tablero_pequeno = Tablero(dibujo)
        self.niveles.agregarTableroPredeterminado(tablero_pequeno)
        self.assertIn(tablero_pequeno, self.niveles.nivelesPredeterminados[0])

        #Tablero 600 casillas (Agregado en la segunda lista)
        dibujo2 = Dibujo(20, 30)
        tablero_mediano = Tablero(dibujo2)
        self.niveles.agregarTableroPredeterminado(tablero_mediano)
        self.assertIn(tablero_mediano, self.niveles.nivelesPredeterminados[1])

        #Tablero 2500 casillas (Agregado en la tercera lista)
        dibujo3 = Dibujo(50, 50)
        tablero_grande = Tablero(dibujo3)
        self.niveles.agregarTableroPredeterminado(tablero_grande)
        self.assertIn(tablero_grande, self.niveles.nivelesPredeterminados[2])

    def test_agregarTableroCreado(self):
        #Tablero Nulo (No se agrega)
        tablero_nulo = None
        self.niveles.agregarTableroCreado(tablero_nulo)
        self.assertEqual(self.niveles.nivelesCreados, [[], [], []])

        #25 Casillas
        dibujo = Dibujo(5, 5)
        tablero_pequeno = Tablero(dibujo)
        self.niveles.agregarTableroCreado(tablero_pequeno)
        self.assertIn(tablero_pequeno, self.niveles.nivelesCreados[0])

        #225 Casillas
        dibujo2 = Dibujo(15, 15)
        tablero_mediano = Tablero(dibujo2)
        self.niveles.agregarTableroCreado(tablero_mediano)
        self.assertIn(tablero_mediano, self.niveles.nivelesCreados[1])

        #1600 Casillas
        dibujo3 = Dibujo(40, 40)
        tablero_grande = Tablero(dibujo3)
        self.niveles.agregarTableroCreado(tablero_grande)
        self.assertIn(tablero_grande, self.niveles.nivelesCreados[2])

    def test_getTableroPredeterminado(self):
        dibujo = Dibujo(5, 5)
        dibujo2 = Dibujo(15, 15)
        dibujo3 = Dibujo(40, 40)
        tablero1 = Tablero(dibujo)
        tablero2 = Tablero(dibujo2)
        tablero3 = Tablero(dibujo3)

        self.niveles.agregarTableroPredeterminado(tablero1)
        self.niveles.agregarTableroPredeterminado(tablero2)
        self.niveles.agregarTableroPredeterminado(tablero3)

        result = self.niveles.tableroPredeterminadoRandom()
        self.assertIn(result, [tablero1, tablero2, tablero3])

    def test_getTableroCreado(self):
        dibujo = Dibujo(10, 10)
        dibujo2 = Dibujo(20, 30)
        dibujo3 = Dibujo(50, 50)
        tablero1 = Tablero(dibujo)
        tablero2 = Tablero(dibujo2)
        tablero3 = Tablero(dibujo3)

        self.niveles.agregarTableroCreado(tablero1)
        self.niveles.agregarTableroCreado(tablero2)
        self.niveles.agregarTableroCreado(tablero3)

        result = self.niveles.tableroCreadoRandom()
        self.assertIn(result, [tablero1, tablero2, tablero3])

    def test_guardar_y_cargar_niveles_predeterminados(self):
        dibujo = Dibujo(10, 10)
        tablero = Tablero(dibujo)
        self.niveles.agregarTableroPredeterminado(tablero)
        self.niveles.GuardarNivelesPredeterminados()

        nuevo_niveles = Niveles()
        nuevo_niveles.CargarNivelesPredeterminados()
        self.assertEqual(nuevo_niveles.nivelesPredeterminados[0][0].getProgreso().all(), self.niveles.nivelesPredeterminados[0][0].getProgreso().all())

        os.remove("Lista_Niveles_Predeterminados")

    def test_guardar_y_cargar_niveles_creados(self):
        dibujo = Dibujo(5, 10)
        tablero = Tablero(dibujo)
        self.niveles.agregarTableroCreado(tablero)
        self.niveles.GuardarNivelesCreados()

        nuevo_niveles = Niveles()
        nuevo_niveles.CargarNivelesCreados()
        self.assertEqual(nuevo_niveles.nivelesCreados[0][0].getProgreso().all(), self.niveles.nivelesCreados[0][0].getProgreso().all())

        os.remove("Lista_Niveles_Usuario")

if __name__ == '__main__':
    unittest.main()
