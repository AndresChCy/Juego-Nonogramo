import pygame
import os

class FrameLoader:
    def __init__(self, folder):
        self.frames = self.load_frames(folder)

    def load_frames(self, folder):
        frames = []
        for filename in sorted(os.listdir(folder)):
            if filename.endswith('.png') or filename.endswith('.gif'):
                frame = pygame.image.load(os.path.join(folder, filename))
                frames.append(frame)
        if not frames:
            print(f"No frames loaded from {folder}. Please check the folder path and contents.")
        return frames

    def get_frames(self):
        return self.frames