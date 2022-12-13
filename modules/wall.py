
import pygame

class Wall():
    def __init__(self, start_x, start_y, width, height, color):
        self.hitbox = pygame.Rect(start_x, start_y, width, height)
        self.color = color

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.hitbox)

    def update(self, x_shift):
        self.hitbox.x += x_shift