import pygame.draw
from pygame.rect import RectType, Rect

from Musica.SoundManager import SoundManager
from srcs.Comandos.Command import Command
from srcs.Visuals.Button import Button
from srcs.Visuals.Colores import Colores



class CommandMenu(Command):
    def __init__(self,screen):
        self.screen = screen

    def execute(self) -> None:
        running = True
        window_width, window_height = self.screen.get_size()
        offset_x = (window_width - 600) // 2
        offset_y = (window_height - 400) // 2
        print("hi")
        menu = Rect(offset_x,offset_y, window_width//1.7,window_height//1.7)
        musica = SoundManager()
        boton_subirMusica = Button(self.screen, 40, 30, 650, 300, Colores.GREEN.value, musica.subirMusica, text="+")
        boton_bajarMusica = Button(self.screen, 40, 30, 40, 510, Colores.RED.value, musica.bajarMusica, text="-")
        boton_subirSonido = Button(self.screen, 40, 30, 650, 510, Colores.GREEN.value, musica.subirSonido, text="+")
        boton_bajarSonido = Button(self.screen, 40, 30, 40, 700, Colores.RED.value, musica.bajarSonido, text="-")

        def close():
            running = False
        boton_cerrar = Button(self.screen, 120, 60, 345, 900, Colores.RED.value, close, text="Cerrar")
        botones = []
        botones.append(boton_subirMusica)
        botones.append(boton_bajarMusica)
        botones.append(boton_subirSonido)
        botones.append(boton_bajarSonido)
        botones.append(boton_cerrar)
        while running:
            pygame.draw.rect(self.screen,Colores.WHITE_SMOKE.value,menu)
            # Dibujar botones de navegación
            for boton in botones:
                boton.draw()
            # Manejar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for boton in botones:
                        if boton.is_clicked(event.pos):
                            boton.click()
            pygame.display.flip()
