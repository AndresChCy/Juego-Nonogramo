import pygame

class SoundBar:
    def __init__(self, screen, x, y, width, height, max_value=100):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max_value = max_value
        self.current_value = 0

    def update(self, value):
        self.current_value = max(0, min(self.max_value, value))

    def draw(self):
        pygame.draw.rect(self.screen, (50, 50, 50), (self.x, self.y, self.width, self.height))
        fill_width = (self.current_value / self.max_value) * self.width
        pygame.draw.rect(self.screen, (0, 255, 0), (self.x, self.y, fill_width, self.height))
        pygame.draw.rect(self.screen, (0, 0, 0), (self.x, self.y, self.width, self.height), 3)