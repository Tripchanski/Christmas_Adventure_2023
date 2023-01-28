import pygame
from modules.level_map import *
from modules.pigeon import *
from modules.level_map import screen_width, screen_height


class Sled():
    def __init__(self, start_x, start_y, width, height, color, image, animation, speed):
        #default -=-=-
        self.hitbox = pygame.Rect(start_x, start_y, width, height)
        self.start_x = start_x
        self.start_y = start_y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.animCounter = 0
        #image -=-=-
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (self.hitbox.width + int(screen_width*0.156), self.hitbox.height + int(screen_height*0.046)))

        self.animation_right = []
        for src in animation:
            img = pygame.image.load(src)
            img = pygame.transform.scale(img, (self.hitbox.width + int(screen_width*0.156), self.hitbox.height + int(screen_height*0.046)))
            self.animation_right.append(img)

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.hitbox)

    def animate(self, screen):
        if self.animCounter + 1 >= 30:
            self.animCounter = 0

        screen.blit(self.animation_right[self.animCounter//5], (self.hitbox.x - screen_width*0.052, self.hitbox.y - screen_height*0.031))
        self.animCounter += 1

    def move_sled(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.hitbox.y -= self.speed
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.hitbox.y += self.speed

        if self.hitbox.y <= 0:
            self.hitbox.y += self.speed
        elif self.hitbox.bottom + self.speed >= screen_height:
            self.hitbox.bottom = screen_height - self.speed

sled_animations = ['images/animations/sled.png', 'images/animations/sled_2.png', 'images/animations/sled_1.png', 'images/animations/sled_2.png', 'images/animations/sled_3.png', 'images/animations/sled_4.png']

nikolay_sled = Sled(screen_width*0.208, window_size[1] - ((window_size[1]+275)//2), screen_width*0.196, screen_height*0.236, (255,0,0), "images/__game_picture__/sled.png", sled_animations, screen_width*0.005)