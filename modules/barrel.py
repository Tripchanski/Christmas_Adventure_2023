import pygame
from modules.object import Object
from modules.level_map import window_size

class Barrel(Object):
	def __init__(self, image, x, y, width, height, color, pk=None):
		super().__init__(image, x, y, width, height, color, pk)
		self.is_in = False
		self.hint = pygame.Rect(window_size[0] // 2 - 32, 250, 85, 85)
		self.hint_image = pygame.image.load('images/__game_picture__/hold_e.png')
		self.counter = 0

	def interaction(self, player, screen, barrel_list):
		keys = pygame.key.get_pressed()

		if player.hitbox.colliderect(self.hitbox):
			if self.is_in == False:
				screen.blit(self.hint_image, (self.hint.x, self.hint.y))
			if keys[pygame.K_e]:
				for barrel in barrel_list:
					barrel.is_in = True
					player.hide = True
			elif keys[pygame.K_e] == False:
				for barrel in barrel_list:
					barrel.is_in = False
					player.hide = False