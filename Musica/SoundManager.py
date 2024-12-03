import pygame

class SoundManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SoundManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            pygame.mixer.init()
            self.sounds = {}
            self.music = None
            self.volumenMusic = 50
            self.volumenSounds = 50
            self.initialized = True

    def load_sound(self, name, file_path):

        self.sounds[name] = pygame.mixer.Sound(file_path)

    def load_sound_as_music(self, name, file_path):

        self.music = pygame.mixer.Sound(file_path)

    def play_sound(self, name, loops=0):
        if name in self.sounds:
            self.sounds[name].set_volume(self.volumenSounds / 100)
            self.sounds[name].play(loops=loops)


    def play_music(self,loops=-1):
        self.music.set_volume(self.volumenMusic / 100)
        self.music.play(loops=loops)


    def stop_all(self):
        pygame.mixer.stop()

    def set_volume_sounds(self, volume):
        self.volumenSounds = max(0, min(100, volume))
        for name in self.sounds:
            self.sounds[name].set_volume(self.volumenSounds / 100)

    def set_volume_music(self, volume):
        self.volumenMusic = max(0, min(100, volume))
        self.music.set_volume(self.volumenMusic / 100)

    def bajarSonido(self):
        self.set_volume_sounds(self.volumenSounds - 10)

    def subirSonido(self):
        self.set_volume_sounds(self.volumenSounds + 10)

    def bajarMusica(self):
        self.set_volume_music(self.volumenMusic - 10)

    def subirMusica(self):
        self.set_volume_music(self.volumenMusic + 10)

    def get_volume_music(self):
        return self.volumenMusic

    def get_volume_sound(self):
        return self.volumenSounds