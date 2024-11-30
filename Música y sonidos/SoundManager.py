import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {}

    def load_sound(self, name, file_path):

        self.sounds[name] = pygame.mixer.Sound(file_path)


    def play_sound(self, name):

        if name in self.sounds:
            self.sounds[name].play()

    def stop_all(self):

        pygame.mixer.stop()
