import pygame
from Colores import Colores


class VictoryMiniatureRenderer:
    def __init__(self, screen, grid_logic, offset_x, offset_y, cell_manager, width, height):
        """
        Initializes the miniature renderer for the victory screen.

        Args:
            screen (pygame.Surface): The screen surface where the miniature will be drawn.
            grid_logic (list of list of int): The current grid logic.
            offset_x (int): The x offset.
            offset_y (int): The y offset.
            cell_manager (CellManager): The cell manager.
            width (int): The width of the miniature.
            height (int): The height of the miniature.
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
        Draws the miniature grid on the screen with a gray border.
        """
        # Draw the grid cells
        for row in range(len(self.grid_logic)):
            for col in range(len(self.grid_logic[row])):
                color = Colores.BLACK.value if self.grid_logic[row][col] == 1 else Colores.WHITE.value
                pygame.draw.rect(self.screen, color,
                                 (self.miniature_offset_x + col * self.miniature_size,
                                  self.miniature_offset_y + row * self.miniature_size,
                                  self.miniature_size, self.miniature_size))

        # Draw the gray border
        border_rect = pygame.Rect(self.miniature_offset_x, self.miniature_offset_y,
                                  self.miniature_size * len(self.grid_logic[0]),
                                  self.miniature_size * len(self.grid_logic))
        pygame.draw.rect(self.screen, Colores.GREY.value, border_rect, 3)