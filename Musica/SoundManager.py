import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {}

    def load_sound(self, name, file_path):

        self.sounds[name] = pygame.mixer.Sound(file_path)


    def play_sound(self, name, loops=0):
        if name in self.sounds:
            self.sounds[name].play(loops=loops)

    def stop_all(self):

        pygame.mixer.stop()

    def set_volume(self, name, volume):
        if name in self.sounds:
            self.sounds[name].set_volume(volume)