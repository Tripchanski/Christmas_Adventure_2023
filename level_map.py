import pygame
from wall import Wall

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

level_map = [
	'                  ',
	'                  ',
	'                  ',
	'                  ',
	'  X     XXX XXX   ',
	'       X       X  ',
	'   P  X          X',
	'GGGGGGGGGGGGGGGGGG',
	'                  ',
	'                  ',
]

wall_size = 108
window_size = pygame.display.get_window_size()