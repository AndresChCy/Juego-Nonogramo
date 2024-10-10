import unittest

from Dibujo import Dibujo
from tablero import tablero


class tablero_test(unittest.TestCase):
    def test_comparar(self):
        solucion= Dibujo( 1, 3)
        progreso = Dibujo (1,3)
        tablero = tablero()
        self.assertEqual(tablero.ComparacionMatrices, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
