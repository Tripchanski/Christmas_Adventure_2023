from modules.object import Object
from modules.level_map import screen_height, screen_width
import pygame

class Exit(Object):
	def __init__(self, image, x, y, width, height, color, pk=None):
		super().__init__(image, x, y, width, height, color, pk)
		self.end_game = False