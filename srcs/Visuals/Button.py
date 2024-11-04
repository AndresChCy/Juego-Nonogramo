import pygame

class Button:
    def __init__(self, screen, text, width, height, x, y, color, text_color, callback, image_path=None):
        self.screen = screen
        self.text = text
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color
        self.text_color = text_color
        self.callback = callback
        self.font = pygame.font.Font(None, 36)
        self.image = pygame.image.load(image_path) if image_path else None

    def draw(self):
        if self.image:
            self.screen.blit(self.image, (self.x, self.y))
        else:
            pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        self.screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height

    def click(self):
        if self.callback:
            self.callback()