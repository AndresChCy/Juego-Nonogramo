import pygame
from srcs.Visuals.Cell import Cell
from srcs.Visuals.Colores import Colores


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
        color_mapping = [
            Colores.BLACK.value, Colores.DARK_GREY.value, Colores.GREY.value, Colores.LIGHT_GREY.value,
            Colores.DARK_GREY.value, Colores.RED.value, Colores.GREEN.value, Colores.BLUE.value,
            Colores.YELLOW.value, Colores.CYAN.value, Colores.MAGENTA.value, Colores.ORANGE.value,
            Colores.PURPLE.value, Colores.PINK.value, Colores.BROWN.value, Colores.LIGHT_RED.value,
            Colores.LIGHT_BLUE.value, Colores.LIGHT_GREEN.value, Colores.LIGHT_YELLOW.value,
            Colores.LIGHT_CYAN.value, Colores.LIGHT_MAGENTA.value, Colores.LIGHT_ORANGE.value,
            Colores.LIGHT_PURPLE.value, Colores.LIGHT_PINK.value, Colores.LIGHT_BROWN.value,
            Colores.DARK_RED.value, Colores.DARK_BLUE.value, Colores.DARK_GREEN.value,
            Colores.DARK_YELLOW.value, Colores.DARK_CYAN.value, Colores.DARK_MAGENTA.value,
            Colores.DARK_ORANGE.value, Colores.DARK_PURPLE.value, Colores.DARK_PINK.value,
            Colores.DARK_BROWN.value, Colores.KHAKI.value
        ]
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                cell_idx = row * self.grid_width + col
                cell_sprite = self.all_cells.sprites()[cell_idx]
                cell_value = int(grid_logic[row][col])
                if 0 < cell_value < len(color_mapping):
                    cell_sprite.fill(color_mapping[cell_value])
                elif cell_value == -1:
                    cell_sprite.mark()
                elif cell_value == -2:
                    cell_sprite.point()
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
