import unittest

from Dibujo import Dibujo
from Tablero import Tablero


class tablero_test(unittest.TestCase):
    def test_comparar(self):
        solucion= Dibujo( 1, 3)
        progreso = Dibujo (1,3)
        tablero = Tablero(solucion)
        self.assertEqual(tablero.CompararDibujos(), True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
