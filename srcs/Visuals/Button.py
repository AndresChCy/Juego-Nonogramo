import pygame
from srcs.Visuals.Colores import Colores

class Button:
    def __init__(self, screen, width, height, x, y, color, text_color, callback, text="", image_path=None, draw_rectangle=False,draw_cross=False, draw_point=False, opacity=255):
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
        self.image = None
        if image_path:
            try:
                self.image = pygame.image.load(image_path)
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
                self.image.set_alpha(opacity)
            except pygame.error as e:
                print(f"Error loading image at {image_path}: {e}")
        self.draw_rectangle = draw_rectangle
        self.draw_cross = draw_cross
        self.draw_point = draw_point
        self.opacity = opacity

    def draw(self):
        if self.image:
            self.screen.blit(self.image, (self.x, self.y))
        else:
            surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            surface.fill((*self.color, self.opacity))
            self.screen.blit(surface, (self.x, self.y))
        if self.draw_rectangle:
            margin = 7
            inner_rect = pygame.Rect(self.x + margin, self.y + margin, self.width - 2 * margin, self.height - 2 * margin)
            pygame.draw.rect(self.screen, Colores.BLACK.value, inner_rect)
        if self.draw_cross:
            pygame.draw.line(self.screen, Colores.RED.value, (self.x, self.y), (self.x + self.width, self.y + self.height), 4)
            pygame.draw.line(self.screen, Colores.RED.value, (self.x + self.width, self.y), (self.x, self.y + self.height), 4)
        if self.draw_point:
            pygame.draw.circle(self.screen, Colores.BLACK.value, (self.x + self.width // 2, self.y + self.height // 2), 5)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        self.screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height

    def click(self):
        if self.callback:
            self.callback()