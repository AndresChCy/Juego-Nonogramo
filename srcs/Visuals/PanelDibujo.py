import sys

import pygame
from pygame.locals import *

from Colores import Colores
from CellManager import CellManager
from ClueGenerator import ClueGenerator
from CluesRenderer import CluesRenderer
from Dibujo import Dibujo
from GridLinesRenderer import GridLinesRenderer
from GridRenderer import GridRenderer
from MiniatureRenderer import MiniatureRenderer
from Panel import Panel
from ProxyPanel import ProxyPanel
from Tablero import Tablero


class panelDibujo(Panel):
    """
    Clase que representa la cuadrícula del juego.
    Es responsable de la lógica de la cuadrícula, la visualización y la interacción del usuario.

    Atributos:
    ----------
    GRID_WIDTH_PX : int
    Ancho máximo de la cuadrícula en píxeles.
    GRID_HEIGHT_PX : int
        Alto máximo de la cuadrícula en píxeles.
    screen : pygame.Surface
        La pantalla o ventana donde se dibuja la cuadrícula.
    GRID_WIDTH : int
        Número de columnas en la cuadrícula (basado en la matriz dada).
    GRID_HEIGHT : int
        Número de filas en la cuadrícula (basado en la matriz dada).
    window_width : int
        Ancho de la ventana del juego.
    window_height : int
        Alto de la ventana del juego.
    CELL_SIZE : int
        Tamaño de cada celda en píxeles.
    actual_grid_width_px : int
        Ancho real de la cuadrícula en píxeles (ajustado para centrado).
    actual_grid_height_px : int
        Alto real de la cuadrícula en píxeles (ajustado para centrado).
    offset_x : int
        Desplazamiento en el eje X para centrar la cuadrícula.
    offset_y : int
        Desplazamiento en el eje Y para centrar la cuadrícula.
    grid_logic : list[list[int]]
        Representa la lógica interna de la cuadrícula donde cada celda puede estar vacía (0), marcada (1) o con una equis roja (-1).
    cell_manager : CellManager
        Instancia que gestiona las celdas de la cuadrícula.
    clue_generator : ClueGenerator
        Genera las pistas para las filas y columnas basadas en la matriz.
    renderer : GridRenderer
        Se encarga de dibujar la cuadrícula y las pistas en la pantalla.
    clock : pygame.time.Clock
        Reloj interno para controlar los FPS del juego.
    FPS : int
        Velocidad de actualización de la pantalla en fotogramas por segundo.
    """
    GRID_WIDTH_PX = 300
    GRID_HEIGHT_PX = 300

    def __init__(self, screen, x,y, proxy: ProxyPanel):
        """
        Inicializa la cuadrícula.

        Args:
            screen (pygame.Surface): La superficie de la pantalla donde se dibujará la cuadrícula.
            matrix (list of list of int): La matriz de que contiene la solución del Nonograma.
        """
        pygame.init()
        self.proxy = proxy
        self.screen = screen
        self.dibujo = Dibujo(y, x)
        self.GRID_WIDTH = len(self.dibujo.getMatriz()[0])
        self.GRID_HEIGHT = len(self.dibujo.getMatriz())
        self.window_width, self.window_height = screen.get_size()
        self.CELL_SIZE = min(self.GRID_WIDTH_PX // self.GRID_WIDTH, self.GRID_HEIGHT_PX // self.GRID_HEIGHT)
        self.actual_grid_width_px = self.GRID_WIDTH* self.CELL_SIZE
        self.actual_grid_height_px = self.GRID_HEIGHT * self.CELL_SIZE
        self.offset_x = (self.window_width - self.actual_grid_width_px) // 2
        self.offset_y = (self.window_height - self.actual_grid_height_px) // 2
        self.cell_manager = CellManager(self.GRID_WIDTH, self.GRID_HEIGHT, self.CELL_SIZE, self.offset_x, self.offset_y)
        self.renderer = dibujoRenderer(self.screen, self.cell_manager, self.dibujo.getMatriz(),
                                     self.offset_x, self.offset_y, self.CELL_SIZE)
        self.clock = pygame.time.Clock()
        self.FPS = 60

    def handle_click(self, pos, button):
        """
        Maneja los eventos de clic del ratón.

        Args:
            pos (tuple of int): La posición (x, y) del clic del ratón.
            button (int): El botón del ratón que se ha pulsado (1 para clic izquierdo, 3 para clic derecho).
        """
        mouse_x, mouse_y = pos
        col = (mouse_x - self.offset_x) // self.CELL_SIZE
        row = (mouse_y - self.offset_y) // self.CELL_SIZE
        if 0 <= col < self.GRID_WIDTH and 0 <= row < self.GRID_HEIGHT:
            if button == 1:  # Clic izquierdo
                self.dibujo.pintar(row,col,1) if self.dibujo.getMatriz()[row][col] != 1 else self.dibujo.pintar(row,col,0)
            elif button == 3:  # Clic derecho
                self.dibujo.pintar(row,col,1) if self.dibujo.getMatriz()[row][col] != 1 else self.dibujo.pintar(row,col,0)
            self.cell_manager.update_grid_visual(self.dibujo.getMatriz())


    def draw(self):
        """
        Dibuja la cuadrícula y actualiza la pantalla.
        """
        self.renderer.draw()
        self.clock.tick(self.FPS)

    def handle_key(self, event):
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        elif event.key == pygame.K_RETURN:
            tab = Tablero(self.dibujo)
            tab.guardarProgreso(self.dibujo.getMatriz(),"Niveles/nivel1")
            self.proxy.cambiarTarget(0)

    def handle_mouse_motion(self ,pos):
        self.renderer.handle_mouse_motion(pos)

    def get_grid_logic(self):
        """
        Obtiene el estado actual de la cuadrícula.

        Returns:
            list of list of int: El estado actual de la cuadrícula.
        """
        return self.grid_logic

class dibujoRenderer:
    def __init__(self, screen, cell_manager, grid_logic, offset_x, offset_y, cell_size):
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
        self.grid_logic = grid_logic
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.cell_size = cell_size
        self.grid_lines_renderer = GridLinesRenderer(screen, cell_manager, offset_x, offset_y, cell_size)
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
