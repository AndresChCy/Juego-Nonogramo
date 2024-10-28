class TextToMatrix:
    def crearMatriz(directorio):
        with open(directorio, 'r') as f:
             datos = f.readlines()

        matriz = []
        for linea in datos:
             # Eliminamos el salto de línea y dividimos por espacios (o puedes usar otro separador)
             matriz.append(linea.strip().split())
        return matriz


