import pygame.draw
import os
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
        self.music_list = self.listar_archivos("Musica/MusicaFondo")
        self.music_index = 0
        self.sound_manager = SoundManager()
        self.cancion_actual = TextRenderer(self.screen, 'Body.ttf', 50, Colores.BLACK.value)
        self.nombre_cancion = "MainMenuTheme"

    def listar_archivos(self, directorio):
        archivos = []
        try:
            for archivo in os.listdir(directorio):
                ruta_completa = os.path.join(directorio, archivo)
                if os.path.isfile(ruta_completa):
                    archivos.append(ruta_completa)
        except FileNotFoundError:
            print(f"Error: El directorio {directorio} no existe.")
        except Exception as e:
            print(f"Error al listar archivos en {directorio}: {e}")
        return archivos

    def next_song(self):
        try:
            if self.music_index == len(self.music_list) - 1:
                self.music_index = 0
            else:
                self.music_index += 1
            directorio = os.path.join(self.music_list[self.music_index])
            self.sound_manager.stop_all()
            self.sound_manager.load_sound_as_music(self.music_list[self.music_index], directorio)
            self.sound_manager.play_music(loops=-1)
            nombre_cancion = os.path.splitext(os.path.basename(self.music_list[self.music_index]))[0]
            self.nombre_cancion = nombre_cancion
        except IndexError:
            print("Error: No hay canciones en la lista de música.")
        except Exception as e:
            print(f"Error al cambiar a la siguiente canción: {e}")

    def previous_song(self):
        try:
            if self.music_index == 0:
                self.music_index = len(self.music_list) - 1
            else:
                self.music_index -= 1
            directorio = os.path.join(self.music_list[self.music_index])
            self.sound_manager.stop_all()
            self.sound_manager.load_sound_as_music(self.music_list[self.music_index], directorio)
            self.sound_manager.play_music(loops=-1)
            nombre_cancion = os.path.splitext(os.path.basename(self.music_list[self.music_index]))[0]
            self.nombre_cancion = nombre_cancion
        except IndexError:
            print("Error: No hay canciones en la lista de música.")
        except Exception as e:
            print(f"Error al cambiar a la canción anterior: {e}")


    def execute(self) -> None:
        global running
        self.running = True
        menu = Rect(self.offset_x,self.offset_y, self.window_width//1.7,self.window_height//1.7)
        musica = SoundManager()
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
        boton_musica_siguiente = Button(self.screen, self.button_width, self.button_height, self.offset_x + self.window_width//1.7 - self.button_width - self.margin,
                                        self.offset_y + 2 * self.button_height + 4 * self.margin, Colores.GREEN.value, self.next_song, text=">")
        boton_musica_anterior = Button(self.screen, self.button_width, self.button_height, self.offset_x + self.margin,
                                        self.offset_y + 2 * self.button_height + 4 * self.margin, Colores.RED.value, self.previous_song, text="<")
        botones = []
        botones.append(boton_subirMusica)
        botones.append(boton_bajarMusica)
        botones.append(boton_subirSonido)
        botones.append(boton_bajarSonido)
        botones.append(boton_cerrar)
        botones.append(boton_musica_siguiente)
        botones.append(boton_musica_anterior)

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
            self.cancion_actual.render(self.nombre_cancion, (self.window_width // 2, self.offset_y + 2 * self.button_height + 4 * self.margin + self.button_height // 2))
            pygame.draw.rect(self.screen, Colores.BLACK.value, (self.offset_x - 5, self.offset_y - 5, self.window_width//1.7 + 10, self.window_height//1.7 + 10), 5)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for boton in botones:
                        if boton.is_clicked(event.pos):
                            boton.click()
            pygame.display.flip()