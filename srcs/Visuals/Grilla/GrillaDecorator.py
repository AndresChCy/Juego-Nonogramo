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
        hor, ver = self._component.getTablero().getCompresiones()
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
                cant = clue[0]
                color = clue[1]
                self.draw_clue(cant, offset_x - (len(clues) - clue_idx) * cell_size,
                               offset_y + row_idx * cell_size,cell_size,color)

    def draw_vertical_clues(self,vertical_clues):
        """
        Dibuja las pistas verticales en la pantalla.
        """
        cell_size = self._component.getCellSize()
        offset_x, offset_y = self._component.getOffsets()
        #vertical_clues = self.clue_generator.generate_vertical_clues()
        for col_idx, clues in enumerate(vertical_clues):
            for clue_idx, clue in enumerate(clues):
                cant = clue[0]
                color = clue[1]
                self.draw_clue(cant, offset_x + col_idx * cell_size,
                               offset_y - (len(clues) - clue_idx) * cell_size,cell_size,color)

    def draw_clue(self, clue, x, y,cell_size,color):
        """
        Dibuja una pista en la pantalla.

        Args:
            clue (int): El valor de la pista.
            x (int): La posición x donde se dibujará la pista.
            y (int): La posición y donde se dibujará la pista.
        """
        if color == 1:
            cell_color = (200,200,200)
        else:
            cell_color = Colores.get_number_mapping().get(color,(100,100,100))
        font = pygame.font.SysFont(None, cell_size // 2)
        rect = pygame.Rect(x, y, cell_size,cell_size)
        pygame.draw.rect(self._component.getScreen(), cell_color, rect)
        text_surface = font.render(str(clue), True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=rect.center)
        self._component.getScreen().blit(text_surface, text_rect)

class DecoratorMiniatureRender(DecoratorGrilla):
    """
    Inicializa la miniatura.

    Args:
        screen (pygame.Surface): La superficie de la pantalla donde se dibujará la miniatura.
        grid_logic (list of list of int): La lógica actual de la cuadrícula.
        offset_x (int): El desplazamiento en el eje x.
        offset_y (int): El desplazamiento en el eje y.
        cell_manager (CellManager): El administrador de celdas.
    """
    def __init__(self, component: GrillaRender ) -> None:
        self._component = component
        self.grid_logic = self._component.getTablero().getProgreso()
        self.screen = self._component.getScreen()
        height, width = self._component.getGridDimensions()
        offset_x , offset_y = self._component.getOffsets()
        self.miniature_size = min(125 // width, 125 // height)
        self.miniature_offset_x = offset_x - (width * self.miniature_size) - 5
        self.miniature_offset_y = offset_y - (height * self.miniature_size) - 5
        self.color_mapping = Colores.get_number_mapping()  # Mapeo de colores

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
                cell_value = self.grid_logic[row][col]
                color = self.color_mapping.get(cell_value, Colores.WHITE.value)  # Usa blanco como predeterminado
                pygame.draw.rect(self.screen, color,
                                 (self.miniature_offset_x + col * self.miniature_size,
                                  self.miniature_offset_y + row * self.miniature_size,
                                  self.miniature_size, self.miniature_size))