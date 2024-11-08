import pygame
from srcs.Visuals.Button import Button
from srcs.Visuals.Panel import Panel
from srcs.Visuals.Colores import Colores

BUTTON_SIZE = 50


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
    """

    def __init__(self, screen, width, height, grilla_visual):
        """
        Inicializa el panel de Nonogram con una serie de botones de interacción.

        Args:
            screen (Surface): Superficie de Pygame donde se renderiza el panel.
            width (int): Ancho del panel.
            height (int): Alto del panel.
            grilla_visual (objeto): Objeto visual de la grilla para controlar las interacciones.
        """
        super().__init__()
        self.screen = screen
        self.width = width
        self.height = height
        self.grilla_visual = grilla_visual
        self.x = screen.get_width() - width  # Ubica el panel en la posición X del lado derecho.

        # Configuración de los botones con posiciones, colores y acciones específicas.
        self.buttons = [
            Button(screen, BUTTON_SIZE, BUTTON_SIZE, self.x + width - BUTTON_SIZE - 10, height - BUTTON_SIZE - 10,
                   Colores.BLUE.value, self.button1_action, image_path="Img/config.png"),
            Button(screen, BUTTON_SIZE, BUTTON_SIZE, self.x + 10, height - BUTTON_SIZE - 10,
                   Colores.RED.value, self.button2_action, image_path="Img/pista.png"),
            Button(screen, BUTTON_SIZE, BUTTON_SIZE, self.x + 10, 10,
                   Colores.WHITE.value, self.button3_action, draw_rectangle=True, opacity=150),
            Button(screen, BUTTON_SIZE, BUTTON_SIZE, self.x + width // 2 - BUTTON_SIZE // 2, 10,
                   Colores.WHITE.value, self.button4_action, draw_cross=True, opacity=150),
            Button(screen, BUTTON_SIZE, BUTTON_SIZE, self.x + width - BUTTON_SIZE - 10, 10,
                   Colores.WHITE.value, self.button5_action, draw_point=True, opacity=150)
        ]

    def handle_click(self, pos, button):
        """
        Gestiona los clics del ratón sobre los botones.

        Args:
            pos (tuple): Posición del clic del ratón.
            button (int): Código del botón presionado (e.g., botón izquierdo o derecho).
        """
        for btn in self.buttons:
            if btn.is_clicked(pos):  # Verifica si el botón fue clicado en la posición.
                btn.click()  # Ejecuta la acción asociada al botón.
                break

    def handle_key(self, event):
        """
        Gestiona eventos de teclado. No implementado.

        Args:
            event (Event): Evento de teclado capturado.
        """
        pass  # Actualmente no se maneja ningún evento de teclado.

    def handle_mouse_motion(self, pos):
        """
        Gestiona el movimiento del ratón. No implementado.

        Args:
            pos (tuple): Posición actual del ratón.
        """
        pass  # Actualmente no se maneja el movimiento del ratón.

    def draw(self):
        """
        Dibuja el panel y sus botones en la superficie.
        """
        # Dibuja el fondo del panel con un color Khaki.
        pygame.draw.rect(self.screen, Colores.KHAKI.value, pygame.Rect(self.x, 0, self.width, self.height))
        # Dibuja cada botón en la lista de botones.
        for btn in self.buttons:
            btn.draw()

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

    def button3_action(self):
        """
        Acción del botón 3. Configura los valores de clic izquierdo y derecho en la grilla visual.
        """
        self.grilla_visual.left_click_value = 1
        self.grilla_visual.right_click_value = -1

    def button4_action(self):
        """
        Acción del botón 4. Cambia los valores de clic izquierdo y derecho en la grilla visual.
        """
        self.grilla_visual.left_click_value = -1
        self.grilla_visual.right_click_value = 1

    def button5_action(self):
        """
        Acción del botón 5. Establece valores específicos de clic para la grilla visual.
        """
        self.grilla_visual.left_click_value = -2
        self.grilla_visual.right_click_value = -1