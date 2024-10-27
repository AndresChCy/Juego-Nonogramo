import unittest

from Dibujo import Dibujo
from Tablero import Tablero


class tablero_test(unittest.TestCase):
    def test_comparar(self):
        solucion= Dibujo( 1, 3)
        progreso = Dibujo (1,3)
        tablero = Tablero(solucion)
        self.assertEqual(tablero.CompararDibujos(), True)

    def test_compresion(self):
        solucion = Dibujo(1, 2)
        solucion.pintar(0, 0, 1)
        tablero = Tablero(solucion)
        comprVert, comprHor = tablero.Compresion()
        self.assertEqual(comprHor, [[1],[0]])
        self.assertEqual(comprVert, [[1]])

    def test_compresion2(self):
        solucion = Dibujo(2, 1)
        solucion.pintar(0, 0, 1)
        tablero = Tablero(solucion)
        comprVert, comprHor = tablero.Compresion()
        self.assertEqual(comprVert, [[1], [0]])
        self.assertEqual(comprHor, [[1]])

    def test_compresion2(self):
        solucion = Dibujo(3, 3)
        solucion.pintar(0, 0, 1)
        tablero = Tablero(solucion)
        comprVert, comprHor = tablero.Compresion()
        self.assertEqual(comprVert, [[1],[0],[0]])
        self.assertEqual(comprHor, [[1], [0], [0]])

if __name__ == '__main__':
    unittest.main()
