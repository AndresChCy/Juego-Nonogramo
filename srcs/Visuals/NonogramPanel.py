import pygame
from srcs.Visuals.Button import Button
from srcs.Visuals.Panel import Panel
from srcs.Visuals.Colores import Colores

BUTTON_SIZE = 50

class NonogramPanel(Panel):
    def __init__(self, screen, width, height, grilla_visual):
        super().__init__()
        self.screen = screen
        self.width = width
        self.height = height
        self.grilla_visual = grilla_visual
        self.x = screen.get_width() - width

        self.buttons = [
            Button(screen, BUTTON_SIZE, BUTTON_SIZE, self.x + width - BUTTON_SIZE - 10, height - BUTTON_SIZE - 10, Colores.BLUE.value, Colores.WHITE.value, self.button1_action, image_path="../../Img/config.png"),
            Button(screen, BUTTON_SIZE, BUTTON_SIZE, self.x + 10, height - BUTTON_SIZE - 10, Colores.RED.value, Colores.WHITE.value, self.button2_action, image_path="../../Img/pista.png"),
            Button(screen, BUTTON_SIZE, BUTTON_SIZE, self.x + 10, 10, Colores.WHITE.value, Colores.WHITE.value, self.button3_action, draw_rectangle=True, opacity=150),
            Button(screen, BUTTON_SIZE, BUTTON_SIZE, self.x + width // 2 - BUTTON_SIZE // 2, 10, Colores.WHITE.value, Colores.BLACK.value, self.button4_action, draw_cross=True, opacity=150),
            Button(screen, BUTTON_SIZE, BUTTON_SIZE, self.x + width - BUTTON_SIZE - 10, 10, Colores.WHITE.value, Colores.WHITE.value, self.button5_action, draw_point=True, opacity=150)
        ]

    def handle_click(self, pos, button):
        for btn in self.buttons:
            if btn.is_clicked(pos):
                btn.click()
                break

    def handle_key(self, event):
        pass

    def handle_mouse_motion(self, pos):
        pass

    def draw(self):
        pygame.draw.rect(self.screen, Colores.KHAKI.value, pygame.Rect(self.x, 0, self.width, self.height))
        for btn in self.buttons:
            btn.draw()

    def button1_action(self):
        print("Boton pistas")

    def button2_action(self):
        print("Boton configuracion")

    def button3_action(self):
        self.grilla_visual.left_click_value = 1
        self.grilla_visual.right_click_value = -1

    def button4_action(self):
        self.grilla_visual.left_click_value = -1
        self.grilla_visual.right_click_value = 1

    def button5_action(self):
        self.grilla_visual.left_click_value = -2
        self.grilla_visual.right_click_value = -1