import pygame

class TextRenderer:
    def __init__(self, screen, font_path, font_size, color):
        self.screen = screen
        self.font = pygame.font.Font(font_path, font_size)
        self.color = color

    def render(self, message, position):
        text_surface = self.font.render(message, True, self.color)
        text_rect = text_surface.get_rect(center=position)
        self.screen.blit(text_surface, text_rect)