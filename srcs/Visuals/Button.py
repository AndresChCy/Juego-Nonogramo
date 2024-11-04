import pygame
from srcs.Visuals.Colores import Colores

class Button:
    """
    Clase que representa un botón interactivo en la interfaz de usuario.

    Atributos:
        screen (Surface): Superficie de Pygame en la que se dibuja el botón.
        width (int): Ancho del botón.
        height (int): Alto del botón.
        x (int): Posición X del botón en la pantalla.
        y (int): Posición Y del botón en la pantalla.
        color (tuple): Color de fondo del botón.
        text_color (tuple): Color del texto del botón.
        callback (callable): Función que se ejecuta al hacer clic en el botón.
        font (Font): Fuente utilizada para el texto del botón.
        image (Surface): Imagen opcional que se muestra en lugar de color de fondo.
        draw_rectangle (bool): Indica si se debe dibujar un rectángulo dentro del botón.
        draw_cross (bool): Indica si se debe dibujar una cruz sobre el botón.
        draw_point (bool): Indica si se debe dibujar un punto en el centro del botón.
        opacity (int): Nivel de opacidad del botón (0-255).
    """

    def __init__(self, screen, width, height, x, y, color, callback, text_color=Colores.WHITE.value,
                 text="", image_path=None, draw_rectangle=False, draw_cross=False, draw_point=False, opacity=255):
        """
        Inicializa un botón con las propiedades y opciones visuales especificadas.

        Args:
            screen (Surface): Superficie de Pygame en la que se dibuja el botón.
            width (int): Ancho del botón.
            height (int): Alto del botón.
            x (int): Posición X del botón en la pantalla.
            y (int): Posición Y del botón en la pantalla.
            color (tuple): Color de fondo del botón.
            callback (callable): Función que se ejecuta cuando el botón es clicado.
            text_color (tuple): Color del texto (opcional).
            text (str): Texto a mostrar en el botón (opcional).
            image_path (str): Ruta de la imagen opcional para el botón (opcional).
            draw_rectangle (bool): Dibuja un rectángulo interior si es True.
            draw_cross (bool): Dibuja una cruz en el botón si es True.
            draw_point (bool): Dibuja un punto en el centro si es True.
            opacity (int): Nivel de opacidad del botón (0-255).
        """
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

        # Cargar imagen si se proporciona una ruta y establecer su opacidad.
        if image_path:
            try:
                self.image = pygame.image.load(image_path)
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
                self.image.set_alpha(opacity)
            except pygame.error as e:
                print(f"Error loading image at {image_path}: {e}")

        # Opciones de dibujo adicionales.
        self.draw_rectangle = draw_rectangle
        self.draw_cross = draw_cross
        self.draw_point = draw_point
        self.opacity = opacity

    def draw(self):
        """
        Dibuja el botón en la pantalla, aplicando todas las opciones visuales configuradas.
        """
        # Dibujar imagen si existe, de lo contrario, dibujar un rectángulo de color.
        if self.image:
            self.screen.blit(self.image, (self.x, self.y))
        else:
            # Crear una superficie transparente con opacidad.
            surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            surface.fill((*self.color, self.opacity))
            self.screen.blit(surface, (self.x, self.y))

        # Dibuja un rectángulo interior si está activado.
        if self.draw_rectangle:
            margin = 7
            inner_rect = pygame.Rect(self.x + margin, self.y + margin, self.width - 2 * margin, self.height - 2 * margin)
            pygame.draw.rect(self.screen, Colores.BLACK.value, inner_rect)

        # Dibuja una cruz en el botón si está activado.
        if self.draw_cross:
            pygame.draw.line(self.screen, Colores.RED.value, (self.x, self.y),
                             (self.x + self.width, self.y + self.height), 4)
            pygame.draw.line(self.screen, Colores.RED.value, (self.x + self.width, self.y),
                             (self.x, self.y + self.height), 4)

        # Dibuja un punto en el centro del botón si está activado.
        if self.draw_point:
            pygame.draw.circle(self.screen, Colores.BLACK.value,
                               (self.x + self.width // 2, self.y + self.height // 2), 5)

        # Renderiza y centra el texto en el botón.
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        self.screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        """
        Verifica si la posición proporcionada coincide con la del botón (si fue clicado).

        Args:
            pos (tuple): Posición del clic del ratón.

        Returns:
            bool: True si el clic fue dentro de los límites del botón, False en caso contrario.
        """
        return self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height

    def click(self):
        """
        Ejecuta la función callback asignada al botón, si existe.
        """
        if self.callback:
            self.callback()