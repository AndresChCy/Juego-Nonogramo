import pygame
import sys
from Grid import Grid
from Colores import Colores

class Window:
    def __init__(self, matrix):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 900))
        pygame.display.set_caption('Nonograma')
        self.cuadricula = Grid(self.screen, matrix)

    def execute(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.cuadricula.handle_click(event.pos, event.button)
                elif event.type == pygame.MOUSEMOTION:
                    self.cuadricula.renderer.handle_mouse_motion(event.pos)
            self.screen.fill(Colores.WHITE.value)
            self.cuadricula.draw()
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
      [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    Window(matrix).execute()