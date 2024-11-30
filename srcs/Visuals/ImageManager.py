import pygame


class ImageManager:
    def __init__(self):
        pygame.init()
        self.images = {}

    def load_image(self, name, file_path, scale=None):
        image = pygame.image.load(file_path)  #
        if scale:
            image = pygame.transform.scale(image, scale)
        self.images[name] = image

    def get_image(self, name):
        if name in self.images:
            return self.images[name]
        else:
            return None
