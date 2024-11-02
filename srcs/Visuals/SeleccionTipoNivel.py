import pygame
from Panel import Panel
from ProxyPanel import ProxyPanel

pygame.init()
pygame.display.set_caption('Juego Nonogram')
ventana = pygame.display.set_mode((800, 600), 0, 32)
fpsControlador = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

class SeleccionTipoNivel(Panel):
    def __init__(self, ventana, proxy: ProxyPanel):
        self.ventana = ventana
        self.proxy = proxy
        self.click = False
        button_width = 220
        button_height = 50

        self.button_niveles = pygame.Rect((ventana.get_width() - button_width) // 2, 200, button_width, button_height)
        self.button_ninveles_creados = pygame.Rect((ventana.get_width() - button_width) // 2, 300, button_width, button_height)
        self.button_al_azar = pygame.Rect((ventana.get_width() - button_width) // 2, 400, button_width, button_height)


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

    def handle_click(self, pos, button):
        mx, my = pos
        click = False
        if button == 1:
            click = True

    def handle_key(self,event):
        pass


if __name__ == '__main__':
    SeleccionTipoNivel(ventana, ProxyPanel())