import pygame
import sys
from pygame.locals import *
from MenuNiveles import MenuNiveles
from Colores import Colores
from Panel import Panel

pygame.init()
pygame.display.set_caption('Juego Nonogram')
ventana = pygame.display.set_mode((800, 600), 0, 32)
fpsControlador = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)


#click = False
class MenuPrincipal(Panel):

    def __init__(self,ventana):
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.click = False
        ventana.fill((0, 0, 0))
        button_width = 200
        button_height = 50
        self.button_1 = pygame.Rect((ventana.get_width() - button_width) // 2, 200, button_width, button_height)
        self.button_2 = pygame.Rect((ventana.get_width() - button_width) // 2, 300, button_width, button_height)
        self.button_3 = pygame.Rect((ventana.get_width() - button_width) // 2, 400, button_width, button_height)


    def draw_text(self,texto, font, color, superficie, x, y):
        textobj = font.render(texto, 1, color)
        textrect = textobj.get_rect(center=(x, y))
        superficie.blit(textobj, textrect)

    def draw(self):
        pygame.draw.rect(ventana, (255, 0, 0), self.button_1)
        pygame.draw.rect(ventana, (255, 0, 0), self.button_2)
        pygame.draw.rect(ventana, (255, 0, 0), self.button_3)

        self.draw_text('Jugar', font, (255, 255, 255), ventana, self.button_1.centerx, self.button_1.centery)
        self.draw_text('Opciones', font, (255, 255, 255), ventana, self.button_2.centerx, self.button_2.centery)
        self.draw_text('Salir', font, (255, 255, 255), ventana, self.button_3.centerx, self.button_3.centery)

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
        mx, my = pygame.mouse.get_pos()
        self.click = True
        if self.button_1.collidepoint((mx, my)) and self.click:
            self.juego()
        if self.button_2.collidepoint((mx, my)) and self.click:
            self.opciones()
        if self.button_3.collidepoint((mx, my)) and self.click:
            self.salir()
        self.click = False

    def handle_mouse_motion(self,pos):
        pass
    def handle_key(self,event):
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()


    def juego(self):
        MenuNiveles(ventana,[1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18])

    def opciones(self):
        ejecutando=True
        while ejecutando:
            ventana.fill((0,0,0))
            self.draw_text('Opciones', font, (255, 255, 255), ventana, ventana.get_width()//2, ventana.get_height()//2)

            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==KEYDOWN and event.key==K_ESCAPE:
                    ejecutando=False

            pygame.display.update()
            fpsControlador.tick(60)

    def salir(self):
        pygame.quit()
        sys.exit()


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
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    Window(matrix).execute()
    #MenuPrincipal(ventana)