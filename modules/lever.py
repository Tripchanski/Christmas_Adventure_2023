import pygame
from modules.level_map import window_size

class Lever():
    def __init__(self, x, y, width, height, pk):
        self.hitbox = pygame.Rect(x, y, width, height)
        self.is_on = False
        self.color = (255,0,0)
        self.pk = pk
        self.hint = pygame.Rect(window_size[0] // 2 - 32, 250, 64, 64)
        self.hint_image = pygame.image.load('images/letter-e.ico')

    def draw(self, window):
            pygame.draw.rect(window, self.color, self.hitbox)

    def interaction(self, player, screen):
        keys = pygame.key.get_pressed()
        if player.hitbox.colliderect(self.hitbox):
            if self.is_on == False:
                pygame.draw.rect(screen, (192,192,192), self.hint)
                screen.blit(self.hint_image, (self.hint.x, self.hint.y))
            if keys[pygame.K_e]:
                self.is_on = True

    def update(self, x_shift, y_shift):
        self.hitbox.x += x_shift
        self.hitbox.y += y_shift
