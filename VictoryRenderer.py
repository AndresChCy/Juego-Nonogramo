import pygame
from CellManager import CellManager
from Colores import Colores
from FrameLoader import FrameLoader
from VictoryMiniatureRenderer import VictoryMiniatureRenderer
from TextRenderer import TextRenderer
from ImageRenderer import ImageRenderer

class VictoryRenderer:
    def __init__(self, screen, grid_logic, cell_manager):
        """
        Inicializa el renderizador de la pantalla de victoria.

        Args:
            screen (pygame.Surface): La superficie de la pantalla.
            grid_logic (list): La lógica de la cuadrícula.
            cell_manager (CellManager): El gestor de celdas.
        """
        self.screen = screen
        miniature_width = screen.get_width() // 3
        miniature_height = miniature_width

        # Inicializa los renderizadores de texto
        self.title_renderer = TextRenderer(screen, 'Title.otf', 100, Colores.ORANGE.value)
        self.body_renderer = TextRenderer(screen, 'Body.ttf', 50, Colores.WHITE.value)

        # Inicializa el renderizador de la miniatura
        self.miniature_renderer = VictoryMiniatureRenderer(screen, grid_logic, screen.get_width() // 2 - miniature_width // 2,
                                                           screen.get_height() // 5 + 100, cell_manager, miniature_width,
                                                           miniature_height)

        # Inicializa los renderizadores de imágenes
        self.left_image_renderer = ImageRenderer(screen, FrameLoader('Gifs_Divididos/Confetti').get_frames(), flip_x=True)
        self.right_image_renderer = ImageRenderer(screen, FrameLoader('Gifs_Divididos/Confetti').get_frames())
        self.fullscreen_image_renderer = ImageRenderer(screen, FrameLoader('Gifs_Divididos/Confetti_Fullscreen').get_frames())

    def draw(self):
        """
        Dibuja la pantalla de victoria.
        """
        # Dibuja la imagen de fondo a pantalla completa
        self.fullscreen_image_renderer.draw((self.screen.get_width() // 2, self.screen.get_height() // 2))

        # Renderiza el título
        self.title_renderer.render("Victoria", (self.screen.get_width() // 2 - 25, self.screen.get_height() // 5 + 25))

        # Dibuja las imágenes a los lados del título
        left_image_position = (self.screen.get_width() // 6, self.screen.get_height() // 5 + 25)
        right_image_position = (self.screen.get_width() // 6 * 5, self.screen.get_height() // 5 + 25)
        self.left_image_renderer.draw(left_image_position)
        self.right_image_renderer.draw(right_image_position)

        # Dibuja la miniatura
        self.miniature_renderer.draw_miniature()

        # Renderiza el mensaje debajo de la miniatura
        new_message_position = (self.screen.get_width() // 2, self.miniature_renderer.miniature_offset_y + self.miniature_renderer.height + 75)
        self.body_renderer.render("Pulse en cualquier parte para volver al Inicio.", new_message_position)


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