import pygame
import sys
from pygame.locals import *

from PanelDibujo import panelDibujo
from srcs.Comandos.Command import Ejecutador
from srcs.Comandos.CommandCambiarPanel import CommandCambiarPanel
from srcs.Comandos.CommandGuardar import CommandGuardar
from srcs.Logica.Dibujo import Dibujo
from srcs.Logica.Niveles import Niveles
from srcs.Visuals.Colores import Colores
from Panel import Panel
from ProxyPanel import ProxyPanel
from srcs.Visuals.Grilla.GrillaVisual import GrillaRender, GrillaVisual
from srcs.Visuals.MenuCrearNivel import CrearNivel
from srcs.Visuals.SeleccionTipoNivel import SeleccionTipoNivel

from Musica.SoundManager import *

pygame.init()
pygame.display.set_caption('Juego Nonogram')
ventana = pygame.display.set_mode((800, 600), 0, 32)
fpsControlador = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)


#click = False
class MenuPrincipal(Panel):

    def __init__(self,ventana,proxy:ProxyPanel):
        self.ventana = ventana
        self.proxy = proxy
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.click = False
        ventana.fill((0, 0, 0))
        button_width = 200
        button_height = 50
        self.button_1 = pygame.Rect((ventana.get_width() - button_width) // 2, 200, button_width, button_height)
        self.button_2 = pygame.Rect((ventana.get_width() - button_width) // 2, 300, button_width, button_height)
        self.button_3 = pygame.Rect((ventana.get_width() - button_width) // 2, 400, button_width, button_height)

        soundManager = SoundManager()
        soundManager.load_sound("MainMenuTheme", "Musica/MainMenuTheme.mp3")
        soundManager.load_sound("guiclick", "Musica/guiclick.ogg")
        soundManager.play_sound("MainMenuTheme")


        self.menuJugar = SeleccionTipoNivel(self.ventana,self.proxy,CommandCambiarPanel(self,self.proxy))
    def draw_text(self,texto, font, color, superficie, x, y):
        textobj = font.render(texto, 1, color)
        textrect = textobj.get_rect(center=(x, y))
        superficie.blit(textobj, textrect)

    def draw(self):
        pygame.draw.rect(self.ventana, (255, 0, 0), self.button_1)
        pygame.draw.rect(self.ventana, (255, 0, 0), self.button_2)
        pygame.draw.rect(self.ventana, (255, 0, 0), self.button_3)

        self.draw_text('Jugar', font, (255, 255, 255), self.ventana, self.button_1.centerx, self.button_1.centery)
        self.draw_text('Crear Nivel', font, (255, 255, 255), self.ventana, self.button_2.centerx, self.button_2.centery)
        self.draw_text('Salir', font, (255, 255, 255), self.ventana, self.button_3.centerx, self.button_3.centery)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                self.click = True

        pygame.display.update()
        fpsControlador.tick(60)

    def handle_click(self, pos, button):
        soundManager = SoundManager()
        soundManager.load_sound("guiclick", "Musica/guiclick.ogg")

        mx, my = pygame.mouse.get_pos()
        self.click = True
        if self.button_1.collidepoint((mx, my)) and self.click:
            soundManager.play_sound("guiclick")
            self.juego()
        if self.button_2.collidepoint((mx, my)) and self.click:
            soundManager.play_sound("guiclick")
            self.crearNivel()
        if self.button_3.collidepoint((mx, my)) and self.click:
            soundManager.play_sound("guiclick")
            self.salir()
        self.click = False

    def handle_mouse_motion(self,pos):
        pass
    def handle_key(self,event):
        if event.type == KEYDOWN and event.key == K_ESCAPE:
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

    def inputs(self):
        font = pygame.font.Font(None, 32)
        clock = pygame.time.Clock()
        rect = pygame.Rect((ventana.get_width() - 400) // 2, 200, 400, 250)
        input_box1 = pygame.Rect(rect.x+ (rect.w-140)//2, rect.y+ (rect.h-32)//3, 140, 32)
        input_box2 = pygame.Rect(rect.x+ (rect.w-140)//2, rect.y+ (rect.h-32)//3 + 50, 140, 32)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color1 = color_inactive
        color2 = color_inactive
        active1 = False
        active2 = False
        text1 = ''
        text2 = ''
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box1.collidepoint(event.pos):
                        active1 = not active1
                    else:
                        active1 = False
                    if input_box2.collidepoint(event.pos):
                        active2 = not active2
                    else:
                        active2 = False
                    color1 = color_active if active1 else color_inactive
                    color2 = color_active if active2 else color_inactive
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if text1 == '' or text2 == '':
                            return False,False
                        else:
                            return int(text1),int(text2)
                    if active1:
                        if event.key == pygame.K_BACKSPACE:
                            text1 = text1[:-1]
                        else:
                            if event.unicode.isdigit() :
                                text1 += event.unicode
                    if active2:
                        if event.key == pygame.K_RETURN:
                            print(text2)  # or process the number input
                            text2 = ''
                        elif event.key == pygame.K_BACKSPACE:
                            text2 = text2[:-1]
                        else:
                            if event.unicode.isdigit() :
                                text2 += event.unicode


           # ventana.fill((30, 30, 30))
            pygame.draw.rect(self.ventana, (0, 0, 0), rect)
            self.draw_text('Escoger dimensiones', font, (255, 255, 255), self.ventana, rect.centerx, rect.top+20)
            txt_surface1 = font.render(text1, True, color1)
            txt_surface2 = font.render(text2, True, color2)
            self.draw_text("Ancho:", font, (255, 255, 255), self.ventana, input_box1.left-50, input_box1.centery)
            self.draw_text("Alto:", font, (255, 255, 255), self.ventana, input_box2.left-50, input_box2.centery)
            #width1 = max(200, txt_surface1.get_width() + 10)
            #input_box1.w = width1
            #width2 = max(200, txt_surface1.get_width() + 10)
            #input_box2.w = width2
            self.ventana.blit(txt_surface1, (input_box1.x + 5, input_box1.y + 5))
            self.ventana.blit(txt_surface2, (input_box2.x + 5, input_box2.y + 5))
            pygame.draw.rect(self.ventana, color1, input_box1, 2)
            pygame.draw.rect(self.ventana, color2, input_box2, 2)
            pygame.display.flip()
            clock.tick(30)


class Window:
    def __init__(self, matrix):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption('Nonograma')
        self.cuadricula = MenuPrincipal(self.screen)

    def execute(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                   self.cuadricula.handle_click(event.pos, event.button)
                elif event.type == pygame.MOUSEMOTION:
                    self.cuadricula.handle_mouse_motion(event.pos)
                elif event.type == pygame.KEYDOWN:
                    self.cuadricula.handle_key(event)
            self.screen.fill(Colores.WHITE.value)
            self.cuadricula.draw()
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