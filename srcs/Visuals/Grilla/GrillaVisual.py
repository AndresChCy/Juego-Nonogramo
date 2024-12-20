import sys

import pygame


from pygame.rect import Rect
from pygame.constants import KEYDOWN, K_ESCAPE, FULLSCREEN

from Musica.SoundManager import SoundManager
from srcs.Comandos.Command import Command
from srcs.Comandos.CommandCambiarPanel import CommandReturnInicio
from srcs.Logica.Dibujo import Pintable
from srcs.Logica.Niveles import Niveles
from srcs.Visuals.Barra import Slider
from srcs.Visuals.Button import Button
from srcs.Visuals.Grilla.CellManager import CellManager
from srcs.Visuals.Colores import Colores
from srcs.Visuals.Grilla.GridLinesRenderer import GridLinesRenderer
from srcs.Logica.Tablero import Tablero
from srcs.Visuals.ImageManager import ImageManager
from srcs.Visuals.NonogramPanel import NonogramPanel
from srcs.Visuals.Panel import Panel
from srcs.Visuals.ProxyPanel import ProxyPanel
from srcs.Visuals.VictoryRenderer import VictoryRenderer
from abc import ABC , abstractmethod




class GrillaRender(Panel,ABC):
    @abstractmethod
    def getScreen(self):
        pass

    @abstractmethod
    def getOffsets(self):
        pass

    @abstractmethod
    def getCellSize(self):
        pass

    @abstractmethod
    def getTablero(self):
        pass

    @abstractmethod
    def getGridDimensions(self):
        pass

    @abstractmethod
    def getPanelOpciones(self):
        pass

    @abstractmethod
    def getBarras(self):
        pass

