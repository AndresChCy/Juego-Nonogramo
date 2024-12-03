import pygame
from srcs.Visuals.Colores import Colores


class GridLinesRenderer:
    def __init__(self, screen, cell_manager, offset_x, offset_y, cell_size):
        """
        Inicializa los gráficos de las líneas delimitadoras de la cuadrícula.

        Args:
            screen (pygame.Surface): La superficie de la pantalla donde se dibujarán las líneas de la cuadrícula.
            cell_manager (CellManager): El administrador de celdas.
            offset_x (int): El desplazamiento en el eje x.
            offset_y (int): El desplazamiento en el eje y.
            cell_size (int): El tamaño de cada celda.
        """
        self.screen = screen
        self.cell_manager = cell_manager
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.cell_size = cell_size

    def draw_grid_lines(self):
        """
        Dibuja las líneas de la cuadrícula en la pantalla.
        """
        for row in range(self.cell_manager.grid_height + 1):
            line_thickness = 3 if row % 5 == 0 else 1
            pygame.draw.line(self.screen, Colores.BLACK.value,
                             (self.offset_x, self.offset_y + row * self.cell_size),
                             (self.offset_x + self.cell_manager.grid_width * self.cell_size,
                              self.offset_y + row * self.cell_size),
                             line_thickness)
        for col in range(self.cell_manager.grid_width + 1):
            line_thickness = 3 if col % 5 == 0 else 1
            pygame.draw.line(self.screen, Colores.BLACK.value,
                             (self.offset_x + col * self.cell_size, self.offset_y),
                             (self.offset_x + col * self.cell_size,
                              self.offset_y + self.cell_manager.grid_height * self.cell_size),
                             line_thickness)

    def update_posicion(self,x,y):
        self.offset_x = x
        self.offset_y = y
