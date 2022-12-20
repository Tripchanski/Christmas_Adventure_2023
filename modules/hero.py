import pygame

class Hero():
    def __init__(self, start_x, start_y, width, height, color, image, animation, speed):
        #default -=-=-
        self.hitbox = pygame.Rect(start_x, start_y, width, height)
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color

        #image -=-=-
        self.image = pygame.image.load('images/' + image)
        self.image_right = pygame.transform.scale(self.image, (150, 200))
        self.image_left = pygame.transform.flip(self.image_right, True, False)
        self.current_image = self.image_right
        self.facing = 'r'
        
        #jump -=-=-
        self.gravity = 0.8
        self.jump_speed = -16
        self.direction = pygame.math.Vector2(0,0)
        self.on_ground = False

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.hitbox)

    def animate(self, screen):
        if self.facing == 'r':
            screen.blit(self.current_image, (self.hitbox.x - 70, self.hitbox.y))
        else:
            screen.blit(self.current_image, (self.hitbox.x - 25, self.hitbox.y))

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.direction.x = 1
            self.facing = 'r'
            self.current_image = self.image_right
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.facing = 'l'
            self.current_image = self.image_left
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] and self.on_ground:
            self.jump()

    def turnon_gravity(self):
        self.direction.y += self.gravity
        self.hitbox.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.move()