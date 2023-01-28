import pygame
from modules.level_map import screen_width, screen_height

class Transition():
	def __init__(self, previous_image, image):
		self.img = pygame.image.load(image)
		self.img = pygame.transform.scale(self.img, (screen_width, screen_height))
		if previous_image != None:
			self.previous_image = pygame.image.load(previous_image)
			self.previous_image = pygame.transform.scale(self.previous_image, (screen_width, screen_height))
		self.opacity_e = 0
		self.opacity_s = 255
		self.stop_e = False
		self.stop_s = False
		self.stop_counter = 0

	def transition_end(self, screen):
		if self.stop_e == False:
			self.opacity_e += 15
			if self.opacity_e == 255:
				self.stop_e = True
		if self.stop_counter != 900:
			self.stop_counter += 15

		self.img.set_alpha(self.opacity_e)
		screen.blit(self.img, (0,0))

	def transition_start(self, screen):
		if self.stop_s == False:
			self.opacity_s -= 15
			if self.opacity_s == 0:
				self.stop_s = True

		if self.previous_image != None:
			self.previous_image.set_alpha(self.opacity_s)
			screen.blit(self.previous_image, (0,0))
		else:
			self.img.set_alpha(self.opacity_s)
			screen.blit(self.img, (0,0))