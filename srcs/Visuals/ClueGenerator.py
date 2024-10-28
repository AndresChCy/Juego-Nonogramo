def _generate_clues(line):
    """
    Genera las pistas para una línea (fila o columna).

    Args:
        line (list of int): Una fila o columna de la matriz.

    Returns:
        list of int: Las pistas para la línea.
    """
    clues = []
    count = 0
    for cell in line:
        if cell == 1:
            count += 1
        elif count > 0:
            clues.append(count)
            count = 0
    if count > 0:
        clues.append(count)
    return clues if clues else [0]


class ClueGenerator:
    def __init__(self, matrix):
        """
        Inicializa el generador de pistas.

        Args:
            matrix (list of list of int): La matriz que contiene la solución del Nonograma.
        """
        self.matrix = matrix

    def generate_horizontal_clues(self):
        """
        Genera las pistas horizontales basadas en la matriz.

        Returns:
            list of list of int: Las pistas horizontales.
        """
        return [_generate_clues(row) for row in self.matrix]

    def generate_vertical_clues(self):
        """
        Genera las pistas verticales basadas en la matriz.

        Returns:
            list of list of int: Las pistas verticales.
        """
        transposed_matrix = zip(*self.matrix)
        return [_generate_clues(col) for col in transposed_matrix]

    