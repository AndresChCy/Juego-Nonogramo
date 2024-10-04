import pygame
from Colores import Colores

class MiniatureRenderer:
    def __init__(self, screen, grid_logic, offset_x, offset_y, cell_manager):
        self.screen = screen
        self.grid_logic = grid_logic
        self.miniature_size = min(125 // cell_manager.grid_width, 125 // cell_manager.grid_height)
        self.miniature_offset_x = offset_x - (cell_manager.grid_width * self.miniature_size) - 5
        self.miniature_offset_y = offset_y - (cell_manager.grid_height * self.miniature_size) - 5

    def draw_miniature(self):
        for row in range(len(self.grid_logic)):
            for col in range(len(self.grid_logic[row])):
                color = Colores.BLACK.value if self.grid_logic[row][col] == 1 else Colores.WHITE.value
                pygame.draw.rect(self.screen, color,
                                 (self.miniature_offset_x + col * self.miniature_size,
                                  self.miniature_offset_y + row * self.miniature_size,
                                  self.miniature_size, self.miniature_size))