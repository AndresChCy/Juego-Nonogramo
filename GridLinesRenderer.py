import pygame
from Colores import Colores

class GridLinesRenderer:
    def __init__(self, screen, cell_manager, offset_x, offset_y, cell_size):
        self.screen = screen
        self.cell_manager = cell_manager
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.cell_size = cell_size

    def draw_grid_lines(self):
        for row in range(self.cell_manager.grid_height + 1):
            line_thickness = 3 if row % 5 == 0 else 1
            pygame.draw.line(self.screen, Colores.BLACK.value,
                             (self.offset_x, self.offset_y + row * self.cell_size),
                             (self.offset_x + self.cell_manager.grid_width * self.cell_size, self.offset_y + row * self.cell_size),
                             line_thickness)
        for col in range(self.cell_manager.grid_width + 1):
            line_thickness = 3 if col % 5 == 0 else 1
            pygame.draw.line(self.screen, Colores.BLACK.value,
                             (self.offset_x + col * self.cell_size, self.offset_y),
                             (self.offset_x + col * self.cell_size, self.offset_y + self.cell_manager.grid_height * self.cell_size),
                             line_thickness)