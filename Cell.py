import pygame
from Colores import Colores


class Cell(pygame.sprite.Sprite):
    """
    Clase que representa una celda individual dentro de la cuadrícula de un juego Nonogram.
    Hereda de `pygame.sprite.Sprite` para permitir el manejo sencillo de sprites en Pygame.

    Atributos:
    ----------
    image : pygame.Surface
        Superficie de la celda para representar su imagen.
    rect : pygame.Rect
        Rectángulo que delimita la posición y el tamaño de la celda.
    filled : bool
        Indica si la celda está llena (seleccionada) en la lógica del juego.
    marked : bool
        Indica si la celda está marcada con una 'X' (marca del jugador).
    """

    def __init__(self, x, y, size):
        """
        Inicializa la Celda.

        Args:
            x (int): La posición x de la celda.
            y (int): La posición y de la celda.
            size (int): El tamaño de la celda.
        """
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(Colores.WHITE.value)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.filled = False
        self.marked = False

    def fill(self):
        """
        Llena la celda y cambia su color.
        """
        self.filled = True
        self.marked = False
        self.image.fill(Colores.DARK_GREY.value)

    def empty(self):
        """
        Vacía la celda y cambia su color.
        """
        self.filled = False
        self.marked = False
        self.image.fill(Colores.WHITE.value)

    def mark(self):
        """
        Marca la celda y cambia su color.
        """
        self.marked = True
        self.filled = False
        self.image.fill(Colores.WHITE.value)

    def draw(self, screen):
        """
        Dibuja la celda en la pantalla.

        Args:
            screen (pygame.Surface): La superficie de la pantalla donde se dibujará la celda.
        """
        screen.blit(self.image, self.rect.topleft)
        if self.filled:
            pygame.draw.rect(screen, Colores.DARK_GREY.value, self.rect)
        elif self.marked:
            pygame.draw.line(screen, Colores.RED.value, self.rect.topleft, self.rect.bottomright, 4)
            pygame.draw.line(screen, Colores.RED.value, self.rect.topright, self.rect.bottomleft, 4)
        else:
            pygame.draw.rect(screen, Colores.WHITE.value, self.rect)
