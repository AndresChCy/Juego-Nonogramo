import pygame
from srcs.Visuals.Colores import Colores
from srcs.Visuals.GridLinesRenderer import GridLinesRenderer
from srcs.Visuals.CluesRenderer import CluesRenderer
from MiniatureRenderer import MiniatureRenderer
from srcs.Logica.Tablero import Tablero


class GridRenderer:
    def __init__(self, screen, cell_manager, clue_generator, tablero: Tablero, offset_x, offset_y, cell_size):
        """
        Inicializa los componentes gráficos de la cuadrícula.

        Args:
            screen (pygame.Surface): La superficie de la pantalla donde se dibujará la cuadrícula.
            cell_manager (CellManager): El administrador de celdas.
            clue_generator (ClueGenerator): El generador de pistas.
            grid_logic (list of list of int): La lógica actual de la cuadrícula.
            offset_x (int): El desplazamiento en el eje x.
            offset_y (int): El desplazamiento en el eje y.
            cell_size (int): El tamaño de cada celda.
        """
        self.screen = screen
        self.cell_manager = cell_manager
        self.clue_generator = clue_generator
        self.grid_logic = tablero.getProgreso()
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.cell_size = cell_size
        self.grid_lines_renderer = GridLinesRenderer(screen, cell_manager, offset_x, offset_y, cell_size)
        self.clues_renderer = CluesRenderer(screen, tablero, offset_x, offset_y, cell_size)
        self.miniature_renderer = MiniatureRenderer(screen, self.grid_logic, offset_x, offset_y, cell_manager)
        self.hovered_row = None
        self.hovered_col = None

    def handle_mouse_motion(self, pos):
        """
        Maneja el movimiento del ratón.

        Args:
            pos (tuple of int): La posición (x, y) del ratón.
        """
        mouse_x, mouse_y = pos
        col = (mouse_x - self.offset_x) // self.cell_size
        row = (mouse_y - self.offset_y) // self.cell_size
        if 0 <= col < len(self.grid_logic[0]) and 0 <= row < len(self.grid_logic):
            self.hovered_row = row
            self.hovered_col = col
        else:
            self.hovered_row = None
            self.hovered_col = None

    def handle_mouse_click(self, pos, button):
        """
        Maneja los clics del ratón.

        Args:
            pos (tuple of int): La posición (x, y) del clic del ratón.
            button (int): El botón del ratón que se ha pulsado (1 para clic izquierdo, 3 para clic derecho).
        """
        mouse_x, mouse_y = pos
        col = (mouse_x - self.offset_x) // self.cell_size
        row = (mouse_y - self.offset_y) // self.cell_size
        if 0 <= col < len(self.grid_logic[0]) and 0 <= row < len(self.grid_logic):
            if button == 1:  # Clic izquierdo
                self.grid_logic[row][col] = 1
            elif button == 3:  # Clic derecho
                self.grid_logic[row][col] = -1
            self.cell_manager.update_grid_visual(self.grid_logic)
        print(self.clues_renderer.vertical_clues)

    def handle_mouse_events(self, event):
        """
        Maneja los eventos del ratón.

        Args:
            event (pygame.event.Event): El evento del ratón.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.handle_mouse_click(event.pos, event.button)

    def draw(self):
        """
        Dibuja la cuadrícula y sus componentes en la pantalla.
        """
        self.cell_manager.draw_cells(self.screen)
        self.draw_hover_effect()
        self.grid_lines_renderer.draw_grid_lines()
        self.clues_renderer.draw_horizontal_clues()
        self.clues_renderer.draw_vertical_clues()
        self.clues_renderer.draw_clue_borders()
        self.miniature_renderer.draw_miniature()

    def draw_hover_effect(self):
        """
        Dibuja el efecto de resaltar la celda sobre la que se encuentra el ratón.
        """
        if self.hovered_row is not None and self.hovered_col is not None:
            for col in range(len(self.grid_logic[0])):
                if self.grid_logic[self.hovered_row][col] == 0:
                    pygame.draw.rect(self.screen, Colores.WHITE_SMOKE.value,
                                     (self.offset_x + col * self.cell_size, self.offset_y + self.hovered_row * self.cell_size,
                                      self.cell_size, self.cell_size))
            for row in range(len(self.grid_logic)):
                if self.grid_logic[row][self.hovered_col] == 0:
                    pygame.draw.rect(self.screen, Colores.WHITE_SMOKE.value,
                                     (self.offset_x + self.hovered_col * self.cell_size, self.offset_y + row * self.cell_size,
                                      self.cell_size, self.cell_size))
            self.clues_renderer.draw_horizontal_clues()
            self.clues_renderer.draw_vertical_clues()