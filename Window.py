import pygame
import sys
from Grid import Grid

WIDTH = 1600
HEIGHT = 900

class Window:
    def __init__(self, grid_width=10, grid_height=10):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Nonograma')
        self.cuadricula = Grid(self.screen, grid_width, grid_height)

    def execute(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.cuadricula.handle_click(event.pos)
            self.screen.fill((255, 255, 255))
            self.cuadricula.draw()
            pygame.display.flip()
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    ventana = Window(grid_width=25, grid_height=15) # Se puede cambiar el tamaño de la cuadricula
    ventana.execute()