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
            Button(screen, "1", BUTTON_SIZE, BUTTON_SIZE, self.x + width - BUTTON_SIZE - 10, height - BUTTON_SIZE - 10, Colores.BLUE.value, Colores.WHITE.value, self.button1_action),
            Button(screen, "2", BUTTON_SIZE, BUTTON_SIZE, self.x + 10, height - BUTTON_SIZE - 10, Colores.RED.value, Colores.WHITE.value, self.button2_action),
            Button(screen, "3", BUTTON_SIZE, BUTTON_SIZE, self.x + 10, 10, Colores.BROWN.value, Colores.WHITE.value, self.button3_action),
            Button(screen, "4", BUTTON_SIZE, BUTTON_SIZE, self.x + width // 2 - BUTTON_SIZE // 2, 10, Colores.YELLOW.value, Colores.BLACK.value, self.button4_action),
            Button(screen, "5", BUTTON_SIZE, BUTTON_SIZE, self.x + width - BUTTON_SIZE - 10, 10, Colores.MAGENTA.value, Colores.WHITE.value, self.button5_action)
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
        pygame.draw.rect(self.screen, Colores.GREEN.value, pygame.Rect(self.x, 0, self.width, self.height))
        for btn in self.buttons:
            btn.draw()

    def button1_action(self):
        print("Button 1 clicked!")

    def button2_action(self):
        print("Button 2 clicked!")

    def button3_action(self):
        print("Button 3 clicked!")
        self.grilla_visual.left_click_value = 1
        self.grilla_visual.right_click_value = -1

    def button4_action(self):
        print("Button 4 clicked!")
        self.grilla_visual.left_click_value = -1
        self.grilla_visual.right_click_value = 1

    def button5_action(self):
        print("Button 5 clicked!")