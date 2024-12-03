import pygame
import sys

from pygame.constants import FULLSCREEN

from Panel import Panel
from pygame.locals import *

from srcs.Comandos.Command import Ejecutador, Command
from srcs.Comandos.CommandCambiarPanel import CommandCambiarPanel
from srcs.Comandos.CommandGuardar import CommandGuardar
from srcs.Logica.Dibujo import Dibujo
from srcs.Visuals.Grilla.GrillaVisual import GrillaVisual
from srcs.Visuals.ImageManager import ImageManager
from srcs.Visuals.ProxyPanel import ProxyPanel

pygame.init()
ventana = pygame.display.set_mode((800, 600), 0, 32)
font = pygame.font.SysFont(None, 40)
font_2 = pygame.font.SysFont(None, 32)

pygame.display.set_caption("Nonogram")
fpsControlador = pygame.time.Clock()

class CrearNivel(Panel):
    def __init__(self, ventana, titulo, ancho, largo,proxy: ProxyPanel,volver: Command):
        self.ventana = ventana
        self.titulo = titulo
        self.ancho = ancho
        self.largo = largo

        self.proxy = proxy
        self.volver = volver

        self.active1 = False
        self.active2 = False

        self.text1 = ''
        self.text2 = ''

        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.color1 = self.color_inactive
        self.color2 = self.color_inactive

        self.rect = pygame.Rect((ventana.get_width() - 400) // 2, 200, 400, 250)
        self.font = pygame.font.Font(None, 32)
        self.clock = pygame.time.Clock()

        self.input_box1 = pygame.Rect(self.rect.x + (self.rect.w - 140) // 2, self.rect.y + (self.rect.h - 32) // 3, 140, 32)
        self.input_box2 = pygame.Rect(self.rect.x + (self.rect.w - 140) // 2, self.rect.y + (self.rect.h - 32) // 3 + 50, 140, 32)
        self.boton_aceptar = pygame.Rect((ventana.get_width() - 200) // 2, ventana.get_height() - 255, 200, 50)

        self.image_manager = ImageManager()
        self.image_manager.load_image("background", "Img/backgroun.jpg", scale=(1000, 700))
        # Cargar la imagen de fondo usando el ImageManager
        self.background_image = self.image_manager.get_image("background")
        self.ventana.blit(self.background_image, (0, 0))

    def execute(self):
        running = True
        while running:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    running = False
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(evento.pos, evento.button)
                elif evento.type == pygame.MOUSEMOTION:
                    self.handle_mouse_motion(evento)
                elif evento.type == pygame.KEYDOWN:
                    self.handle_key(evento)

            self.ventana.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()
        pygame.quit()
        sys.exit()

    def handle_mouse_motion(self,event):
        pass

    def handle_click(self, pos, button):
        if self.input_box1.collidepoint(pos):
            self.active1 = not self.active1
        else:
            self.active1 = False

        if self.input_box2.collidepoint(pos):
            self.active2 = not self.active2
        else:
            self.active2 = False

        if self.boton_aceptar.collidepoint(pos):
            print("Botón Aceptar presionado")
            if (self.text1 != "" and self.text2 != ""):
                dibujo = Dibujo(int(self.text1), int(self.text2))
                com = Ejecutador()
                com.addCommand(CommandGuardar(dibujo))
                com.addCommand(self.volver)
                def pantallaNormal():
                    self.screen = pygame.display.set_mode((1000, 650))
                com.addCommand(pantallaNormal)
                # self.proxy.ponerTarget(panelDibujo(ventana,x,y,self.proxy))
                self.screen = pygame.display.set_mode((0, 0), FULLSCREEN)
                self.proxy.ponerTarget(GrillaVisual(ventana, dibujo, self.proxy, com, dibujo=True))
            else:
                self.volver.execute()

        self.color1 = self.color_active if self.active1 else self.color_inactive
        self.color2 = self.color_active if self.active2 else self.color_inactive

    def handle_key(self,event):
        if event.key == pygame.K_RETURN:
            if self.text1 == '' or self.text2 == '':
                self.volver.execute()
            else:
                dibujo = Dibujo(int(self.text1), int(self.text2))
                com = Ejecutador()
                com.addCommand(CommandGuardar(dibujo))
                com.addCommand(self.volver)
                def pantallaNormal():
                    self.screen = pygame.display.set_mode((1000, 650))
                com.addCommand(pantallaNormal)
                # self.proxy.ponerTarget(panelDibujo(ventana,x,y,self.proxy))
                self.screen = pygame.display.set_mode((0, 0), FULLSCREEN)
                self.proxy.ponerTarget(GrillaVisual(ventana, dibujo, self.proxy, com))

        if self.active1:
            if event.key == pygame.K_BACKSPACE:
                self.text1 = self.text1[:-1]
            elif event.unicode.isdigit():
                self.text1 += event.unicode

        elif self.active2:
            if event.key == pygame.K_BACKSPACE:
                self.text2 = self.text2[:-1]
            elif event.unicode.isdigit():
                self.text2 += event.unicode

    def draw(self):
        self.ventana.blit(self.background_image, (0, 0))
        pygame.draw.rect(self.ventana, (0, 0, 0), self.rect)
        self.draw_text('Escoger dimensiones', font, (255, 255, 255), self.ventana, self.rect.centerx, self.rect.top + 20)

        txt_surface1 = font.render(self.text1, True, self.color1)
        txt_surface2 = font.render(self.text2, True, self.color2)

        self.draw_text("Alto:", font_2, (255, 255, 255), self.ventana, self.input_box1.left - 50, self.input_box1.centery)
        self.draw_text("Ancho:", font_2, (255, 255, 255), self.ventana, self.input_box2.left - 50, self.input_box2.centery)

        self.ventana.blit(txt_surface1, (self.input_box1.x + 5, self.input_box1.y + 5))
        self.ventana.blit(txt_surface2, (self.input_box2.x + 5, self.input_box2.y + 5))

        pygame.draw.rect(self.ventana, (255,0,0), self.boton_aceptar)
        self.draw_text("Aceptar", font, (255, 255, 255), self.ventana, self.boton_aceptar.centerx,self.boton_aceptar.centery)

        pygame.draw.rect(self.ventana, self.color1, self.input_box1, 2)
        pygame.draw.rect(self.ventana, self.color2, self.input_box2, 2)

        pygame.display.flip()
        self.clock.tick(30)

    def draw_text(self,texto, font, color, superficie, x, y):
        textobj = font.render(texto, 1, color)
        textrect = textobj.get_rect(center=(x, y))
        superficie.blit(textobj, textrect)

if __name__ == "__main__":
    ventana = pygame.display.set_mode((800, 600), 0, 32)
    crear_nivel = CrearNivel(ventana,"Dimensiones", 8, 8)
    crear_nivel.execute()