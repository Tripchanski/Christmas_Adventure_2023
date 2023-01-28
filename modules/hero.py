import pygame

class Hero():
    def __init__(self, start_x, start_y, width, height, color, image, animation, speed, pk=None):
        #default -=-=-
        self.hitbox = pygame.Rect(start_x, start_y, width, height)
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.pk = pk
        self.animCounter = 0

        #image -=-=-
        self.image = pygame.image.load(image)
        self.image_right = pygame.transform.scale(self.image, (150, 200))
        self.image_left = pygame.transform.flip(self.image_right, True, False)
        self.current_image = self.image_right
        self.facing = 'r'

        #animation -=-=-
        self.animation_right = []
        for src in animation:
            img = pygame.image.load(src)
            img = pygame.transform.scale(img, (150, 200))
            self.animation_right.append(img)

        self.animation_left = []
        for src in animation:
            img = pygame.image.load(src)
            img = pygame.transform.scale(img, (150, 200))
            img = pygame.transform.flip(img, True, False)
            self.animation_left.append(img)
        
        #jump -=-=-
        self.gravity = 1
        self.jump_speed = -16
        self.direction = pygame.math.Vector2(0,0)
        self.on_ground = False
        self.jumped = False

        #status -=-=-
        self.gift_count = 0
        self.hide = False

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.hitbox)

    def animate(self, screen):

        if self.animCounter + 1 >= 30:
            self.animCounter = 0

        if self.facing == 'r':
            if self.pk == 2:
                screen.blit(self.animation_right[self.animCounter // 5], (self.hitbox.x - 70, self.hitbox.y - 50))
                self.animCounter += 1
            elif self.pk == 3:
                screen.blit(self.animation_right[self.animCounter // 5], (self.hitbox.x - 60, self.hitbox.y - 40))
                self.animCounter += 1
            elif self.pk == 1:
                screen.blit(self.animation_right[self.animCounter // 5], (self.hitbox.x - 50, self.hitbox.y - 40))
                self.animCounter += 1
        elif self.facing == 'l':
            if self.pk == 2:
                screen.blit(self.animation_left[self.animCounter // 5], (self.hitbox.x - 25, self.hitbox.y - 50))
                self.animCounter += 1
            elif self.pk == 3:
                screen.blit(self.animation_left[self.animCounter // 5], (self.hitbox.x - 30, self.hitbox.y - 40))
                self.animCounter += 1
            elif self.pk == 1:
                screen.blit(self.animation_left[self.animCounter // 5], (self.hitbox.x - 30, self.hitbox.y - 40))
                self.animCounter += 1

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing = 'r'
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing = 'l'
        else:
            self.direction.x = 0
            self.animCounter = 0

        if (keys[pygame.K_SPACE] and self.on_ground) or (keys[pygame.K_w] and self.on_ground) or (keys[pygame.K_UP] and self.on_ground):
            self.jump()
            self.jumped = True

    def turnon_gravity(self, stop_move):
        self.direction.y += self.gravity
        if stop_move == False:
            self.hitbox.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.move()