import pygame
from CellManager import CellManager
from ClueGenerator import ClueGenerator
from GridRenderer import GridRenderer
from Panel import Panel


class Grid(Panel):
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

    def __init__(self, screen, matrix):
        """
        Inicializa la cuadrícula.

        Args:
            screen (pygame.Surface): La superficie de la pantalla donde se dibujará la cuadrícula.
            matrix (list of list of int): La matriz de que contiene la solución del Nonograma.
        """
        pygame.init()
        self.screen = screen
        self.GRID_WIDTH = len(matrix[0])
        self.GRID_HEIGHT = len(matrix)
        self.window_width, self.window_height = screen.get_size()
        self.CELL_SIZE = min(self.GRID_WIDTH_PX // self.GRID_WIDTH, self.GRID_HEIGHT_PX // self.GRID_HEIGHT)
        self.actual_grid_width_px = self.GRID_WIDTH * self.CELL_SIZE
        self.actual_grid_height_px = self.GRID_HEIGHT * self.CELL_SIZE
        self.offset_x = (self.window_width - self.actual_grid_width_px) // 2
        self.offset_y = (self.window_height - self.actual_grid_height_px) // 2
        self.grid_logic = [[0 for _ in range(self.GRID_WIDTH)] for _ in range(self.GRID_HEIGHT)]
        self.cell_manager = CellManager(self.GRID_WIDTH, self.GRID_HEIGHT, self.CELL_SIZE, self.offset_x, self.offset_y)
        self.clue_generator = ClueGenerator(matrix)
        self.renderer = GridRenderer(self.screen, self.cell_manager, self.clue_generator, self.grid_logic,
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
                self.grid_logic[row][col] = 1 if self.grid_logic[row][col] != 1 else 0
            elif button == 3:  # Clic derecho
                self.grid_logic[row][col] = -1 if self.grid_logic[row][col] != -1 else 0
            self.cell_manager.update_grid_visual(self.grid_logic)

    def draw(self):
        """
        Dibuja la cuadrícula y actualiza la pantalla.
        """
        self.renderer.draw()
        self.clock.tick(self.FPS)

    def handle_key(self, event):
        pass

    def handle_mouse_motion(self ,pos):
        self.renderer.handle_mouse_motion(pos)

    def get_grid_logic(self):
        """
        Obtiene el estado actual de la cuadrícula.

        Returns:
            list of list of int: El estado actual de la cuadrícula.
        """
        return self.grid_logic
