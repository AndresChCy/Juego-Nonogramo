import pygame
from pygame.locals import *

from srcs.Logica.Dibujo import Dibujo
from srcs.Visuals.Grid import Grid
from Panel import Panel
from ProxyPanel import ProxyPanel
from srcs.Logica.Tablero import Tablero
from srcs.Visuals.Grilla.GrillaDecorator import DecoratorClues, DecoratorMiniatureRender
from srcs.Visuals.Grilla.GrillaVisual import GrillaVisual

pygame.init()
pygame.display.set_caption('Juego Nonogram')
ventana = pygame.display.set_mode((800, 600), 0, 32)
fpsControlador = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

class MenuNiveles(Panel):
    def __init__(self, ventana, lista, proxy : ProxyPanel):
        self.ventana = ventana
        self.proxy = proxy
        self.click = False
        self.listaNiveles = lista
        self.numNiveles = len(lista)
        self.nivelesPorPagina = 6
        self.numPaginas = (self.numNiveles+self.nivelesPorPagina-1)//self.nivelesPorPagina
        self.paginaActual = 0
        self.ejecutando = True
        self.botones = []
        ancho_flechas = 50
        alto_flechas = 30
        margen_inferior = 20

        self.boton_izquierda = pygame.Rect(ventana.get_width() // 4 - ancho_flechas // 2,
                                      ventana.get_height() - alto_flechas - margen_inferior, ancho_flechas,
                                      alto_flechas)
        self.boton_derecha = pygame.Rect(3 * ventana.get_width() // 4 - ancho_flechas // 2,
                                    ventana.get_height() - alto_flechas - margen_inferior, ancho_flechas, alto_flechas)


    def draw_page(self, ventana):
        button_width = 200
        button_height = 50
        espacio = 50
        ladoIzquierdo = ventana.get_width()//2-button_width-espacio//2
        ladoDerecho = ventana.get_width()//2+espacio//2

        inicio = self.paginaActual*self.nivelesPorPagina
        fin = min(inicio+self.nivelesPorPagina, self.numNiveles)

        self.botones = []
        for i in range(inicio, fin):
            fila = (i-inicio)//2
            columna = (i-inicio)%2

            if columna == 0:
                x = ladoIzquierdo
            else:
                x = ladoDerecho
            y = 150+(fila*100)
            self.botones.append(pygame.Rect(x, y, button_width, button_height))

        for numBoton, boton in enumerate(self.botones, start=inicio+1):
            pygame.draw.rect(ventana, (255, 0, 0), boton)
            self.draw_text(f'Nivel {numBoton}', font, (255, 255, 255), ventana, boton.centerx, boton.centery)

    def draw_text(self, texto, font, color, superficie, x, y):
        textobj = font.render(texto, 1, color)
        textrect = textobj.get_rect(center=(x, y))
        superficie.blit(textobj, textrect)

    def botonClick(self,n):
        print("a")
        print("Se ha presionado el botón:",n)

        matrix = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        ]
        aux = Dibujo(1, 1)
        aux.cargarMatriz("Niveles/nivel1")
        g = GrillaVisual(self.ventana, self.listaNiveles[n-1], self.proxy,None)
        gc = DecoratorClues(g)
        gcm = DecoratorMiniatureRender(gc)
        self.proxy.ponerTarget(gcm)

    def handle_mouse_motion(self, event):
        pass

    def handle_click(self, pos, button):
        mx, my = pos
        click = False
        if button == 1:
                click = True

            # parte de accionar de los botones de navegacion

        if self.boton_izquierda.collidepoint(mx, my) and self.paginaActual > 0 and click:
            self.paginaActual -= 1
        if self.boton_derecha.collidepoint(mx, my) and self.paginaActual < self.numPaginas - 1 and click:
            self.paginaActual += 1

            # parte para la interaccion delos botones
        for numBoton, boton in enumerate(self.botones, start=self.paginaActual * self.nivelesPorPagina + 1):
            if boton.collidepoint(mx, my) and click:
                self.botonClick(numBoton)


    def handle_key(self, event):
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            self.proxy.cambiarTarget(0)

    def draw(self):
        self.ventana.fill((0, 0, 0))
        self.draw_text('Niveles', font, (255, 255, 255), self.ventana, ventana.get_width() // 2, 100)
        mx, my = pygame.mouse.get_pos()
        self.draw_page(self.ventana)

        # -----------------------------CREANDO BOTONES----------------------------------   (se repite en draw_page)
        button_width, button_height, espacio = 200, 50, 50
        ladoIzquierdo = self.ventana.get_width() // 2 - button_width - espacio // 2
        ladoDerecho = self.ventana.get_width() // 2 + espacio // 2
        inicio = self.paginaActual * self.nivelesPorPagina
        fin = min(inicio + self.nivelesPorPagina, self.numNiveles)

        botones = []
        for i in range(inicio, fin):
            fila = (i - inicio) // 2
            columna = (i - inicio) % 2

            if columna == 0:
                x = ladoIzquierdo
            else:
                x = ladoDerecho
            y = 150 + (fila * 100)
            botones.append(pygame.Rect(x, y, button_width, button_height))
        # -----------------------------CREANDO BOTONES------------------------------------ (se repite en draw_page)

        # parte que dibuja los botones de navegacion
        pygame.draw.rect(ventana, (100, 100, 100), self.boton_izquierda)
        pygame.draw.rect(ventana, (100, 100, 100), self.boton_derecha)
        self.draw_text('<<', font, (255, 255, 255), ventana, self.boton_izquierda.centerx, self.boton_izquierda.centery)
        self.draw_text('>>', font, (255, 255, 255), ventana, self.boton_derecha.centerx, self.boton_derecha.centery)
        pygame.display.update()
        fpsControlador.tick(60)
if __name__ == "__main__":
    MenuNiveles(ventana, [1,2,3,4,5,6,7,8,9])
