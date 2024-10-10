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
        self.hovered_row = None
        self.hovered_col = None

    def handle_mouse_motion(self, pos):
        mouse_x, mouse_y = pos
        col = (mouse_x - self.offset_x) // self.cell_size
        row = (mouse_y - self.offset_y) // self.cell_size
        if 0 <= col < len(self.grid_logic[0]) and 0 <= row < len(self.grid_logic):
            self.hovered_row = row
            self.hovered_col = col
        else:
            self.hovered_row = None
            self.hovered_col = None

    def handle_mouse_click(self, pos, button):
        mouse_x, mouse_y = pos
        col = (mouse_x - self.offset_x) // self.cell_size
        row = (mouse_y - self.offset_y) // self.cell_size
        if 0 <= col < len(self.grid_logic[0]) and 0 <= row < len(self.grid_logic):
            if button == 1:  # Left click
                self.grid_logic[row][col] = 1
            elif button == 3:  # Right click
                self.grid_logic[row][col] = -1
            self.cell_manager.update_grid_visual(self.grid_logic)

    def handle_mouse_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.handle_mouse_click(event.pos, event.button)

    def draw(self):
        self.cell_manager.draw_cells(self.screen)
        self.draw_hover_effect()
        self.grid_lines_renderer.draw_grid_lines()
        self.clues_renderer.draw_horizontal_clues()
        self.clues_renderer.draw_vertical_clues()
        self.clues_renderer.draw_clue_borders()
        self.miniature_renderer.draw_miniature()

    def draw_hover_effect(self):
        if self.hovered_row is not None and self.hovered_col is not None:
            for col in range(len(self.grid_logic[0])):
                if self.grid_logic[self.hovered_row][col] == 0:
                    pygame.draw.rect(self.screen, Colores.WHITE_SMOKE.value,
                                     (self.offset_x + col * self.cell_size, self.offset_y + self.hovered_row * self.cell_size,
                                      self.cell_size, self.cell_size))
            for row in range(len(self.grid_logic)):
                if self.grid_logic[row][self.hovered_col] == 0:
                    pygame.draw.rect(self.screen, Colores.WHITE_SMOKE.value,
                                     (self.offset_x + self.hovered_col * self.cell_size, self.offset_y + row * self.cell_size,
                                      self.cell_size, self.cell_size))
            self.clues_renderer.draw_horizontal_clues()
            self.clues_renderer.draw_vertical_clues()