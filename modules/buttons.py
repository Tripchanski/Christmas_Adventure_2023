import pygame
from modules.level_map import screen

class Button:
    def __init__(self, width, height, x, y, image, image_hover):
        self.hitbox = pygame.Rect(x, y, width, height)
        self.pressed = False
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (self.hitbox.width, self.hitbox.height))
        self.image_hover = pygame.image.load(image_hover)
        self.image_hover = pygame.transform.scale(self.image_hover, (self.hitbox.width, self.hitbox.height))

    def action(self, action=None, music=None):
        mouse = pygame.mouse.get_pos()

        if self.hitbox.x < mouse[0] < self.hitbox.x + self.hitbox.width and self.hitbox.y < mouse[1] < self.hitbox.y + self.hitbox.height:
            if action is not None:
                if action == 'press':
                    self.pressed = True
                    if music is not None:
                        music.stop()
                else:
                    if music is not None:
                        for sound in music:
                            sound.stop()
                    action()

# ============================================================
    def animate(self, screen):

        mouse = pygame.mouse.get_pos()
        if self.hitbox.x < mouse[0] < self.hitbox.x + self.hitbox.width and self.hitbox.y < mouse[1] < self.hitbox.y + self.hitbox.height:
           screen.blit(self.image_hover, (self.hitbox.x, self.hitbox.y))
        else:
            screen.blit(self.image, (self.hitbox.x, self.hitbox.y))
# ============================================================

    def music_plus(self):
        mouse = pygame.mouse.get_pos()
        
        if self.hitbox.x < mouse[0] < self.hitbox.x + self.hitbox.width and self.hitbox.y < mouse[1] < self.hitbox.y + self.hitbox.height:
            #screen.blit(self.image_hover, (self.x, self.y))
            self.pressed = True
        #else:
        #    screen.blit(self.image, (self.x, self.y))

    def music_minus(self):
        mouse = pygame.mouse.get_pos()

        if self.hitbox.x < mouse[0] < self.hitbox.x + self.hitbox.width and self.hitbox.y < mouse[1] < self.hitbox.y + self.hitbox.height:
            self.pressed = True