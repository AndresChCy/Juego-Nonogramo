import os
import unittest

from srcs.Logica.Niveles import Niveles

class almacenar_test(unittest.TestCase):
    def setUp(self):
        self.niveles = Niveles()

    def test_agregarTableroPredeterminado(self):
        #Tablero Nulo (No se agrega)
        tablero_nulo = [[]]
        self.niveles.agregarTableroPredeterminado(tablero_nulo)
        self.assertEqual(self.niveles.nivelesPredeterminados, [[], [], []])

        #Tablero 100 casillas (Agregado en la primera lista)
        tablero_pequeno = [[0]*10]*10
        self.niveles.agregarTableroPredeterminado(tablero_pequeno)
        self.assertIn(tablero_pequeno, self.niveles.nivelesPredeterminados[0])

        #Tablero 600 casillas (Agregado en la segunda lista)
        tablero_mediano = [[0]*20]*30
        self.niveles.agregarTableroPredeterminado(tablero_mediano)
        self.assertIn(tablero_mediano, self.niveles.nivelesPredeterminados[1])

        #Tablero 2500 casillas (Agregado en la tercera lista)
        tablero_grande = [[0]*50]*50
        self.niveles.agregarTableroPredeterminado(tablero_grande)
        self.assertIn(tablero_grande, self.niveles.nivelesPredeterminados[2])

    def test_agregarTableroCreado(self):
        #Tablero Nulo (No se agrega)
        tablero_nulo = [[]]
        self.niveles.agregarTableroCreado(tablero_nulo)
        self.assertEqual(self.niveles.nivelesCreados, [[], [], []])

        #25 Casillas
        tablero_pequeno = [[0]*5]*5
        self.niveles.agregarTableroCreado(tablero_pequeno)
        self.assertIn(tablero_pequeno, self.niveles.nivelesCreados[0])

        #225 Casillas
        tablero_mediano = [[0]*15]*15
        self.niveles.agregarTableroCreado(tablero_mediano)
        self.assertIn(tablero_mediano, self.niveles.nivelesCreados[1])

        #1600 Casillas
        tablero_grande = [[0]*40]*40
        self.niveles.agregarTableroCreado(tablero_grande)
        self.assertIn(tablero_grande, self.niveles.nivelesCreados[2])

    def test_getTableroPredeterminado(self):
        tablero1 = [[0]*5]*5
        tablero2 = [[0]*15]*15
        tablero3 = [[0]*40]*40

        self.niveles.agregarTableroPredeterminado(tablero1)
        self.niveles.agregarTableroPredeterminado(tablero2)
        self.niveles.agregarTableroPredeterminado(tablero3)

        result = self.niveles.getTableroPredeterminado()
        self.assertIn(result, [tablero1, tablero2, tablero3])

    def test_getTableroCreado(self):
        tablero1 = [[0]*10]*10
        tablero2 = [[0]*20]*30
        tablero3 = [[0]*50]*50

        self.niveles.agregarTableroCreado(tablero1)
        self.niveles.agregarTableroCreado(tablero2)
        self.niveles.agregarTableroCreado(tablero3)

        result = self.niveles.getTableroCreado()
        self.assertIn(result, [tablero1, tablero2, tablero3])

    def test_guardar_y_cargar_niveles_predeterminados(self):
        tablero = [[0]*10]*10
        self.niveles.agregarTableroPredeterminado(tablero)
        self.niveles.GuardarNivelesPredeterminados()

        nuevo_niveles = Niveles()
        nuevo_niveles.CargarNivelesPredeterminados()
        self.assertEqual(nuevo_niveles.nivelesPredeterminados, self.niveles.nivelesPredeterminados)

        os.remove("Lista_Niveles_Predeterminados")

    def test_guardar_y_cargar_niveles_creados(self):
        tablero = [[0]*5]*10
        self.niveles.agregarTableroCreado(tablero)
        self.niveles.GuardarNivelesCreados()

        nuevo_niveles = Niveles()
        nuevo_niveles.CargarNivelesCreados()
        self.assertEqual(nuevo_niveles.nivelesCreados, self.niveles.nivelesCreados)

        os.remove("Lista_Niveles_Usuario")

if __name__ == '__main__':
    unittest.main()
