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

        # Inicializa las celdas y los mapeos de colores
        self._initialize_cells()
        self.mapping_colores = Colores.get_number_mapping()  # Mapeo numérico de colores
        self.mapping_colores_inverso = Colores.get_reverse_mapping()  # Mapeo inverso de colores

    def _initialize_cells(self):
        """
        Inicializa todas las celdas de la cuadrícula.
        """
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                cell = Cell(self.offset_x + col * self.cell_size, self.offset_y + row * self.cell_size, self.cell_size)
                self.all_cells.add(cell)

        for cell in self.all_cells:
            cell.empty()

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
                cell_value = int(grid_logic[row][col])  # Identificador de color o acción especial
                # Usa el mapeo para determinar el color o la acción especial
                if 1 <= cell_value <= 36:
                    cell_sprite.fill(cell_value, self.mapping_colores)  # Pinta la celda con el color correspondiente
                elif cell_value == 0:
                    cell_sprite.empty()
                elif cell_value == -1:
                    cell_sprite.mark()  # Marca la celda
                elif cell_value == -2:
                    cell_sprite.point()  # Pone la celda en estado apuntado
                else:
                    cell_sprite.empty()  # Limpia la celda

    def draw_cells(self, screen):
        """
        Dibuja todas las celdas en la pantalla.

        Args:
            screen (pygame.Surface): La superficie de la pantalla donde se dibujarán las celdas.
        """
        for cell in self.all_cells:
            cell.draw(screen)