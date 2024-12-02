import pygame
from pygame import KEYDOWN, K_ESCAPE

from Panel import Panel
from ProxyPanel import ProxyPanel
from srcs.Comandos.Command import Command
from srcs.Comandos.CommandCambiarPanel import CommandCambiarPanel
from srcs.Logica.Niveles import Niveles
from srcs.Visuals.Grilla.GrillaDecorator import DecoratorClues, DecoratorMiniatureRender
from srcs.Visuals.Grilla.GrillaVisual import GrillaVisual
from srcs.Visuals.MenuDificultad import MenuDificultad
from srcs.Visuals.MenuNiveles import MenuNiveles

pygame.init()
pygame.display.set_caption('Juego Nonogram')
ventana = pygame.display.set_mode((800, 600), 0, 32)
fpsControlador = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

class SeleccionTipoNivel(Panel):
    def __init__(self, ventana, proxy: ProxyPanel, enter: Command):
        self.ventana = ventana
        self.proxy = proxy
        self.click = False
        button_width = 220
        button_height = 50
        self.enter = enter

        self.button_niveles = pygame.Rect((ventana.get_width() - button_width) // 2, 200, button_width, button_height)
        self.button_ninveles_creados = pygame.Rect((ventana.get_width() - button_width) // 2, 300, button_width, button_height)
        self.button_al_azar = pygame.Rect((ventana.get_width() - button_width) // 2, 400, button_width, button_height)
        niveles = Niveles()
        toMe = CommandCambiarPanel(self,self.proxy)
        menuNivelesBase = MenuNiveles(self.ventana, niveles.getNivelesBase()[0], self.proxy)
        menuNivelesBase2 = MenuNiveles(self.ventana, niveles.getNivelesBase()[1], self.proxy)
        menuNivelesBase3 = MenuNiveles(self.ventana, niveles.getNivelesBase()[2], self.proxy)
        menuNivelesCrea = MenuNiveles(self.ventana, niveles.getNivelesCreados()[0], self.proxy)
        menuNivelesCrea2 = MenuNiveles(self.ventana, niveles.getNivelesCreados()[1], self.proxy)
        menuNivelesCrea3 = MenuNiveles(self.ventana, niveles.getNivelesCreados()[2], self.proxy)

        toNivelesBase = CommandCambiarPanel(menuNivelesBase, self.proxy)
        toNivelesBase2 = CommandCambiarPanel(menuNivelesBase2, self.proxy)
        toNivelesBase3 = CommandCambiarPanel(menuNivelesBase3, self.proxy)
        toNivelesCrea = CommandCambiarPanel(menuNivelesCrea, self.proxy)
        toNivelesCrea2 = CommandCambiarPanel(menuNivelesCrea2, self.proxy)
        toNivelesCrea3 = CommandCambiarPanel(menuNivelesCrea3, self.proxy)

        self.nivelesBase =  MenuDificultad(self.ventana,self.proxy, toNivelesBase, toNivelesBase2, toNivelesBase3,toMe)
        self.nivelesCrea = MenuDificultad(self.ventana, self.proxy, toNivelesCrea, toNivelesCrea2, toNivelesCrea3,toMe)

    def draw_text(self,texto, font, color, superficie, x, y):
        textobj = font.render(texto, 1, color)
        textrect = textobj.get_rect(center=(x, y))
        superficie.blit(textobj, textrect)

    def draw(self):
        pygame.draw.rect(self.ventana, (255, 0, 0), self.button_niveles)
        pygame.draw.rect(self.ventana, (255, 0, 0), self.button_ninveles_creados)
        pygame.draw.rect(self.ventana, (255, 0, 0), self.button_al_azar)

        self.draw_text('Niveles', font, (255, 255, 255), self.ventana, self.button_niveles.centerx, self.button_niveles.centery)
        self.draw_text('Niveles Creados', font, (255, 255, 255), self.ventana, self.button_ninveles_creados.centerx, self.button_ninveles_creados.centery)
        self.draw_text('Nivel al azar', font, (255, 255, 255), self.ventana, self.button_al_azar.centerx, self.button_al_azar.centery)

    def handle_mouse_motion(self,event):
        pass

    def handle_click(self, pos, button, soundManager):
        mx, my = pos
        click = False
        if button == 1:
            click = True
        if self.button_niveles.collidepoint(mx, my) and click:
            niveles = Niveles()
            menuNivelesBase = MenuNiveles(self.ventana, niveles.getNivelesBase()[0], self.proxy)
            menuNivelesBase2 = MenuNiveles(self.ventana, niveles.getNivelesBase()[1], self.proxy)
            menuNivelesBase3 = MenuNiveles(self.ventana, niveles.getNivelesBase()[2], self.proxy)
            menuNivelesCrea = MenuNiveles(self.ventana, niveles.getNivelesCreados()[0], self.proxy)
            menuNivelesCrea2 = MenuNiveles(self.ventana, niveles.getNivelesCreados()[1], self.proxy)
            menuNivelesCrea3 = MenuNiveles(self.ventana, niveles.getNivelesCreados()[2], self.proxy)

            toNivelesBase = CommandCambiarPanel(menuNivelesBase, self.proxy)
            toNivelesBase2 = CommandCambiarPanel(menuNivelesBase2, self.proxy)
            toNivelesBase3 = CommandCambiarPanel(menuNivelesBase3, self.proxy)
            toNivelesCrea = CommandCambiarPanel(menuNivelesCrea, self.proxy)
            toNivelesCrea2 = CommandCambiarPanel(menuNivelesCrea2, self.proxy)
            toNivelesCrea3 = CommandCambiarPanel(menuNivelesCrea3, self.proxy)
            toMe = CommandCambiarPanel(self, self.proxy)
            self.nivelesBase = MenuDificultad(self.ventana, self.proxy, toNivelesBase, toNivelesBase2, toNivelesBase3,toMe)
            self.nivelesCrea = MenuDificultad(self.ventana, self.proxy, toNivelesCrea, toNivelesCrea2, toNivelesCrea3,toMe)
            self.proxy.ponerTarget(self.nivelesBase)
        if self.button_ninveles_creados.collidepoint(mx, my) and click:
            niveles = Niveles()
            menuNivelesBase = MenuNiveles(self.ventana, niveles.getNivelesBase()[0], self.proxy)
            menuNivelesBase2 = MenuNiveles(self.ventana, niveles.getNivelesBase()[1], self.proxy)
            menuNivelesBase3 = MenuNiveles(self.ventana, niveles.getNivelesBase()[2], self.proxy)
            menuNivelesCrea = MenuNiveles(self.ventana, niveles.getNivelesCreados()[0], self.proxy)
            menuNivelesCrea2 = MenuNiveles(self.ventana, niveles.getNivelesCreados()[1], self.proxy)
            menuNivelesCrea3 = MenuNiveles(self.ventana, niveles.getNivelesCreados()[2], self.proxy)

            toNivelesBase = CommandCambiarPanel(menuNivelesBase, self.proxy)
            toNivelesBase2 = CommandCambiarPanel(menuNivelesBase2, self.proxy)
            toNivelesBase3 = CommandCambiarPanel(menuNivelesBase3, self.proxy)
            toNivelesCrea = CommandCambiarPanel(menuNivelesCrea, self.proxy)
            toNivelesCrea2 = CommandCambiarPanel(menuNivelesCrea2, self.proxy)
            toNivelesCrea3 = CommandCambiarPanel(menuNivelesCrea3, self.proxy)
            toMe = CommandCambiarPanel(self, self.proxy)
            self.nivelesBase = MenuDificultad(self.ventana, self.proxy, toNivelesBase, toNivelesBase2, toNivelesBase3,toMe)
            self.nivelesCrea = MenuDificultad(self.ventana, self.proxy, toNivelesCrea, toNivelesCrea2, toNivelesCrea3,toMe)
            self.proxy.ponerTarget(self.nivelesCrea)
        if self.button_al_azar.collidepoint(mx, my) and click:
            tablero = Niveles().getTableroAleatorio()
            if tablero != None:
                g = GrillaVisual(self.ventana,tablero,self.proxy,None)
                gc = DecoratorClues(g)
                gcm = DecoratorMiniatureRender(gc)
                self.proxy.ponerTarget(gcm)

    def handle_key(self,event):
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            self.enter.execute()


if __name__ == '__main__':
    SeleccionTipoNivel(ventana, ProxyPanel())