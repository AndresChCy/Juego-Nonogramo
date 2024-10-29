from srcs.Logica.Niveles import Niveles
from srcs.Logica.matrizTotext import MatrizToText


def test_niveles( tmp_path):
    matriz_to_text = MatrizToText()
    matriz = [['1', '0', '1'], ['0', '1', '0'], ['1', '1', '1']]
    archivo = tmp_path / "matrizToTextTest.txt"

    # Llamar al método
    matriz_to_text.matrizToText(matriz, archivo)
    niveles = Niveles(tmp_path)
    assert (len(niveles.getList()),1)
    assert((niveles.getList()[0].getSol()),matriz)


