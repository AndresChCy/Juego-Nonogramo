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
        self.marked = False

    def fill(self):
        self.filled = True
        self.marked = False
        self.image.fill(Colores.DARK_GREY.value)

    def empty(self):
        self.filled = False
        self.marked = False
        self.image.fill(Colores.WHITE.value)

    def mark(self):
        self.marked = True
        self.filled = False
        self.image.fill(Colores.WHITE.value)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
        if self.filled:
            pygame.draw.rect(screen, Colores.DARK_GREY.value, self.rect)
        elif self.marked:
            pygame.draw.line(screen, Colores.RED.value, self.rect.topleft, self.rect.bottomright, 4)
            pygame.draw.line(screen, Colores.RED.value, self.rect.topright, self.rect.bottomleft, 4)
        else:
            pygame.draw.rect(screen, Colores.WHITE.value, self.rect)