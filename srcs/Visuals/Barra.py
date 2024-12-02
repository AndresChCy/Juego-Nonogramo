import pygame
import sys

from srcs.Visuals.Colores import Colores
from srcs.Visuals.Panel import Panel



# Clase Slider
class Slider(Panel):
    def __init__(self, x, y, w, h, min_val, max_val, start_val ,screen):
        self.rect = pygame.Rect(x, y, w, h)
        self.min_val = min_val
        self.max_val = max_val
        self.val = start_val
        self.grab = False
        self.handle_rect = pygame.Rect(x, y, w, h // 20)
        self.surface = screen
    def draw(self):
        # Dibujar la barra
        pygame.draw.rect(self.surface, Colores.GREY.value, self.rect)
        # Dibujar el indicador de posición
        handle_y = self.rect.y + (self.val - self.min_val) / (self.max_val - self.min_val) * self.rect.h
        self.handle_rect.topleft = (self.rect.x, handle_y)
        pygame.draw.rect(self.surface, Colores.RED.value if self.grab else Colores.GREEN.value, self.handle_rect)

    def handle_click(self, pos,button):
        if self.handle_rect.collidepoint(pos):
            self.grab = True
        else:
            self.grab = False


    def handle_key(self,event):
        pass

    def handle_mouse_motion(self,pos):
        if self.grab:
            mouse_y = pos[1]
            self.val = self.min_val + (mouse_y - self.rect.y) / self.rect.h * (self.max_val - self.min_val)
            self.val = max(self.min_val, min(self.max_val, self.val))

    def handle_clickUp(self,event):
        if event.type == pygame.MOUSEBUTTONUP:
            self.grab = False

    def get_value(self):
        return self.val


# Crear una instancia del slider
