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
            self.volumenMusic = 0.5
            self.volumenSounds = 0.5
            self.initialized = True

    def load_sound(self, name, file_path):

        self.sounds[name] = pygame.mixer.Sound(file_path)

    def load_sound_as_music(self, name, file_path):

        self.music = pygame.mixer.Sound(file_path)

    def play_sound(self, name, loops=0):
        if name in self.sounds:
            self.sounds[name].set_volume(self.volumenSounds)
            self.sounds[name].play(loops=loops)


    def play_music(self,loops=-1):
        self.music.set_volume(self.volumenMusic)
        self.music.play(loops=loops)


    def stop_all(self):
        pygame.mixer.stop()

    def set_volume_sounds(self, volume):
        self.volumenSounds = volume
        for name in self.sounds:
            self.sounds[name].set_volume(volume)

    def set_volume_music(self, volume):
        self.volumenMusic = volume
        self.music.set_volume(volume)

    def bajarSonido(self):
        self.volumenSounds = self.volumenSounds - 0.1

    def subirSonido(self):
        self.volumenSounds = self.volumenSounds + 0.1

    def bajarMusica(self):
        self.volumenMusic = self.volumenMusic - 0.1
        self.music.set_volume(self.volumenMusic)
    def subirMusica(self):
        self.volumenMusic = self.volumenMusic + 0.1
        self.music.set_volume(self.volumenMusic)