class GrillaVisual(GrillaRender):

    GRID_WIDTH_PX = 440
    GRID_HEIGHT_PX = 440


    def __init__(self, screen, tablero: Pintable, proxy:ProxyPanel, enter: Command = None, dibujo: bool = False):
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
        self.proxy = proxy
        super().__init__(screen)
        self.tablero = tablero
        self.soundManager =SoundManager()
        self.right_click_value = -1
        self.left_click_value = 1
        self.enter = enter

        self.GRID_WIDTH = len(tablero.getProgreso()[0])
        self.GRID_HEIGHT = len(tablero.getProgreso())
        window_width, window_height = screen.get_size()
        self.cell_size = min(self.GRID_WIDTH_PX // self.GRID_WIDTH, self.GRID_HEIGHT_PX // self.GRID_HEIGHT)
        self.cell_size = max(self.cell_size,25)
        actual_grid_width_px = self.GRID_WIDTH * self.cell_size
        actual_grid_height_px = self.GRID_HEIGHT * self.cell_size
        self.offset_x = (window_width - actual_grid_width_px) // 2 +20
        self.offset_y = (window_height - actual_grid_height_px) // 2 + 40

        self.cell_manager = CellManager(self.GRID_WIDTH, self.GRID_HEIGHT,self.cell_size, self.offset_x, self.offset_y,self)
        self.grid_lines_renderer = GridLinesRenderer(screen, self.cell_manager, self.offset_x, self.offset_y,self.cell_size)
        self.hovered_row = None
        self.hovered_col = None
        if self.tablero.__class__ == Tablero :
            self.nonogram_panel = NonogramPanel(screen, int(window_width * 0.2), window_height, self ,colores_extra=list(tablero.getColors()))
        else:
            self.nonogram_panel = NonogramPanel(screen, int(window_width * 0.2), window_height, self ,dibujo=dibujo)


        self.barraVer = Slider(window_width - int(window_width * 0.2) -20, 150, 20, 400, -500, 1000, self.offset_y, self.screen)
        self.barraHor = Slider(window_width - int(window_width * 0.25)-810, window_height-20, 800, 20, -500, 1000, self.offset_x, self.screen,ver = False)
        self.rect = Rect(self.offset_x,self.offset_y,actual_grid_width_px,actual_grid_height_px)

        self.image_manager = ImageManager()
        self.image_manager.load_image("background", "Img/nonogram_back.jpg",screen.get_size())
        # Cargar la imagen de fondo usando el ImageManager
        self.background_image = self.image_manager.get_image("background")
        self.botonVolver = Button(self.screen, 210, 50, 50, 50, Colores.BLUE.value, enter
                                  , Colores.WHITE.value, "Volver y Guardar")


    def handle_mouse_motion(self, pos):
        """
        Maneja el movimiento del ratón.

        Args:
            pos (tuple of int): La posición (x, y) del ratón.
        """
        mouse_x, mouse_y = pos
        col = (mouse_x - self.offset_x) // self.cell_size
        row = (mouse_y - self.offset_y) // self.cell_size
        if 0 <= col < self.GRID_WIDTH and 0 <= row < self.GRID_HEIGHT:
            self.hovered_row = int(row)
            self.hovered_col = int(col)
        else:
            self.hovered_row = None
            self.hovered_col = None
        self.barraVer.handle_mouse_motion(pos)
        self.barraHor.handle_mouse_motion(pos)

    def handle_click(self, pos, button):
        """
        Maneja los clics del ratón.

        Args:
            pos (tuple of int): La posición (x, y) del clic del ratón.
            button (int): El botón del ratón que se ha pulsado (1 para clic izquierdo, 3 para clic derecho).
        """
        self.barraVer.handle_click(pos, button)
        self.barraHor.handle_click(pos,button)
        mouse_x, mouse_y = pos
        col = int((mouse_x - self.offset_x) // self.cell_size)
        row = int((mouse_y - self.offset_y) // self.cell_size)
        self.nonogram_panel.handle_click(pos, button)
        if 0 <= col < self.GRID_WIDTH and 0 <= row < self.GRID_HEIGHT:
            if button == 1:  # Clic izquierdo
                self.tablero.pintar(row,col,self.left_click_value) if self.tablero.getProgreso()[row][col] != self.left_click_value else self.tablero.pintar(row,col,0)
                self.soundManager.play_sound("pintar")

            elif button == 3:  # Clic derecho
                self.tablero.pintar(row,col,self.right_click_value) if self.tablero.getProgreso()[row][col] != self.right_click_value else self.tablero.pintar(row,col,0)
            #self.cell_manager.update_grid_visual(self.tablero.getProgreso())
            if self.tablero.__class__ == Tablero:
                if self.tablero.CompararDibujos():
                    self.proxy.ponerTarget(VictoryRenderer(self.screen, self.proxy, self.tablero.getProgreso(), self.cell_manager))
                    self.tablero.reiniciar()
        if self.botonVolver.is_clicked(pos):
            self.botonVolver.click()


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
        self.screen.blit(self.background_image, (0, 0))
        offset_y = self.barraVer.get_value()
        offset_x = self.barraHor.get_value()
        if self.offset_y != offset_y or self.offset_x != offset_x:
            self.offset_x = offset_x
            self.offset_y = offset_y
            self.cell_manager.update_posicion(self.offset_x,self.offset_y)
            self.grid_lines_renderer.update_posicion(self.offset_x,self.offset_y)

        #self.screen.blit(self.background_image, (0, 0))

        self.cell_manager.update_grid_visual(self.tablero.getProgreso())
        self.cell_manager.draw_cells(self.screen)
        self.draw_hover_effect()
        self.grid_lines_renderer.draw_grid_lines()
        self.nonogram_panel.draw()

        self.barraVer.draw()
        self.barraHor.draw()

        #self.rect.topleft = (100,-offset_y)

        self.botonVolver.draw()

        #self.clues_renderer.draw_horizontal_clues()
       # self.clues_renderer.draw_vertical_clues()
       # self.clues_renderer.draw_clue_borders()
       # self.miniature_renderer.draw_miniature()

    def handle_key(self, event):
        if event.type == KEYDOWN and event.key == K_ESCAPE:

            niveles = Niveles()
            niveles.GuardarNivelesCreados()
            niveles.GuardarNivelesPredeterminados()
            CommandReturnInicio(self.proxy,self.screen).execute()
        elif event.key == pygame.K_RETURN:
            if self.enter != None:
                self.enter.execute()
        self.nonogram_panel.handle_key(event)

    def handle_clickUp(self, event):
        self.barraVer.handle_clickUp(event)
        self.barraHor.handle_clickUp(event)

    def draw_hover_effect(self):
        """
        Dibuja el efecto de resaltar la celda sobre la que se encuentra el ratón.
        """
        if self.hovered_row is not None and self.hovered_col is not None:
            for col in range(self.GRID_WIDTH):
                if self.tablero.getProgreso()[self.hovered_row][col] == 0:
                    pygame.draw.rect(self.screen, Colores.WHITE_SMOKE.value,
                                     (self.offset_x + col * self.cell_size, self.offset_y + self.hovered_row * self.cell_size,
                                      self.cell_size, self.cell_size))
            for row in range(self.GRID_HEIGHT):
                if self.tablero.getProgreso()[row][self.hovered_col] == 0:
                    pygame.draw.rect(self.screen, Colores.WHITE_SMOKE.value,
                                     (self.offset_x + self.hovered_col * self.cell_size, self.offset_y + row * self.cell_size,
                                      self.cell_size, self.cell_size))

    def pista(self):
        self.tablero.pista()
        if (self.tablero.CompararDibujos()):

            self.proxy.ponerTarget(VictoryRenderer(self.screen, self.proxy, self.tablero.getProgreso(), self.cell_manager))
            self.tablero.reiniciar()

    def getScreen(self):
        return self.screen
    def getOffsets(self):
        return self.offset_x,self.offset_y
    def getCellSize(self):
        return self.cell_size
    def getTablero(self):
        return self.tablero
    def getGridDimensions(self):
        return self.GRID_HEIGHT,self.GRID_WIDTH
    def getPanelOpciones(self):
        return self.nonogram_panel

    def getBarras(self):
        return self.barraHor,self.barraVer
