class MatrizToText:
    def matrizToText(self, matriz, directorio):
        with open(directorio, "w") as f:
            for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                    f.write(str(matriz[i][j]))
                    if j < len(matriz[i]) - 1:
                        f.write(" ")
                f.write("\n")