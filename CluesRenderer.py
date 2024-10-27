import pygame

from Tablero import Tablero


class CluesRenderer:
    def __init__(self, screen, tablero: Tablero, offset_x, offset_y, cell_size):
        """
        Inicializa los gráficos de las pistas.

        Args:
            screen (pygame.Surface): La superficie de la pantalla donde se dibujarán las pistas.
            clue_generator (ClueGenerator): El generador de pistas.
            offset_x (int): El desplazamiento en el eje x.
            offset_y (int): El desplazamiento en el eje y.
            cell_size (int): El tamaño de cada celda.
        """
        self.screen = screen
        self.horizontal_clues,self.vertical_clues = tablero.Compresion()
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.cell_size = cell_size
        self.font = pygame.font.SysFont(None, self.cell_size // 2)

    def draw_horizontal_clues(self):
        """
        Dibuja las pistas horizontales en la pantalla.
        """
        #horizontal_clues = self.clue_generator.generate_horizontal_clues()
        for row_idx, clues in enumerate(self.horizontal_clues):
            for clue_idx, clue in enumerate(clues):
                self.draw_clue(clue, self.offset_x - (len(clues) - clue_idx) * self.cell_size,
                               self.offset_y + row_idx * self.cell_size)

    def draw_vertical_clues(self):
        """
        Dibuja las pistas verticales en la pantalla.
        """
        #vertical_clues = self.clue_generator.generate_vertical_clues()
        for col_idx, clues in enumerate(self.vertical_clues):
            for clue_idx, clue in enumerate(clues):
                self.draw_clue(clue, self.offset_x + col_idx * self.cell_size,
                               self.offset_y - (len(clues) - clue_idx) * self.cell_size)

    def draw_clue(self, clue, x, y):
        """
        Dibuja una pista en la pantalla.

        Args:
            clue (int): El valor de la pista.
            x (int): La posición x donde se dibujará la pista.
            y (int): La posición y donde se dibujará la pista.
        """
        rect = pygame.Rect(x, y, self.cell_size, self.cell_size)
        pygame.draw.rect(self.screen, (200, 200, 200), rect)
        text_surface = self.font.render(str(clue), True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect)

    def draw_clue_borders(self):
        """
        Dibuja los bordes de las pistas en la pantalla.
        """
        pass
