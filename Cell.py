import pygame

class Cell(pygame.sprite.Sprite):
    WHITE = (255, 255, 255)
    FILLED_COLOR = (0, 128, 255)

    def __init__(self, x, y, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(self.WHITE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.filled = False

    def fill(self):
        self.filled = True
        self.image.fill(self.FILLED_COLOR)

    def empty(self):
        self.filled = False
        self.image.fill(self.WHITE)