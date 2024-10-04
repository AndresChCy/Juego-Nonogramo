import pygame
from Colores import Colores

class GridRenderer:
    def __init__(self, screen, cell_manager, clue_generator, offset_x, offset_y, cell_size):
        self.screen = screen
        self.cell_manager = cell_manager
        self.clue_generator = clue_generator
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.cell_size = cell_size
        self.font = pygame.font.SysFont('Raleway Bolt', 20)

    def draw_grid_lines(self):
        for row in range(self.cell_manager.grid_height + 1):
            pygame.draw.line(self.screen, Colores.BLACK.value,
                             (self.offset_x, self.offset_y + row * self.cell_size),
                             (self.offset_x + self.cell_manager.grid_width * self.cell_size, self.offset_y + row * self.cell_size))
        for col in range(self.cell_manager.grid_width + 1):
            pygame.draw.line(self.screen, Colores.BLACK.value,
                             (self.offset_x + col * self.cell_size, self.offset_y),
                             (self.offset_x + col * self.cell_size, self.offset_y + self.cell_manager.grid_height * self.cell_size))

    def draw_horizontal_clues(self):
        horizontal_clues = self.clue_generator.generate_horizontal_clues()
        for row_idx, clue in enumerate(horizontal_clues):
            total_width = 0
            for clue_number in reversed(clue):
                clue_text = str(clue_number)
                text_surface = self.font.render(clue_text, True, Colores.BLACK.value)
                text_width = text_surface.get_width()
                x = self.offset_x - total_width - text_width - 5
                y = self.offset_y + row_idx * self.cell_size + self.cell_size // 4
                self.screen.blit(text_surface, (x, y))
                total_width += text_width + 5

    def draw_vertical_clues(self):
        vertical_clues = self.clue_generator.generate_vertical_clues()
        for col_idx, clue in enumerate(vertical_clues):
            for i, num in enumerate(reversed(clue)):
                text_surface = self.font.render(str(num), True, Colores.BLACK.value)
                text_height = text_surface.get_height()
                x = self.offset_x + col_idx * self.cell_size + self.cell_size // 4
                y = self.offset_y - (len(clue) - i) * text_height
                self.screen.blit(text_surface, (x, y))

    def draw(self):
        self.cell_manager.all_cells.draw(self.screen)
        self.draw_grid_lines()
        self.draw_horizontal_clues()
        self.draw_vertical_clues()