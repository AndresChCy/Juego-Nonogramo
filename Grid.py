# Grid.py
import pygame
from CellManager import CellManager
from ClueGenerator import ClueGenerator
from GridRenderer import GridRenderer

class Grid:
    GRID_WIDTH_PX = 600
    GRID_HEIGHT_PX = 600

    def __init__(self, screen, grid_width=10, grid_height=10):
        pygame.init()
        self.screen = screen
        self.GRID_WIDTH = grid_width
        self.GRID_HEIGHT = grid_height
        self.window_width, self.window_height = screen.get_size()
        self.CELL_SIZE = min(self.GRID_WIDTH_PX // self.GRID_WIDTH, self.GRID_HEIGHT_PX // self.GRID_HEIGHT)
        self.actual_grid_width_px = self.GRID_WIDTH * self.CELL_SIZE
        self.actual_grid_height_px = self.GRID_HEIGHT * self.CELL_SIZE
        self.offset_x = (self.window_width - self.actual_grid_width_px) // 2
        self.offset_y = (self.window_height - self.actual_grid_height_px) // 2
        self.grid_logic = [[0 for _ in range(self.GRID_WIDTH)] for _ in range(self.GRID_HEIGHT)]
        self.cell_manager = CellManager(self.GRID_WIDTH, self.GRID_HEIGHT, self.CELL_SIZE, self.offset_x, self.offset_y)
        self.clue_generator = ClueGenerator(self.grid_logic)
        self.renderer = GridRenderer(self.screen, self.cell_manager, self.clue_generator, self.grid_logic, self.offset_x, self.offset_y, self.CELL_SIZE)
        self.clock = pygame.time.Clock()
        self.FPS = 60

    def handle_click(self, pos):
        mouse_x, mouse_y = pos
        col = (mouse_x - self.offset_x) // self.CELL_SIZE
        row = (mouse_y - self.offset_y) // self.CELL_SIZE
        if 0 <= col < self.GRID_WIDTH and 0 <= row < self.GRID_HEIGHT:
            self.grid_logic[row][col] = 1 if self.grid_logic[row][col] == 0 else 0
            self.cell_manager.update_grid_visual(self.grid_logic)

    def draw(self):
        self.renderer.draw()
        self.clock.tick(self.FPS)

    def get_grid_logic(self):
        return self.grid_logic