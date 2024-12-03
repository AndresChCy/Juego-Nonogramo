import pygame.draw
from pygame.rect import RectType, Rect

from Musica.SoundManager import SoundManager
from srcs.Comandos.Command import Command
from srcs.Visuals.Button import Button
from srcs.Visuals.Colores import Colores
from srcs.Visuals.SoundBar import SoundBar
from srcs.Visuals.TextRenderer import TextRenderer



class CommandMenu(Command):
    def __init__(self,screen):
        self.button_height = 50
        self.button_width = 50
        self.margin = 10
        self.screen = screen
        self.window_width = self.screen.get_width()
        self.window_height = self.screen.get_height()
        self.offset_x = (self.window_width - 600) // 2
        self.offset_y = (self.window_height - 400) // 2
        self.running = False
        self.sound_bar_music = SoundBar(self.screen, self.offset_x + 3 * self.margin + 2 * self.button_width, self.offset_y + self.margin,
                                        7 * self.button_width, self.button_height)
        self.sound_bar_sound = SoundBar(self.screen, self.offset_x + 3 * self.margin + 2 * self.button_width, self.offset_y + 2 * self.margin + self.button_height,
                                        7 * self.button_width, self.button_height)
        self.text_music = TextRenderer(self.screen, 'Body.ttf', 50, Colores.WHITE.value)
        self.text_sound = TextRenderer(self.screen, 'Body.ttf', 50, Colores.WHITE.value)


    def execute(self) -> None:
        global running
        self.running = True
        print("hi")
        menu = Rect(self.offset_x,self.offset_y, self.window_width//1.7,self.window_height//1.7)
        musica = SoundManager()
        musica.volumenMusic = 50
        musica.volumenSounds = 50
        boton_subirMusica = Button(self.screen, self.button_width, self.button_height, self.offset_x + self.margin,
                                   self.offset_y + self.margin, Colores.GREEN.value, musica.subirMusica, text="+")
        boton_bajarMusica = Button(self.screen, self.button_width, self.button_height, self.offset_x + 2 * self.margin + self.button_width,
                                   self.offset_y + self.margin, Colores.RED.value, musica.bajarMusica, text="-")
        boton_subirSonido = Button(self.screen, self.button_width, self.button_height, self.offset_x + self.margin,
                                   self.offset_y + 2 * self.margin + self.button_height, Colores.GREEN.value, musica.subirSonido, text="+")
        boton_bajarSonido = Button(self.screen, self.button_width, self.button_height, self.offset_x + 2 * self.margin + self.button_width,
                                   self.offset_y + 2 * self.margin + self.button_height, Colores.RED.value, musica.bajarSonido, text="-")

        def close():
            self.running = False

        boton_cerrar = Button(self.screen, self.button_width, self.button_height, self.offset_x + self.window_width//1.7 - self.button_width,
                              self.offset_y, Colores.RED.value, close, text="X")
        botones = []
        botones.append(boton_subirMusica)
        botones.append(boton_bajarMusica)
        botones.append(boton_subirSonido)
        botones.append(boton_bajarSonido)
        botones.append(boton_cerrar)

        while self.running:
            pygame.draw.rect(self.screen,Colores.WHITE_SMOKE.value,menu)
            # Dibujar botones de navegación
            for boton in botones:
                boton.draw()
            # Manejar eventos
            self.sound_bar_music.update(musica.get_volume_music())
            self.sound_bar_sound.update(musica.get_volume_sound())
            self.sound_bar_music.draw()
            self.sound_bar_sound.draw()
            self.text_music.render("Volumen Música", (self.window_width // 2, self.offset_y + self.margin + self.button_height // 2))
            self.text_sound.render("Volumen Sonido", (self.window_width // 2, self.offset_y + 2 * self.margin + self.button_height + self.button_height // 2))
            pygame.draw.rect(self.screen, Colores.BLACK.value, (self.offset_x - 5, self.offset_y - 5, self.window_width//1.7 + 10, self.window_height//1.7 + 10), 5)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for boton in botones:
                        if boton.is_clicked(event.pos):
                            boton.click()
            pygame.display.flip()