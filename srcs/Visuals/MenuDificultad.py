import pygame
from pygame import KEYDOWN, K_ESCAPE

from Panel import Panel
from ProxyPanel import ProxyPanel
from srcs.Comandos.Command import Command

from Musica.SoundManager import *

pygame.init()
pygame.display.set_caption('Juego Nonogram')
ventana = pygame.display.set_mode((800, 600), 0, 32)
fpsControlador = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

class MenuDificultad(Panel):
    def __init__(self, ventana, proxy: ProxyPanel, facil : Command ,mid : Command, hard : Command,esc: Command):
        self.ventana = ventana
        self.proxy = proxy
        self.click = False
        button_width = 200
        button_height = 50
        self.esc = esc
        self.button_facil = pygame.Rect((ventana.get_width() - button_width) // 2, 200, button_width, button_height)
        self.button_normal = pygame.Rect((ventana.get_width() - button_width) // 2, 300, button_width, button_height)
        self.button_dificil = pygame.Rect((ventana.get_width() - button_width) // 2, 400, button_width, button_height)

        self.facil = facil
        self.mid = mid
        self. hard = hard
    def draw_text(self,texto, font, color, superficie, x, y):
        textobj = font.render(texto, 1, color)
        textrect = textobj.get_rect(center=(x, y))
        superficie.blit(textobj, textrect)

    def draw(self):
        pygame.draw.rect(self.ventana, (255, 0, 0), self.button_facil)
        pygame.draw.rect(self.ventana, (255, 0, 0), self.button_normal)
        pygame.draw.rect(self.ventana, (255, 0, 0), self.button_dificil)

        self.draw_text('Facil', font, (255, 255, 255), self.ventana, self.button_facil.centerx, self.button_facil.centery)
        self.draw_text('Normal', font, (255, 255, 255), self.ventana, self.button_normal.centerx, self.button_normal.centery)
        self.draw_text('Dificil', font, (255, 255, 255), self.ventana, self.button_dificil.centerx, self.button_dificil.centery)

    def handle_mouse_motion(self,event):
        pass

    def handle_click(self, pos, button):
        soundManager = SoundManager()
        soundManager.load_sound("guiclick", "Musica/guiclick.ogg")

        mx, my = pos
        click = False
        if button == 1:
            click = True

        if self.button_facil.collidepoint(mx, my) and click:
            soundManager.play_sound("guiclick")
            self.facil.execute()
        if self.button_normal.collidepoint(mx, my) and click:
            soundManager.play_sound("guiclick")
            self.mid.execute()
        if self.button_dificil.collidepoint(mx, my) and click:
            soundManager.play_sound("guiclick")
            self.hard.execute()

    def handle_key(self,event):
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            self.esc.execute()


if __name__ == '__main__':
    MenuDificultad(ventana, ProxyPanel())