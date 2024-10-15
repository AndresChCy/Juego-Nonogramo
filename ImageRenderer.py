import pygame

class ImageRenderer:
    def __init__(self, screen, frames, flip_x=False, flip_y=False):
        self.screen = screen
        self.frames = [pygame.transform.flip(frame, flip_x, flip_y) for frame in frames]
        self.current_frame = 0
        self.frame_delay = 4
        self.frame_counter = 0

    def draw(self, position):
        image = self.frames[self.current_frame]
        image_rect = image.get_rect(center=position)
        self.screen.blit(image, image_rect)
        self.frame_counter += 1
        if self.frame_counter >= self.frame_delay:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.frame_counter = 0