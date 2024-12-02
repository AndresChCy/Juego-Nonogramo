import pygame

class ImageRenderer:
    def __init__(self, screen, frames, flip_x=False, flip_y=False, size=None):
        """
        Inicializa el renderizador de imágenes.

        Args:
            screen (pygame.Surface): La superficie de la pantalla donde se dibujarán las imágenes.
            frames (list): Lista de fotogramas (imágenes) a renderizar.
            flip_x (bool): Si se deben voltear las imágenes horizontalmente.
            flip_y (bool): Si se deben voltear las imágenes verticalmente.
        """
        self.screen = screen
        self.frames = [pygame.transform.flip(frame, flip_x, flip_y) for frame in frames]
        if size:
            self.frames = [pygame.transform.scale(frame, size) for frame in self.frames]
        self.current_frame = 0
        self.frame_delay = 4
        self.frame_counter = 0

    def draw(self, position):
        """
        Dibuja la imagen actual en la pantalla.

        Args:
            position (tuple): La posición (x, y) donde se centrará la imagen.
        """
        image = self.frames[self.current_frame]
        image_rect = image.get_rect(center=position)
        self.screen.blit(image, image_rect)
        self.frame_counter += 1
        if self.frame_counter >= self.frame_delay:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.frame_counter = 0