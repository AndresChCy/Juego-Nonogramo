class TextToMatriz:
    def crearMatriz(directorio):
        with open(directorio, 'r') as f:
             datos = f.readlines()

        matriz = []
        for linea in datos:
             # Eliminamos el salto de línea y dividimos por espacios (o puedes usar otro separador)
             matriz.append(linea.strip().split())
        return matriz

def test_crearMatriz():
    assert TextToMatriz.crearMatriz("../test/textToMatrizTest1") == [['1', '0', '1'], ['0', '1', '0'], ['1', '1', '1']]
    assert TextToMatriz.crearMatriz("../test/textToMatrizTest2") == [['1', '0', '1'], ['0', '1', '0'], ['1']]
    assert TextToMatriz.crearMatriz("../test/textToMatrizTest3") != [['98', '0', '1'], ['0', '1', '0'], ['1', '-1', '1']]  #Se espera que no se igual por que no esta en el "formato" o estilo en el que se escriben las matrices