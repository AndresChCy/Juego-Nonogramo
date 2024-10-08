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
        self.draw_cells()

    def draw_cells(self):
        for row in range(len(self.grid_logic)):
            for col in range(len(self.grid_logic[row])):
                if self.grid_logic[row][col] == 1:  # Check for black cell
                    color = Colores.BLACK.value
                    pygame.draw.rect(self.screen, color,
                                     (self.offset_x + col * self.cell_size,
                                      self.offset_y + row * self.cell_size,
                                      self.cell_size, self.cell_size))
                elif self.grid_logic[row][col] == -1:  # Check for red X
                    start_pos1 = (self.offset_x + col * self.cell_size, self.offset_y + row * self.cell_size)
                    end_pos1 = (self.offset_x + (col + 1) * self.cell_size, self.offset_y + (row + 1) * self.cell_size)
                    start_pos2 = (self.offset_x + (col + 1) * self.cell_size, self.offset_y + row * self.cell_size)
                    end_pos2 = (self.offset_x + col * self.cell_size, self.offset_y + (row + 1) * self.cell_size)
                    pygame.draw.line(self.screen, Colores.RED.value, start_pos1, end_pos1, 3)
                    pygame.draw.line(self.screen, Colores.RED.value, start_pos2, end_pos2, 3)