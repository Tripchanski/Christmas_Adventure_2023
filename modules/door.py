from modules.object import Object
from modules.json import *
import pygame
sound = pygame.mixer.Sound('sounds/SOUNDS/Button_On.mp3')
sound.set_volume(round(read('json/settings.json')['volume']['sounds_volume'], 1))
class Door(Object):
	def __init__(self, image, x, y, width, height, color, pk=None):
		super().__init__(image, x, y, width, height, color, pk)
		self.start_x = x
		self.start_y = y
		self.closed = False
		self.counter = self.hitbox.height
		self.play_sound = True
	def open(self, level_arm):
		if self.closed == False:
			if level_arm.pk == self.pk and level_arm.is_on == True:
				level_arm.color = (0,255,0)
				if self.play_sound == True:
					
					self.play_sound = False
					sound.play()
				if self.counter > 0:
					self.hitbox.y -= 1
					self.counter -= 1
				else:
					self.counter = self.hitbox.height
					self.closed = True
					self.play_sound = True
					level_arm.is_on = False

		else:
			if level_arm.pk == self.pk and level_arm.is_on == True:
				level_arm.color = (255,0,0)
				if self.play_sound == True:
					self.play_sound = False
					sound.play()
				if self.counter > 0:
					self.hitbox.y += 1
					self.counter -= 1
				else:
					self.counter = self.hitbox.height
					self.closed = False
					self.play_sound = True
					level_arm.is_on = False