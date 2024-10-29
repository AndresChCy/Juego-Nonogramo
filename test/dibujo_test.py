import unittest
from srcs.Logica.Dibujo import Dibujo

class dibujo_test(unittest.TestCase):
   def test_pintar(self):
        boceto = Dibujo(1, 2)
        boceto.pintar(0, 0, 1)
        self.assertEqual(boceto.getMatriz()[0][0], 1)  # add assertion here
        self.assertEqual(boceto.getMatriz()[0][1], 0)

if __name__ == '__main__':
    unittest.main()
