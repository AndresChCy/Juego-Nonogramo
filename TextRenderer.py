import pygame

class TextRenderer:
    def __init__(self, screen, font_path, font_size, color):
        """
        Inicializa el renderizador de texto.

        Args:
            screen (pygame.Surface): La superficie de la pantalla donde se dibujará el texto.
            font_path (str): La ruta al archivo de la fuente.
            font_size (int): El tamaño de la fuente.
            color (tuple): El color del texto.
        """
        self.screen = screen
        self.font = pygame.font.Font(font_path, font_size)
        self.color = color

    def render(self, message, position):
        """
        Renderiza el texto en la pantalla.

        Args:
            message (str): El mensaje de texto a renderizar.
            position (tuple): La posición (x, y) donde se centrará el texto.
        """
        text_surface = self.font.render(message, True, self.color)
        text_rect = text_surface.get_rect(center=position)
        self.screen.blit(text_surface, text_rect)