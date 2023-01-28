
import pygame

class Wall():
    def __init__(self, x, y, width, height, color, pk=None):
        self.hitbox = pygame.Rect(x, y, width, height)
        self.color = color
        self.pk = pk

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.hitbox)

    def update(self, x_shift, y_shift):
        self.hitbox.x += x_shift
        self.hitbox.y += y_shift