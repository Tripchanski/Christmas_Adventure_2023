import pygame
import random
from modules.level_map import *
from modules.sled import *


class Pigeon():
    def __init__(self, start_x, start_y, width, height, color, image, animation, speed):
        self.hitbox = pygame.Rect(start_x, start_y, width, height)
        self.start_x = start_x
        self.start_y = start_y
        self.speed = speed
        self.color = color
        self.animCounter = 0

        self.animation_left = []
        for src in animation:
            img = pygame.image.load(src)
            img = pygame.transform.scale(img, (self.hitbox.width, self.hitbox.height))
            self.animation_left.append(img)

        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (self.hitbox.width, self.hitbox.height))

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.hitbox)

    def animate(self, screen):
        screen.blit(self.animation_left[self.animCounter // 5], (self.hitbox.x, self.hitbox.y))

    def fly(self):
        self.hitbox.x -= self.speed

        if self.animCounter + 1 >= 30:
            self.animCounter = 0

        self.animCounter += 1

        if self.hitbox.x <= -100:
            self.hitbox.x = window_size[0] + 10
            self.hitbox.y = random.randint(50, screen_height - int(screen_height*0.074) - 10)
            self.speed = random.randint(int(screen_width*0.005), int(screen_width*0.008))

pigeon_animation = ['images/animations/bird_1.png', 'images/animations/bird_2.png', 'images/animations/bird_3.png', 'images/animations/bird_4.png', 'images/animations/bird_3.png', 'images/animations/bird_2.png']

