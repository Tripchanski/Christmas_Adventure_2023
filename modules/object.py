import pygame

class Object():
    def __init__(self, image, x, y, width, height, color, pk=None):
        self.hitbox = pygame.Rect(x, y, width, height)
        self.color = color
        self.image_source = image
        if image != None:
            if image == 'images/__game_picture__/snow2.png':
                self.image = pygame.image.load(image)
                self.image = pygame.transform.scale(self.image, (self.hitbox.width+20, self.hitbox.height+15))
            else:
                self.image = pygame.image.load(image)
                self.image = pygame.transform.scale(self.image, (self.hitbox.width, self.hitbox.height))
        self.pk = pk

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.hitbox)

    def animate(self, screen):
        if self.image_source == 'images/__game_picture__/snow2.png':
            screen.blit(self.image, (self.hitbox.x-10, self.hitbox.y-15))
        else:
            screen.blit(self.image, (self.hitbox.x, self.hitbox.y))

    def update(self, x_shift, y_shift):
        self.hitbox.x += x_shift
        self.hitbox.y += y_shift