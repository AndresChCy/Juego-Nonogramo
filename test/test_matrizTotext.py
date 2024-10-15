class MatrizToText:
    def matrizToText(self, matriz, directorio):
        with open(directorio, "w") as f:
            for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                    f.write(str(matriz[i][j]))
                    if j < len(matriz[i]) - 1:
                        f.write(" ")
                f.write("\n")


def test_matrizToText(tmp_path):
    matriz_to_text = MatrizToText()
    matriz = [['1', '0', '1'], ['0', '1', '0'], ['1', '1', '1']]
    archivo = tmp_path / "matrizToTextTest.txt"

    # Llamar al método
    matriz_to_text.matrizToText(matriz, archivo)

    # Leer el archivo y comprobar su contenido
    with open(archivo, 'r') as f:
        contenido = f.readlines()

    # Verificar que el contenido del archivo sea el esperado
    assert contenido == ['1 0 1\n', '0 1 0\n', '1 1 1\n']