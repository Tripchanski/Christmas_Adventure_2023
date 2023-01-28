import pygame
from modules.object import Object
from modules.level_map import screen_width, screen_height

class Npc(Object):
	def __init__(self, speed, direction, image, animation, x, y, width, height, color, pk=None):
		super().__init__(image, x, y, width, height, color, pk)
		self.image = pygame.image.load(image)
		self.image_right = pygame.transform.scale(self.image, (150, 200))
		self.image_left = pygame.transform.flip(self.image_right, True, False)
		self.ray = pygame.Rect(self.hitbox.centerx, self.hitbox.y + 20, screen_width*0.234, 10)
		self.warning = pygame.image.load('images/__game_picture__/warning.png')
		self.warning = pygame.transform.scale(self.warning, (17, 47))
		self.direction = direction
		self.speed = speed
		self.current_image = self.image_right
		self.stop_game = False
		self.stop_counter = 0
		self.animCounter = 0

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

	def draw(self, screen):
		pygame.draw.rect(screen, self.color, self.hitbox)
		pygame.draw.rect(screen, (0, 255, 0), self.ray)
		
	def animate(self, screen):
		self.ray.y = self.hitbox.y + 70

		if self.animCounter + 1 >= 30:
			self.animCounter = 0
		
		if self.direction == 'l':
			self.ray.x = self.hitbox.centerx - self.ray.width
			screen.blit(self.animation_right[self.animCounter // 5], (self.hitbox.x - 50, self.hitbox.y))
			self.animCounter += 1
			self.speed = -5
		elif self.direction == 'r':
			self.ray.x = self.hitbox.centerx
			screen.blit(self.animation_left[self.animCounter // 5], (self.hitbox.x - 30, self.hitbox.y))
			self.animCounter += 1
			self.speed = 5
	
	def walk(self, player, screen):
		if not self.stop_game:
			self.hitbox.x += self.speed
			self.ray.x += self.speed

		if self.ray.colliderect(player.hitbox) and player.hide != True:
			self.stop_game = True
			screen.blit(self.warning, (self.hitbox.centerx-5.5, self.hitbox.y - 55))