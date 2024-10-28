import pygame
from Colores import Colores

class VictoryMiniatureRenderer:
    def __init__(self, screen, grid_logic, offset_x, offset_y, cell_manager, width, height):
        """
        Inicializa el renderizador de miniaturas para la pantalla de victoria.

        Args:
            screen (pygame.Surface): La superficie de la pantalla donde se dibujará la miniatura.
            grid_logic (list of list of int): La lógica actual de la cuadrícula.
            offset_x (int): El desplazamiento en el eje x.
            offset_y (int): El desplazamiento en el eje y.
            cell_manager (CellManager): El gestor de celdas.
            width (int): El ancho de la miniatura.
            height (int): La altura de la miniatura.
        """
        self.screen = screen
        self.grid_logic = grid_logic
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.width = width
        self.height = height
        self.cell_manager = cell_manager
        self.miniature_size = min(width // cell_manager.grid_width, height // cell_manager.grid_height)
        self.miniature_offset_x = offset_x
        self.miniature_offset_y = offset_y

    def draw_miniature(self):
        """
        Dibuja la cuadrícula en miniatura en la pantalla con un borde gris.
        """
        # Dibuja las celdas de la cuadrícula
        for row in range(len(self.grid_logic)):
            for col in range(len(self.grid_logic[row])):
                color = Colores.BLACK.value if self.grid_logic[row][col] == 1 else Colores.WHITE.value
                pygame.draw.rect(self.screen, color,
                                 (self.miniature_offset_x + col * self.miniature_size,
                                  self.miniature_offset_y + row * self.miniature_size,
                                  self.miniature_size, self.miniature_size))

        # Dibuja el borde gris
        border_rect = pygame.Rect(self.miniature_offset_x, self.miniature_offset_y,
                                  self.miniature_size * len(self.grid_logic[0]),
                                  self.miniature_size * len(self.grid_logic))
        pygame.draw.rect(self.screen, Colores.GREY.value, border_rect, 3)