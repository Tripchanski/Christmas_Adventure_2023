from level_map import *
import pygame
import sys
# ================================
from buttons import Button
from wall import Wall
from hero import Hero
from level import Level
# ================================

clock = pygame.time.Clock()

# =============================================================================================================================================


menu_music = pygame.mixer.Sound('sounds/music_1.mp3')               #      MUSIC and SOUNDS      #


# ==============================================================================================================================================


text_font = pygame.font.SysFont('comicsansms', 45)

text = text_font.render("Christmas Adventure 2023",True, (0,255,0))
text2 = text_font.render('Salam Brat!!!', True, (102,0,0))
text3 = text_font.render('Тут будут настпройки но пока их нет :(', True, (102,0,0))


# ======================================================================================================================================================   

start_img = pygame.image.load('images/button_play.png')
start_img = pygame.transform.scale(start_img, (270, 270))

opt_img = pygame.image.load('images/button_settings.png')
opt_img = pygame.transform.scale(opt_img, (250, 250))

exit_img = pygame.image.load('images/button_exit.png')
exit_img = pygame.transform.scale(exit_img, (200, 200))

# ===================================================================                BUTTONS_IMG

start_img_hover = pygame.image.load('images/button_play_hover.png')
start_img_hover = pygame.transform.scale(start_img_hover, (270, 270))

opt_img_hover = pygame.image.load('images/button_settings_hover.png')
opt_img_hover = pygame.transform.scale(opt_img_hover, (250, 250))

exit_img_hover = pygame.image.load('images/button_exit-hover.png')
exit_img_hover = pygame.transform.scale(exit_img_hover, (200, 200))

# ======================================================================================================================================================      


start_button = Button(270, 270, 20, 280, start_img, start_img_hover)
opt_button = Button(250, 250, 235, 530, opt_img, opt_img_hover)
exit_button_menu = Button(200, 200, 30, 590, exit_img, exit_img_hover)


quit_button2 = Button(160, 160, window_size[0] - 165, 0, exit_img, exit_img_hover)


# ===============================================================================================================================================

def main_menu():

    bg_img = pygame.image.load('images/background.jpg')
    bg_img = pygame.transform.scale(bg_img, (1920, 1080))
    main = True
    while main:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

    # =================================================

        start_button.draw(start_game)
        opt_button.draw(opttions)
        exit_button_menu.draw(quit)

        screen.blit(bg_img, (0, 0))

        start_button.animate(screen)
        opt_button.animate(screen)
        exit_button_menu.animate(screen)

    # =================================================
        screen.blit(text, (window_size[0]//2-250, window_size[1]//2-400))


        pygame.display.update()

# ===============================================================================================================================================

level = Level(level_map, screen)

def start_game():

    game = True

    while game:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        quit_button2.draw(quit)
        screen.fill((0,0,150))
        quit_button2.animate(screen)

        level.run()

        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)


def opttions():

    opt = True
    while opt:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        exit_button_menu.draw(quit)

        screen.fill((119, 210, 153))

        exit_button_menu.animate(screen)

        screen.blit(exit_img, (window_size[0]//2-exit_button_menu.width//2, window_size[1]//2-exit_button_menu.height//2+200))
        screen.blit(text3, (window_size[0]//2-400, window_size[1]//2-200))

        pygame.display.update()
        pygame.display.flip()



main_menu()