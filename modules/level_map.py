import pygame

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

wall_size = 108
window_size = pygame.display.get_window_size()

if window_size[0] == 1536 and window_size[1] == 864:
	level_map = [
		'                        X             ',
		'                       X              ',
		'                      X               ',
		'                     X                ',
		'                    X                 ',
		'                   X                  ',
		'     XXX          X                   ',
		'        X        X                    ',
		'         X      X                     ',
		'          XX   X                      ',
		'              X                       ',
		'             X                        ',
		'            X                         ',
		'           X                          ',
		'          X                           ',
		'         X                         XXX',
		'X X     XXX XXX                       ',
		'X      X       X                      ',
		'X  P  X          X                 XXX',
		'G                                     ',
		'                                      ',
		'                                      ',
	]
elif window_size[0] == 1920 and window_size[1] == 1080:
	level_map = [
		'                        X             ',
		'                       X              ',
		'                      X               ',
		'                     X                ',
		'                    X                 ',
		'                   X                  ',
		'     XXX          X                   ',
		'        X        X                    ',
		'         X      X                     ',
		'          XX   X                      ',
		'              X                       ',
		'             X                        ',
		'            X                         ',
		'           X                          ',
		'          X                           ',
		'         X                         XXX',
		'X X     XXX XXX                       ',
		'X      X       X                      ',
		'X  P  X          X                 XXX',
		'G                                     ',
	]