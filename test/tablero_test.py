import unittest

from srcs.Logica.Dibujo import Dibujo
from srcs.Logica.Tablero import Tablero


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
        self.assertEqual(comprHor, [[(1,1)],[(0,1)]])
        self.assertEqual(comprVert, [[(1,1)]])

    def test_compresion2(self):
        solucion = Dibujo(2, 1)
        solucion.pintar(0, 0, 1)
        tablero = Tablero(solucion)
        comprVert, comprHor = tablero.Compresion()
        self.assertEqual(comprVert, [[(1,1)], [(0,1)]])
        self.assertEqual(comprHor, [[(1,1)]])

    def test_compresion3(self):
        solucion = Dibujo(3, 3)
        solucion.pintar(0, 0, 1)
        tablero = Tablero(solucion)
        comprVert, comprHor = tablero.Compresion()
        self.assertEqual(comprVert, [[(1,1)],[(0,1)],[(0,1)]])
        self.assertEqual(comprHor, [[(1,1)], [(0,1)], [(0,1)]])

    def test_compresion4(self):
        solucion = Dibujo(3, 3)
        solucion.pintar(0, 0, 2)
        tablero = Tablero(solucion)
        comprVert, comprHor = tablero.Compresion()
        self.assertEqual(comprVert, [[(1,2)],[(0,1)],[(0,1)]])
        self.assertEqual(comprHor, [[(1,2)], [(0,1)], [(0,1)]])

    def test_compresion5(self):
        solucion = Dibujo(3, 3)
        solucion.pintar(0, 0, 2)
        solucion.pintar(0,1,1)
        tablero = Tablero(solucion)
        comprVert, comprHor = tablero.Compresion()
        self.assertEqual(comprVert, [[(1,2),(1,1)],[(0,1)],[(0,1)]])
        self.assertEqual(comprHor, [[(1,2)], [(1,1)], [(0,1)]])

if __name__ == '__main__':
    unittest.main()
