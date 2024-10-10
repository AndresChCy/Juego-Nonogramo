import pygame
import sys
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Juego Nonogram')
ventana = pygame.display.set_mode((800, 600), 0, 32)
fpsControlador = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

def draw_text(texto, font, color, superficie, x, y):
    textobj = font.render(texto, 1, color)
    textrect = textobj.get_rect(center=(x,y))
    superficie.blit(textobj, textrect)

click = False
def Menu_Principal():
    global click
    while True:
        ventana.fill((0, 0, 0))
        draw_text('Menu Principal', font, (255, 255, 255), ventana, ventana.get_width()//2, 100)

        mx, my = pygame.mouse.get_pos()
        button_width = 200
        button_height = 50
        button_1 = pygame.Rect((ventana.get_width()-button_width)//2, 200, button_width, button_height)
        button_2 = pygame.Rect((ventana.get_width()-button_width)//2, 300, button_width, button_height)
        button_3 = pygame.Rect((ventana.get_width()-button_width)//2, 400, button_width, button_height)

        if button_1.collidepoint((mx, my)) and click:
            juego()
        if button_2.collidepoint((mx, my)) and click:
            opciones()
        if button_3.collidepoint((mx, my)) and click:
            salir()

        pygame.draw.rect(ventana, (255, 0, 0), button_1)
        pygame.draw.rect(ventana, (255, 0, 0), button_2)
        pygame.draw.rect(ventana, (255, 0, 0), button_3)

        draw_text('Jugar', font, (255, 255, 255), ventana, button_1.centerx, button_1.centery)
        draw_text('Opciones', font, (255, 255, 255), ventana, button_2.centerx, button_2.centery)
        draw_text('Salir', font, (255, 255, 255), ventana, button_3.centerx, button_3.centery)


        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN and event.key==K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type==MOUSEBUTTONDOWN and event.button==1:
                click = True

        pygame.display.update()
        fpsControlador.tick(60)

def juego():
    ejecutando=True
    while ejecutando:
        ventana.fill((0,0,0))
        draw_text('Juego', font, (255, 255, 255), ventana, ventana.get_width()//2, ventana.get_height()//2)

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN and event.key==K_ESCAPE:
                ejecutando=False

        pygame.display.update()
        fpsControlador.tick(60)

def opciones():
    ejecutando=True
    while ejecutando:
        ventana.fill((0,0,0))
        draw_text('Opciones', font, (255, 255, 255), ventana, ventana.get_width()//2, ventana.get_height()//2)

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN and event.key==K_ESCAPE:
                ejecutando=False

        pygame.display.update()
        fpsControlador.tick(60)

def salir():
    pygame.quit()
    sys.exit()

Menu_Principal()
