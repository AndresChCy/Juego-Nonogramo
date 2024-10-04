import pygame
from Colores import Colores
from GridLinesRenderer import GridLinesRenderer
from CluesRenderer import CluesRenderer
from MiniatureRenderer import MiniatureRenderer

class GridRenderer:
    def __init__(self, screen, cell_manager, clue_generator, grid_logic, offset_x, offset_y, cell_size):
        self.screen = screen
        self.cell_manager = cell_manager
        self.clue_generator = clue_generator
        self.grid_logic = grid_logic
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.cell_size = cell_size
        self.grid_lines_renderer = GridLinesRenderer(screen, cell_manager, offset_x, offset_y, cell_size)
        self.clues_renderer = CluesRenderer(screen, clue_generator, offset_x, offset_y, cell_size)
        self.miniature_renderer = MiniatureRenderer(screen, grid_logic, offset_x, offset_y, cell_manager)

    def draw(self):
        self.cell_manager.all_cells.draw(self.screen)
        self.grid_lines_renderer.draw_grid_lines()
        self.clues_renderer.draw_horizontal_clues()
        self.clues_renderer.draw_vertical_clues()
        self.clues_renderer.draw_clue_borders()
        self.miniature_renderer.draw_miniature()