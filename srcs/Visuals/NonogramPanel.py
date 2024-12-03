import pygame
from srcs.Visuals.Button import Button
from srcs.Visuals.Panel import Panel
from srcs.Visuals.Colores import Colores
from srcs.Visuals.Tutorial import mostrar_tutorial


class NonogramPanel(Panel):
    """
    Panel de Nonogram que extiende la clase Panel.
    Este panel visualiza una sección de botones para interacciones específicas dentro de un juego de Nonogram.

    Atributos:
        screen (Surface): Superficie de Pygame donde se renderiza el panel.
        width (int): Ancho del panel.
        height (int): Alto del panel.
        grilla_visual (objeto): Objeto de visualización de la grilla que responde a acciones del usuario.
        x (int): Posición X del panel en la pantalla.
        buttons (list): Lista de botones para interacciones dentro del panel.
        colores_extra (list): Lista de botones adicionales a mostrar en el panel extendido.
    """

    def __init__(self, screen, width, height, grilla_visual, colores_extra=None, dibujo : bool =False):
        """
        Inicializa el panel de Nonogram con una serie de botones de interacción.

        Args:
            screen (Surface): Superficie de Pygame donde se renderiza el panel.
            width (int): Ancho del panel.
            height (int): Alto del panel.
            grilla_visual (objeto): Objeto visual de la grilla para controlar las interacciones.
            colores_extra (list): Lista de botones extra para mostrar en un panel desplegable (opcional).
        """
        #super().__init__()
        self.screen = screen
        self.width = width
        self.height = height
        self.grilla_visual = grilla_visual
        self.x = screen.get_width() - width
        self.colores_extra = colores_extra
        self.reverse_mapping_colores = Colores.get_reverse_mapping()
        self.dibujo = dibujo
        self.BUTTON_SIZE = int(self.width / 4)
        self.margin = int(self.width / 16)

        # Crear los botones principales del panel
        if not self.dibujo:
            BUTTON_SIZE = self.BUTTON_SIZE
            self.buttons = [
                Button(screen, BUTTON_SIZE, BUTTON_SIZE, self.x + width - BUTTON_SIZE - self.margin, height - BUTTON_SIZE - self.margin,
                       Colores.WHITE.value, self.button1_action, image_path="Img/config.png", button_margin=False,
                       background_opacity=100),
                Button(screen, BUTTON_SIZE, BUTTON_SIZE, self.x + self.margin, height - BUTTON_SIZE - self.margin,
                       Colores.RED.value, self.button2_action, image_path="Img/pista.png", button_margin=False),
                Button(screen, BUTTON_SIZE, BUTTON_SIZE, self.x + self.margin, self.margin,
                       Colores.WHITE.value, self.button3_action, draw_rectangle=True, opacity=150),
                Button(screen, BUTTON_SIZE, BUTTON_SIZE, self.x + width // 2 - BUTTON_SIZE // 2, self.margin,
                       Colores.WHITE.value, self.button4_action, draw_cross=True, opacity=150),
                Button(screen, BUTTON_SIZE, BUTTON_SIZE, self.x + width - BUTTON_SIZE - self.margin, self.margin,
                       Colores.WHITE.value, self.button5_action, draw_point=True, opacity=150),
                Button(screen, BUTTON_SIZE, BUTTON_SIZE, self.x + self.margin, 2 * self.margin + BUTTON_SIZE,
                       Colores.GREEN.value, mostrar_tutorial, text="?",text_color=Colores.DARK_GREY.value)
            ]

        else:
            self.grilla_visual.right_click_value = 1
            self.buttons = []
            self._create_color_buttons()

        if colores_extra is not None:
            self.extended_panel_button_visible = True
            colors = Button(screen, BUTTON_SIZE, BUTTON_SIZE, self.x + width // 2 - BUTTON_SIZE // 2, 2 * self.margin + BUTTON_SIZE,
                            Colores.WHITE.value, self.button9_action, image_path="Img/palette.png")
            self.buttons.append(colors)
            self._create_extended_buttons()
        else:
            self.extended_panel_button_visible = False

        self.extended_panel_visible = False

    def _create_extended_buttons(self):
        """
        Crea botones adicionales que aparecen en un panel extendido al pasar el cursor sobre el botón 7.

        Returns:
            list: Lista de instancias de botones adicionales.
        """
        self.botones_extra = []
        BUTTON_SIZE = self.BUTTON_SIZE
        retroceso = Button(self.screen, BUTTON_SIZE, BUTTON_SIZE, self.x + self.margin, self.margin, Colores.WHITE.value,
                           self.button9_action, image_path="Img/retroceso_panel.png", button_margin=False)
        self.botones_extra.append(retroceso)
        retroceso = Button(self.screen, BUTTON_SIZE, BUTTON_SIZE, self.x + self.width // 2 - BUTTON_SIZE // 2,
                           self.height - BUTTON_SIZE - self.margin, Colores.RED.value, self.button9_action)
        for i, color in enumerate(self.colores_extra, start=2):
            color = Colores.get_number_mapping().get(color)
            if i % 3 == 1:
                color = Button(self.screen, BUTTON_SIZE, BUTTON_SIZE, self.x + self.margin,
                               ((i // 3) + 1) * self.margin + (i // 3) * BUTTON_SIZE,
                               color, lambda c=color: self.button10_action(c))
            elif i % 3 == 2:
                color = Button(self.screen, BUTTON_SIZE, BUTTON_SIZE, self.x + self.width // 2 - BUTTON_SIZE // 2,
                               ((i // 3) + 1) * self.margin + (i // 3) * BUTTON_SIZE, color,
                               lambda c=color: self.button10_action(c))
            else:
                color = Button(self.screen, BUTTON_SIZE, BUTTON_SIZE, self.x + self.width - BUTTON_SIZE - self.margin,
                               (i // 3) * self.margin + ((i // 3) - 1) * BUTTON_SIZE, color,
                               lambda c=color: self.button10_action(c))

            self.botones_extra.append(color)

    def _create_color_buttons(self):
        self.buttons = []
        BUTTON_SIZE = self.BUTTON_SIZE

        # Filtrar los colores que no deben ser considerados
        colores_filtrados = [color for color in self.reverse_mapping_colores if color not in [(255, 255, 255), (245, 245, 245)]]

        for i, color in enumerate(colores_filtrados):
            if i % 3 == 1:
                color = Button(self.screen, BUTTON_SIZE, BUTTON_SIZE, self.x + self.margin,
                               ((i // 3) + 1) * self.margin + (i // 3) * BUTTON_SIZE,
                               color, lambda c=color: self.button10_action(c))
            elif i % 3 == 2:
                color = Button(self.screen, BUTTON_SIZE, BUTTON_SIZE, self.x + self.width // 2 - BUTTON_SIZE // 2,
                               ((i // 3) + 1) * self.margin + (i // 3) * BUTTON_SIZE, color,
                               lambda c=color: self.button10_action(c))
            else:
                color = Button(self.screen, BUTTON_SIZE, BUTTON_SIZE, self.x + self.width - BUTTON_SIZE - self.margin,
                               (i // 3) * self.margin + ((i // 3) - 1) * BUTTON_SIZE, color,
                               lambda c=color: self.button10_action(c))

            self.buttons.append(color)


    def handle_mouse_motion(self, pos):
        """
        Gestiona el movimiento del ratón y controla la visibilidad del panel extendido al pasar sobre el botón 7.

        Args:
            pos (tuple): Posición actual del ratón.
        """
        pass

    def draw(self):
        """
        Dibuja el panel y sus botones en la superficie.
        """
        pygame.draw.rect(self.screen, Colores.KHAKI.value, pygame.Rect(self.x, 0, self.width, self.height))
        for btn in self.buttons:
            if btn:
                btn.draw()

        if self.extended_panel_visible:
            pygame.draw.rect(self.screen, Colores.LIGHT_GREY.value, pygame.Rect(self.x, 0, self.width, self.height))
            for btn in self.botones_extra:
                btn.draw()

    def handle_click(self, pos, button):
        """
        Gestiona los clics del ratón sobre los botones y los botones del panel extendido.

        Args:
            pos (tuple): Posición del clic del ratón.
            button (int): Código del botón presionado (e.g., botón izquierdo o derecho).
        """
        if not self.extended_panel_visible:
            for btn in self.buttons:
                if btn and btn.is_clicked(pos):
                    btn.click()
                    break
        else:
            for btn in self.botones_extra:
                if btn and btn.is_clicked(pos):
                    btn.click()
                    break

    def handle_key(self, event):
        """
        Maneja las pulsaciones de teclas en el panel.

        Args:
            key (int): Código de la tecla presionada.
        """
        if event.key == pygame.K_c:
            if self.extended_panel_visible:
                self.extended_panel_visible = False
            else:
                self.extended_panel_visible = True

    # Acciones de los botones (ejemplos)
    def button1_action(self):
        """
        Acción del botón 1. Imprime un mensaje de configuración.
        """
        print("Boton configuracion")

    def button2_action(self):
        """
        Acción del botón 2. Imprime un mensaje de pista.
        """
        print("Boton pistas")
        self.grilla_visual.pista()

    def button3_action(self):
        """
        Acción del botón 3. Configura los valores de clic izquierdo y derecho en la grilla visual.
        """
        self.grilla_visual.left_click_value = 1
        self.grilla_visual.right_click_value = -1

    def button4_action(self):
        """
        Acción del botón 4. Cambia los valores de clic izquierdo y derecho en la grilla v
        isual.
        """
        self.grilla_visual.left_click_value = -1
        self.grilla_visual.right_click_value = 1

    def button5_action(self):
        """
        Acción del botón 5. Establece valores específicos de clic para la grilla visual.
        """
        self.grilla_visual.left_click_value = -2
        self.grilla_visual.right_click_value = -1

    def button6_action(self):
        """
        Acción del botón 6.
        """
        print("Boton 6")

    def button7_action(self):
        """
        Acción del botón 7.
        """
        print("Boton 7")

    def button8_action(self):
        """
        Acción del botón 8.
        """
        print("Boton 8")

    def button9_action(self):
        """
        Acción del botón 9.
        """
        if self.extended_panel_visible:
            self.extended_panel_visible = False
        else:
            self.extended_panel_visible = True

    def button10_action(self, color):
        """
        Acción del botón 10.
        """
        self.grilla_visual.left_click_value = self.reverse_mapping_colores.get(color)