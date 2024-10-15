import unittest

from Dibujo import Dibujo
from Tablero import Tablero


class tablero_test(unittest.TestCase):
    def test_comparar(self):
        solucion= Dibujo( 1, 3)
        progreso = Dibujo (1,3)
        tablero = Tablero(solucion)
        self.assertEqual(tablero.CompararDibujos(), True)  # add assertion here

    def test_compresion(self):
        solucion = Dibujo(1, 2)
        solucion.pintar(0, 0, 1)
        tablero = Tablero(solucion)
        comprVert, comprHor = tablero.Compresion()
        self.assertEqual(comprHor, [[1],[0]])
        self.assertEqual(comprVert, [1])

if __name__ == '__main__':
    unittest.main()
