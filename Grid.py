import pygame
from Cell import Cell
from Colores import Colores

class Grid:
    CELL_SIZE = 40

    def __init__(self, screen, grid_width=10, grid_height=10):
        self.screen = screen
        self.GRID_WIDTH = grid_width
        self.GRID_HEIGHT = grid_height
        self.window_width, self.window_height = screen.get_size()
        self.grid_width_px = self.GRID_WIDTH * self.CELL_SIZE
        self.grid_height_px = self.GRID_HEIGHT * self.CELL_SIZE
        self.offset_x = (self.window_width - self.grid_width_px) // 2
        self.offset_y = (self.window_height - self.grid_height_px) // 2
        self.grid_logic = [[0 for _ in range(self.GRID_WIDTH)] for _ in range(self.GRID_HEIGHT)]
        self.all_cells = pygame.sprite.Group()
        self._initialize_cells()
        self.clock = pygame.time.Clock()
        self.FPS = 60

    def _initialize_cells(self):
        for row in range(self.GRID_HEIGHT):
            for col in range(self.GRID_WIDTH):
                cell = Cell(self.offset_x + col * self.CELL_SIZE, self.offset_y + row * self.CELL_SIZE, self.CELL_SIZE)
                self.all_cells.add(cell)

    def update_grid_visual(self):
        for row in range(self.GRID_HEIGHT):
            for col in range(self.GRID_WIDTH):
                cell_idx = row * self.GRID_WIDTH + col
                cell_sprite = list(self.all_cells)[cell_idx]
                if self.grid_logic[row][col] == 1:
                    cell_sprite.fill()
                else:
                    cell_sprite.empty()

    def draw_grid_lines(self):
        for row in range(self.GRID_HEIGHT + 1):
            pygame.draw.line(self.screen, Colores.BLACK.value, (self.offset_x, self.offset_y + row * self.CELL_SIZE), (self.offset_x + self.grid_width_px, self.offset_y + row * self.CELL_SIZE))
        for col in range(self.GRID_WIDTH + 1):
            pygame.draw.line(self.screen, Colores.BLACK.value, (self.offset_x + col * self.CELL_SIZE, self.offset_y), (self.offset_x + col * self.CELL_SIZE, self.offset_y + self.grid_height_px))

    def handle_click(self, pos):
        mouse_x, mouse_y = pos
        col = (mouse_x - self.offset_x) // self.CELL_SIZE
        row = (mouse_y - self.offset_y) // self.CELL_SIZE
        if 0 <= col < self.GRID_WIDTH and 0 <= row < self.GRID_HEIGHT:
            self.grid_logic[row][col] = 1 if self.grid_logic[row][col] == 0 else 0
            self.update_grid_visual()

    def draw(self):
        self.all_cells.draw(self.screen)
        self.draw_grid_lines()
        self.clock.tick(self.FPS)

    def get_grid_logic(self):
        return self.grid_logic