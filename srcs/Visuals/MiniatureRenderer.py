import pygame
from srcs.Visuals.Colores import Colores


class MiniatureRenderer:

    def __init__(self, screen, grid_logic, offset_x, offset_y, cell_manager):
        """
        Inicializa la miniatura.

        Args:
            screen (pygame.Surface): La superficie de la pantalla donde se dibujará la miniatura.
            grid_logic (list of list of int): La lógica actual de la cuadrícula.
            offset_x (int): El desplazamiento en el eje x.
            offset_y (int): El desplazamiento en el eje y.
            cell_manager (CellManager): El administrador de celdas.
        """
        self.screen = screen
        self.grid_logic = grid_logic
        self.miniature_size = min(125 // cell_manager.grid_width, 125 // cell_manager.grid_height)
        self.miniature_offset_x = offset_x - (cell_manager.grid_width * self.miniature_size) - 5
        self.miniature_offset_y = offset_y - (cell_manager.grid_height * self.miniature_size) - 5

    def draw_miniature(self):
        """
        Dibuja la miniatura de la cuadrícula en la pantalla.
        """
        for row in range(len(self.grid_logic)):
            for col in range(len(self.grid_logic[row])):
                color = Colores.BLACK.value if self.grid_logic[row][col] == 1 else Colores.WHITE.value
                pygame.draw.rect(self.screen, color,
                                 (self.miniature_offset_x + col * self.miniature_size,
                                  self.miniature_offset_y + row * self.miniature_size,
                                  self.miniature_size, self.miniature_size))
