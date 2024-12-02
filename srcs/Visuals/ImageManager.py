import pygame


class ImageManager:
    def __init__(self):
        self.images = {}

    def load_image(self, key, path, scale=None):
        try:
            image = pygame.image.load(path)
            if scale:
                image = pygame.transform.scale(image, scale)
            self.images[key] = image
        except pygame.error as e:
            print(f"Error al cargar la imagen {path}: {e}")
            self.images[key] = None

    def get_image(self, key):
        return self.images.get(key)
