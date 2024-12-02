import pygame
import sys

from pygame.constants import K_ESCAPE, KEYDOWN
from pygame.locals import *

from PanelDibujo import panelDibujo
from srcs.Comandos.Command import Ejecutador
from srcs.Comandos.CommandCambiarPanel import CommandCambiarPanel
from srcs.Comandos.CommandGuardar import CommandGuardar
from srcs.Logica.Dibujo import Dibujo
from srcs.Logica.Niveles import Niveles
from srcs.Visuals.Button import Button
from srcs.Visuals.Colores import Colores
from Panel import Panel
from ProxyPanel import ProxyPanel
from srcs.Visuals.Grilla.GrillaVisual import GrillaRender, GrillaVisual
from srcs.Visuals.MenuCrearNivel import CrearNivel
from srcs.Visuals.MenuNiveles import MenuNiveles
from srcs.Visuals.NonogramPanel import NonogramPanel
from srcs.Visuals.SeleccionTipoNivel import SeleccionTipoNivel

pygame.init()
pygame.display.set_caption('Juego Nonogram')
ventana = pygame.display.set_mode((800, 600), 0, 32)
fpsControlador = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)


#click = False
class Menu(Panel):

    def __init__(self,ventana,proxy:ProxyPanel,comandos , nombres,volver= None):
        self.ventana = ventana
        self.proxy = proxy
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.click = False
        self.volver = volver
        ventana.fill((0, 0, 0))
        button_width = 200
        button_height = 50
        center = (ventana.get_width() - button_width) // 2
        self.buttons = []
        for i in range (len(comandos)):
            if len(comandos) != len(nombres):
                nombre = comandos[i].__class__.__name__
            else:
                nombre = nombres[i]
            boton = Button(self.ventana,button_width,button_height,center,200 + 100*i,Colores.BLUE.value,comandos[i]
                           ,Colores.WHITE.value,nombre)
            self.buttons.append(boton)


        #self.button_1 = pygame.Rect((ventana.get_width() - button_width) // 2, 200, button_width, button_height)
        #self.button_2 = pygame.Rect((ventana.get_width() - button_width) // 2, 300, button_width, button_height)
    #    self.button_3 = pygame.Rect((ventana.get_width() - button_width) // 2, 400, button_width, button_height)

        self.menuJugar = SeleccionTipoNivel(self.ventana,self.proxy,CommandCambiarPanel(self,self.proxy))
    def draw_text(self,texto, font, color, superficie, x, y):
        textobj = font.render(texto, 1, color)
        textrect = textobj.get_rect(center=(x, y))
        superficie.blit(textobj, textrect)

    def draw(self):
        for buttons in self.buttons:
            buttons.draw()

        fpsControlador.tick(60)

    def handle_click(self, pos, button):
        mx, my = pygame.mouse.get_pos()
        self.click = True
        for btn in self.buttons:
            if btn and btn.is_clicked(pos):
                btn.click()
                break
        self.click = False

    def handle_mouse_motion(self,pos):
        pass
    def handle_key(self,event):
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                if self.volver:
                    self.volver()
                else:
                    pygame.quit()
                    sys.exit()


    def juego(self):
        self.proxy.ponerTarget(self.menuJugar)

    def crearNivel(self):
        self.proxy.ponerTarget(CrearNivel(self.ventana,"Escoger dimensiones",400,300,self.proxy,CommandCambiarPanel(self,self.proxy)))
       # x,y = self.inputs()
        #if (x and y):
         #   dibujo = Dibujo(x,y)
          #  com = Ejecutador()
           # com.addCommand(CommandGuardar(dibujo))
            #com.addCommand(CommandCambiarPanel(self,self.proxy))
           # self.proxy.ponerTarget(panelDibujo(ventana,x,y,self.proxy))
            #self.proxy.ponerTarget(GrillaVisual(ventana,dibujo,self.proxy,com))
       # self.proxy.cambiarTarget(1)
        #ejecutando=True
        #while ejecutando:
            #ventana.fill((0,0,0))
            #self.draw_text('Opciones', font, (255, 255, 255), ventana, ventana.get_width()//2, ventana.get_height()//2)

       #     for event in pygame.event.get():
          #      if event.type==QUIT:
          #          pygame.quit()
          #          sys.exit()
           #     if event.type==KEYDOWN and event.key==K_ESCAPE:
           #         ejecutando=False

           # pygame.display.update()
           # fpsControlador.tick(60)

    def salir(self):
        pygame.quit()
        niveles = Niveles()
        niveles.GuardarNivelesCreados()
        niveles.GuardarNivelesPredeterminados()
        sys.exit()


def aaa():
    print("hiii")


class Window:
    def __init__(self, matrix):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption('Nonograma')
        self.p = ProxyPanel([])
        co = CommandCambiarPanel(Menu(self.screen,self.p,[None,None],["hola"]),self.p)
        self.cuadricula = Menu(self.screen,self.p,[aaa,co],["hola"])
        self.p.ponerTarget(self.cuadricula)


    def execute(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                   self.p.handle_click(event.pos, event.button)
                elif event.type == pygame.MOUSEMOTION:
                    self.p.handle_mouse_motion(event.pos)
                elif event.type == pygame.KEYDOWN:
                    self.p.handle_key(event)
            self.screen.fill(Colores.WHITE.value)
            self.p.draw()
            pygame.display.flip()
        pygame.quit()
        sys.exit()
if __name__ == "__main__":
    matrix = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],

    ]
    Window(matrix).execute()
    #MenuPrincipal(ventana)