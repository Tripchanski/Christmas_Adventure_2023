import pygame
from level_map import screen


class Button:
    def __init__(self, width, height, x, y, image, image_hover):

        self.width = width
        self.height = height
        self.color = (0,0,0)
        self.x = x
        self.y = y
        self.image = image
        self.image_hover = image_hover

    def draw(self, action=None):
        
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()


        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
            if click[0] == 1:
                if action is not None:
                    if action == quit:
                        pygame.quit()
                    else:
                        action()
        else:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))


# ============================================================
    def animate(self, screen):

        mouse = pygame.mouse.get_pos()
        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
           screen.blit(self.image_hover, (self.x, self.y))
        else:
            screen.blit(self.image, (self.x, self.y))
# ============================================================