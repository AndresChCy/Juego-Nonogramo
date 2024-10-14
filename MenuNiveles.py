import pygame
import sys
from pygame.locals import *

from Panel import Panel

pygame.init()
pygame.display.set_caption('Juego Nonogram')
ventana = pygame.display.set_mode((800, 600), 0, 32)
fpsControlador = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

class MenuNiveles:
    def __init__(self, ventana, lista):
        self.click = False
        self.listaNiveles = lista
        self.numNiveles = len(lista)
        self.nivelesPorPagina = 6
        self.numPaginas = (self.numNiveles+self.nivelesPorPagina-1)//self.nivelesPorPagina
        self.paginaActual = 0
        self.ejecutando = True

        while self.ejecutando:
            ventana.fill((0,0,0))
            self.draw_text('Niveles', font, (255, 255, 255), ventana, ventana.get_width()//2, 100)
            mx, my = pygame.mouse.get_pos()
            self.draw_page(ventana)

            #-----------------------------CREANDO BOTONES----------------------------------   (se repite en draw_page)
            button_width, button_height, espacio = 200, 50, 50
            ladoIzquierdo = ventana.get_width()//2-button_width-espacio//2
            ladoDerecho = ventana.get_width()//2+espacio//2
            inicio = self.paginaActual*self.nivelesPorPagina
            fin = min(inicio+self.nivelesPorPagina, self.numNiveles)

            botones = []
            for i in range(inicio, fin):
                fila = (i-inicio)//2
                columna = (i-inicio)%2

                if columna == 0:
                    x = ladoIzquierdo
                else:
                    x = ladoDerecho
                y = 150+(fila*100)
                botones.append(pygame.Rect(x, y, button_width, button_height))
            #-----------------------------CREANDO BOTONES------------------------------------ (se repite en draw_page)

            #parte que dibuja los botones de navegacion
            ancho_flechas = 50
            alto_flechas = 30
            margen_inferior = 20
            boton_izquierda = pygame.Rect(ventana.get_width()//4 - ancho_flechas//2, ventana.get_height()-alto_flechas-margen_inferior, ancho_flechas, alto_flechas)
            boton_derecha = pygame.Rect(3 * ventana.get_width()//4 - ancho_flechas//2, ventana.get_height()-alto_flechas-margen_inferior, ancho_flechas, alto_flechas)
            pygame.draw.rect(ventana, (100, 100, 100), boton_izquierda)
            pygame.draw.rect(ventana, (100, 100, 100), boton_derecha)
            self.draw_text('<<', font, (255, 255, 255), ventana, boton_izquierda.centerx, boton_izquierda.centery)
            self.draw_text('>>', font, (255, 255, 255), ventana, boton_derecha.centerx, boton_derecha.centery)

            #parte de manejo de eventos
            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    self.ejecutando = False
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    click = True

            #parte de accionar de los botones de navegacion
            if boton_izquierda.collidepoint(mx, my) and self.paginaActual>0 and click:
                self.paginaActual -= 1
            if boton_derecha.collidepoint(mx, my) and self.paginaActual<self.numPaginas-1 and click:
                self.paginaActual += 1

            #parte para la interaccion delos botones
            for numBoton, boton in enumerate(botones,start=self.paginaActual*self.nivelesPorPagina+1):
                if boton.collidepoint(mx, my) and click:
                    self.botonClick(numBoton)

            #mantener fotogramas
            pygame.display.update()
            fpsControlador.tick(60)

    def draw_page(self, ventana):
        button_width = 200
        button_height = 50
        espacio = 50
        ladoIzquierdo = ventana.get_width()//2-button_width-espacio//2
        ladoDerecho = ventana.get_width()//2+espacio//2

        inicio = self.paginaActual*self.nivelesPorPagina
        fin = min(inicio+self.nivelesPorPagina, self.numNiveles)

        botones = []
        for i in range(inicio, fin):
            fila = (i-inicio)//2
            columna = (i-inicio)%2

            if columna == 0:
                x = ladoIzquierdo
            else:
                x = ladoDerecho
            y = 150+(fila*100)
            botones.append(pygame.Rect(x, y, button_width, button_height))

        for numBoton, boton in enumerate(botones, start=inicio+1):
            pygame.draw.rect(ventana, (255, 0, 0), boton)
            self.draw_text(f'Nivel {numBoton}', font, (255, 255, 255), ventana, boton.centerx, boton.centery)

    def draw_text(self, texto, font, color, superficie, x, y):
        textobj = font.render(texto, 1, color)
        textrect = textobj.get_rect(center=(x, y))
        superficie.blit(textobj, textrect)

    def botonClick(self,n):
        print("Se ha presionado el botón:",n)

if __name__ == "__main__":
    MenuNiveles(ventana, [1,2,3,4,5,6,7,8,9])
