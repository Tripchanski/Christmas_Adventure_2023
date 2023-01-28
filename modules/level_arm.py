import pygame
from modules.level_map import window_size

class Level_arm():
    def __init__(self, image_on, image_off, x, y, width, height, pk):
        self.hitbox = pygame.Rect(x, y, width, height)
        self.is_on = False
        self.color = (255,0,0)
        self.image_on = pygame.image.load(image_on)
        self.image_on = pygame.transform.scale(self.image_on, (self.hitbox.width, self.hitbox.height))
        self.image_off = pygame.image.load(image_off)
        self.image_off = pygame.transform.scale(self.image_off, (self.hitbox.width, self.hitbox.height))
        self.pk = pk
        self.hint = pygame.Rect(window_size[0] // 2 - 32, 250, 85, 85)
        self.hint_image = pygame.image.load('images/__game_picture__/press_e.png')
        self.hint_image = pygame.transform.scale(self.hint_image, (self.hint.width, self.hint.height))

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.hitbox)

    def animate(self, screen):
        if self.color == (0,255,0):
            screen.blit(self.image_on, (self.hitbox.x, self.hitbox.y))
        elif self.color == (255,0,0):
            screen.blit(self.image_off, (self.hitbox.x, self.hitbox.y))

    def interaction(self, player):
        keys = pygame.key.get_pressed()
        if player.hitbox.colliderect(self.hitbox):
            if keys[pygame.K_e]:
                self.is_on = True

    def update(self, x_shift, y_shift):
        self.hitbox.x += x_shift
        self.hitbox.y += y_shift
