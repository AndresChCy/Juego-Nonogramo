import pygame

from srcs.Visuals.Colores import Colores
from srcs.Visuals.Grilla.GrillaVisual import GrillaVisual, GrillaRender
from srcs.Visuals.Panel import Panel


class DecoratorGrilla(GrillaRender):

    def __init__(self, component: GrillaRender) -> None:
        self._component = component

    @property
    def component(self) -> Panel:
        return self._component

    def draw(self):
        self._component.draw()

    def handle_mouse_motion(self, event):
        self._component.handle_mouse_motion(event)

    def handle_click(self, pos, button):
        self._component.handle_click( pos, button)

    def handle_key(self, event):
        self._component.handle_key(event)

    def getScreen(self):
        return self._component.getScreen()

    def getOffsets(self):
        return self._component.getOffsets()

    def getCellSize(self):
        return self._component.getCellSize()

    def getTablero(self):
        return self._component.getTablero()

    def getGridDimensions(self):
        return self._component.getGridDimensions()

class DecoratorClues(DecoratorGrilla):

    def draw(self):
        super().draw()
        self.draw_clues()

    def draw_clues(self):
        hor, ver = self._component.getTablero().Compresion()
        self.draw_horizontal_clues(hor)
        self.draw_vertical_clues(ver)

    def draw_horizontal_clues(self,horizontal_clues):
        """
        Dibuja las pistas horizontales en la pantalla.
        """
        cell_size = self._component.getCellSize()
        offset_x, offset_y = self._component.getOffsets()
        #horizontal_clues = self.clue_generator.generate_horizontal_clues()
        for row_idx, clues in enumerate(horizontal_clues):
            for clue_idx, clue in enumerate(clues):
                self.draw_clue(clue, offset_x - (len(clues) - clue_idx) * cell_size,
                               offset_y + row_idx * cell_size,cell_size)

    def draw_vertical_clues(self,vertical_clues):
        """
        Dibuja las pistas verticales en la pantalla.
        """
        cell_size = self._component.getCellSize()
        offset_x, offset_y = self._component.getOffsets()
        #vertical_clues = self.clue_generator.generate_vertical_clues()
        for col_idx, clues in enumerate(vertical_clues):
            for clue_idx, clue in enumerate(clues):
                self.draw_clue(clue, offset_x + col_idx * cell_size,
                               offset_y - (len(clues) - clue_idx) * cell_size,cell_size)

    def draw_clue(self, clue, x, y,cell_size):
        """
        Dibuja una pista en la pantalla.

        Args:
            clue (int): El valor de la pista.
            x (int): La posición x donde se dibujará la pista.
            y (int): La posición y donde se dibujará la pista.
        """
        font = pygame.font.SysFont(None, cell_size // 2)
        rect = pygame.Rect(x, y, cell_size,cell_size)
        pygame.draw.rect(self._component.getScreen(), (200, 200, 200), rect)
        text_surface = font.render(str(clue), True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=rect.center)
        self._component.getScreen().blit(text_surface, text_rect)

class DecoratorMiniatureRender(DecoratorGrilla):
    def __init__(self, component: GrillaRender ) -> None:
        self._component = component
        self.grid_logic = self._component.getTablero().getProgreso()
        self.screen = self._component.getScreen()
        height, width = self._component.getGridDimensions()
        offset_x , offset_y = self._component.getOffsets()
        self.miniature_size = min(125 // width, 125 // height)
        self.miniature_offset_x = offset_x - (width * self.miniature_size) - 5
        self.miniature_offset_y = offset_y - (height * self.miniature_size) - 5

    def draw(self):
        super().draw()
        self.draw_miniature()

    def draw_miniature(self):
        """
        Dibuja la miniatura de la cuadrícula en la pantalla.
        """
        #self.grid_logic = self._component.getTablero().getProgreso()

        for row in range(len(self.grid_logic)):
            for col in range(len(self.grid_logic[row])):
                color = Colores.BLACK.value if self.grid_logic[row][col] == 1 else Colores.WHITE.value
                pygame.draw.rect(self.screen, color,
                                 (self.miniature_offset_x + col * self.miniature_size,
                                  self.miniature_offset_y + row * self.miniature_size,
                                  self.miniature_size, self.miniature_size))