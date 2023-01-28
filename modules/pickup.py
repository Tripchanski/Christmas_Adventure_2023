import pygame
from modules.object import Object

class Pickup(Object):
    def __init__(self, image, x, y, width, height, color, pk=None):
        super().__init__(image, x, y, width, height, color, pk)
        self.color = color
        self.pk = pk

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.hitbox)
    
    def collide(self, player, drop_list, drop):
        if player.hitbox.colliderect(self.hitbox):
            drop_list.remove(drop)
            if self.pk == 1:
                player.gift_count += 1
        

    def update(self, x_shift, y_shift):
        self.hitbox.x += x_shift
        self.hitbox.y += y_shift