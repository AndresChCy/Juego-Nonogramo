import pygame
from pygame.locals import *

from srcs.Logica.Dibujo import Dibujo
from srcs.Visuals.Grid import Grid
from Panel import Panel
from ProxyPanel import ProxyPanel
from srcs.Logica.Tablero import Tablero

pygame.init()
pygame.display.set_caption('Juego Nonogram')
ventana = pygame.display.set_mode((800, 600), 0, 32)
fpsControlador = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

class MenuDificultad(Panel):
    def __init__(self, ventana, proxy: ProxyPanel):
        self.ventana = ventana
        self.proxy = proxy
        self.click = False
        button_width = 200
        button_height = 50

        self.button_facil = pygame.Rect((ventana.get_width() - button_width) // 2, 200, button_width, button_height)
        self.button_normal = pygame.Rect((ventana.get_width() - button_width) // 2, 300, button_width, button_height)
        self.button_dificil = pygame.Rect((ventana.get_width() - button_width) // 2, 400, button_width, button_height)


    def draw_text(self,texto, font, color, superficie, x, y):
        textobj = font.render(texto, 1, color)
        textrect = textobj.get_rect(center=(x, y))
        superficie.blit(textobj, textrect)

    def draw(self):
        pygame.draw.rect(self.ventana, (255, 0, 0), self.button_facil)
        pygame.draw.rect(self.ventana, (255, 0, 0), self.button_normal)
        pygame.draw.rect(self.ventana, (255, 0, 0), self.button_dificil)

        self.draw_text('Facil', font, (255, 255, 255), self.ventana, self.button_1.centerx, self.button_1.centery)
        self.draw_text('Normal', font, (255, 255, 255), self.ventana, self.button_2.centerx, self.button_2.centery)
        self.draw_text('Dificil', font, (255, 255, 255), self.ventana, self.button_3.centerx, self.button_3.centery)

    def handle_mouse_motion(self,event):
        pass
    def handle_click(self, pos, button):
        pass
    def handle_key(self,event):
        pass
    def draw(self):
        pass
