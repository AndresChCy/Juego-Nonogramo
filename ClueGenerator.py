class ClueGenerator:
    def __init__(self, grid_logic):
        self.grid_logic = grid_logic

    def generate_horizontal_clues(self, matrix=None):
        if matrix is None:
            matrix = self.grid_logic
        horizontal_clues = []
        for row in matrix:
            clue = []
            count = 0
            for cell in row:
                if cell == 1:
                    count += 1
                elif count > 0:
                    clue.append(count)
                    count = 0
            if count > 0:
                clue.append(count)
            horizontal_clues.append(clue if clue else [0])
        return horizontal_clues

    def generate_vertical_clues(self, matrix=None):
        if matrix is None:
            matrix = self.grid_logic
        vertical_clues = []
        for col in range(len(matrix[0])):
            clue = []
            count = 0
            for row in range(len(matrix)):
                if matrix[row][col] == 1:
                    count += 1
                elif count > 0:
                    clue.append(count)
                    count = 0
            if count > 0:
                clue.append(count)
            vertical_clues.append(clue if clue else [0])
        return vertical_clues