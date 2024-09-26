import pygame
from Colores import Colores

class Cell(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(Colores.WHITE.value)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.filled = False

    def fill(self):
        self.filled = True
        self.image.fill(Colores.BLACK.value)

    def empty(self):
        self.filled = False
        self.image.fill(Colores.WHITE.value)