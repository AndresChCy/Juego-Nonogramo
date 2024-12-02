import pygame

from Musica.SoundManager import SoundManager
from srcs.Visuals.Grilla.CellManager import CellManager
from srcs.Visuals.Colores import Colores
from srcs.Visuals.FrameLoader import FrameLoader
from srcs.Visuals.Panel import Panel
from srcs.Visuals.ProxyPanel import ProxyPanel
from srcs.Visuals.VictoryMiniatureRenderer import VictoryMiniatureRenderer
from srcs.Visuals.TextRenderer import TextRenderer
from srcs.Visuals.ImageRenderer import ImageRenderer

class VictoryRenderer(Panel):
    def __init__(self, screen,proxy: ProxyPanel ,grid_logic, cell_manager):
        """
        Inicializa el renderizador de la pantalla de victoria.

        Args:
            screen (pygame.Surface): La superficie de la pantalla.
            grid_logic (list): La lógica de la cuadrícula.
            cell_manager (CellManager): El gestor de celdas.
        """
        self.proxy = proxy
        self.screen = screen
        miniature_width = screen.get_width() // 3
        miniature_height = miniature_width

        # Inicializa los renderizadores de texto
        self.title_renderer = TextRenderer(screen, 'Title.otf', int(screen.get_height() // 6.5), Colores.ORANGE.value)
        self.body_renderer = TextRenderer(screen, 'Body.ttf', int(screen.get_height() // (6.5 * 2)), Colores.WHITE.value)

        # Inicializa el renderizador de la miniatura
        self.miniature_renderer = VictoryMiniatureRenderer(screen, grid_logic, screen.get_width() // 2 - miniature_width // 2,
                                                           screen.get_height() // 5 + int(screen.get_height() // 6.5), cell_manager, miniature_width,
                                                           miniature_height)

        # Inicializa los renderizadores de imágenes
        image_size = (screen.get_width() // 3, screen.get_width() // 3)
        self.left_image_renderer = ImageRenderer(screen, FrameLoader('Gifs_Divididos/Confetti').get_frames(), flip_x=True, size=image_size)
        self.right_image_renderer = ImageRenderer(screen, FrameLoader('Gifs_Divididos/Confetti').get_frames(), size=image_size)
        self.fullscreen_image_renderer = ImageRenderer(screen, FrameLoader('Gifs_Divididos/Confetti_Fullscreen').get_frames(), size=(screen.get_width(), screen.get_height()))

        self.soundManager = SoundManager()
        self.soundManager.stop_all()
        #self.soundManager.load_sound("victory", "Musica/victory.mp3")

        self.soundManager.play_sound("victory")

    def draw(self):
        """
        Dibuja la pantalla de victoria.
        """
        # Dibuja la imagen de fondo a pantalla completa
        self.screen.fill(Colores.BLACK.value)
        self.fullscreen_image_renderer.draw((self.screen.get_width() // 2, self.screen.get_height() // 2))

        # Renderiza el título
        self.title_renderer.render("Victoria", (self.screen.get_width() // 2 - int(self.screen.get_width() // 40), self.screen.get_height() // 5 - int(self.screen.get_width() // 40)))

        # Dibuja las imágenes a los lados del título
        left_image_position = (self.screen.get_width() // 6, self.screen.get_height() // 5 + int(self.screen.get_height() // 26))
        right_image_position = (self.screen.get_width() // 6 * 5, self.screen.get_height() // 5 + int(self.screen.get_height() // 26))
        self.left_image_renderer.draw(left_image_position)
        self.right_image_renderer.draw(right_image_position)

        # Dibuja la miniatura
        self.miniature_renderer.miniature_offset_y = self.screen.get_height() // 4
        self.miniature_renderer.draw_miniature()

        # Renderiza el mensaje debajo de la miniatura
        new_message_position = (self.screen.get_width() // 2, self.miniature_renderer.miniature_offset_y + self.miniature_renderer.height + int(self.screen.get_height() // 30))
        self.body_renderer.render("Pulse en cualquier parte para volver al Inicio.", new_message_position)

    def handle_mouse_motion(self, event):
        pass

    def handle_click(self, pos, button):
        self.soundManager.stop_all()
        self.soundManager.play_music()
        self.proxy.cambiarTarget(0)
        self.screen = pygame.display.set_mode((1000, 650))

    def handle_key(self, event):
        pass

#Código de prueba
def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption("Victory Panel Test")
    clock = pygame.time.Clock()

    # Example grid logic and cell manager
    grid_logic = [
        [1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
        [1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
        [1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
        [1, 0, 0, 1, 0, 0, 1, 0, 0, 1]
    ]
    cell_size = 30
    offset_x = 50
    offset_y = 50
    cell_manager = CellManager(len(grid_logic[0]), len(grid_logic), cell_size, offset_x, offset_y)

    victory_renderer = VictoryRenderer(screen, grid_logic, cell_manager)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(Colores.BLACK.value)
        victory_renderer.draw()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()