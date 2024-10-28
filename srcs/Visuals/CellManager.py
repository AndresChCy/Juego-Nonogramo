import pygame
from Cell import Cell


class CellManager:
    def __init__(self, grid_width, grid_height, cell_size, offset_x, offset_y):
        """
        Inicializa las celdas.

        Args:
            grid_width (int): El ancho de la cuadrícula en número de celdas.
            grid_height (int): La altura de la cuadrícula en número de celdas.
            cell_size (int): El tamaño de cada celda.
            offset_x (int): El desplazamiento en el eje x.
            offset_y (int): El desplazamiento en el eje y.
        """
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.cell_size = cell_size
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.all_cells = pygame.sprite.Group()
        self._initialize_cells()

    def _initialize_cells(self):
        """
        Inicializa todas las celdas de la cuadrícula.
        """
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                cell = Cell(self.offset_x + col * self.cell_size, self.offset_y + row * self.cell_size, self.cell_size)
                self.all_cells.add(cell)

    def update_grid_visual(self, grid_logic):
        """
        Actualiza la visualización de la cuadrícula basada en la lógica de la cuadrícula.

        Args:
            grid_logic (list of list of int): La lógica actual de la cuadrícula.
        """
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                cell_idx = row * self.grid_width + col
                cell_sprite = self.all_cells.sprites()[cell_idx]
                if grid_logic[row][col] == 1:
                    cell_sprite.fill()
                elif grid_logic[row][col] == -1:
                    cell_sprite.mark()
                else:
                    cell_sprite.empty()

    def draw_cells(self, screen):
        """
        Dibuja todas las celdas en la pantalla.

        Args:
            screen (pygame.Surface): La superficie de la pantalla donde se dibujarán las celdas.
        """
        for cell in self.all_cells:
            cell.draw(screen)
