class ClueGenerator:
    def __init__(self, grid_logic):
        self.grid_logic = grid_logic

    def generate_horizontal_clues(self):
        horizontal_clues = []
        for row in self.grid_logic:
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

    def generate_vertical_clues(self):
        vertical_clues = []
        for col in range(len(self.grid_logic[0])):
            clue = []
            count = 0
            for row in range(len(self.grid_logic)):
                if self.grid_logic[row][col] == 1:
                    count += 1
                elif count > 0:
                    clue.append(count)
                    count = 0
            if count > 0:
                clue.append(count)
            vertical_clues.append(clue if clue else [0])
        return vertical_clues