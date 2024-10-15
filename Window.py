import pygame
import sys
from Grid import Grid
from Colores import Colores
from Menu import MenuPrincipal
from MenuNiveles import MenuNiveles
from ProxyPanel import ProxyPanel


class Window:
    def __init__(self, matrix):
        pygame.init()
        self.screen = pygame.display.set_mode((900, 600))
        pygame.display.set_caption('Nonograma')
        self.panel = ProxyPanel([])
        cuadricula = Grid(self.screen, matrix)
        menu = MenuPrincipal(self.screen,self.panel)
        menuNiveles = MenuNiveles(self.screen,[1,2,3,4,5,6,7,8,9],self.panel)
        self.panel.addToList(menu)
        self.panel.addToList(menuNiveles)
        self.panel.addToList(cuadricula)

    def execute(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
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