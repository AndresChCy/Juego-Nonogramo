import pygame
import sys
from Grid import Grid
from Colores import Colores
from Menu import MenuPrincipal
from MenuNiveles import MenuNiveles
from ProxyPanel import ProxyPanel
from srcs.Logica.Niveles import Niveles
from srcs.Visuals.MenuDificultad import MenuDificultad
from srcs.Visuals.SeleccionTipoNivel import SeleccionTipoNivel
from ImageManager import ImageManager


class Window:
    def __init__(self, matrix):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 700))
        pygame.display.set_caption('Nonograma')
        self.panel = ProxyPanel([])

        # cuadricula = Grid(self.screen, matrix,self.panel)
        niveles = Niveles()
        # niveles.GuardarNivelesCreados()
        # niveles.GuardarNivelesPredeterminados()
        niveles.CargarNivelesCreados()
        niveles.CargarNivelesPredeterminados()
        menu = MenuPrincipal(self.screen, self.panel)
        # menuTipos = SeleccionTipoNivel(self.screen, self.panel)
        self.panel.addToList(menu)
        # self.panel.addToList(cuadricula)

    def execute(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    niveles = Niveles()
                    niveles.GuardarNivelesCreados()
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.panel.handle_click(event.pos, event.button)
                elif event.type == pygame.MOUSEMOTION:
                    self.panel.handle_mouse_motion(event.pos)
                elif event.type == pygame.KEYDOWN:
                    self.panel.handle_key(event)
            self.screen.fill(Colores.WHITE.value)
            self.panel.draw()
            pygame.display.flip()
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    matrix = [
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
      [1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    Window(matrix).execute()