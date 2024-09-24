import pygame
import sys

WEIGHT = 1600
HEIGHT = 900

class Ventana:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WEIGHT, HEIGHT))
        pygame.display.set_caption('Monogram')

    def execute(self):
        running = True
        while running:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    running = False
            self.screen.fill((255, 255, 255))
            pygame.display.flip()
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    ventana = Ventana()
    ventana.execute()