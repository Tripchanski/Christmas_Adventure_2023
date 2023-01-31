from modules.level_map import *
import pygame
import os
# ================================
from modules.buttons import Button
from modules.level import Level
from modules.object import Object
from modules.make_text import *
from modules.sled import *
from modules.pigeon import *
from modules.transition import Transition
from modules.json import *

# ================================

clock = pygame.time.Clock()

# =============================================================================================================================================
music_list = [pygame.mixer.Sound('sounds/shedrik.wav'), pygame.mixer.Sound("sounds/i'm_sorry.wav"), pygame.mixer.Sound('sounds/default.wav'), pygame.mixer.Sound('sounds/picturesque.wav'), pygame.mixer.Sound('sounds/day_snow.wav'), pygame.mixer.Sound('sounds/window.wav'), pygame.mixer.Sound('sounds/home.wav'), pygame.mixer.Sound('sounds/i_miss_you.wav')]                #      MUSIC and SOUNDS      #
sounds_list = [pygame.mixer.Sound('sounds/steps.wav'), pygame.mixer.Sound('sounds/wind.wav'), pygame.mixer.Sound('sounds/snow.wav')]

for music in music_list:
    music.set_volume(round(read('json/settings.json')['volume']['music_volume'], 1))
for sound in sounds_list:
    sound.set_volume(round(read('json/settings.json')['volume']['sounds_volume'], 1))


#=-=-=-=-=-=-=-=-=-
opacity = 200

santa = pygame.image.load('images/__game_picture__/heroes/santa.png')
santa = pygame.transform.scale(santa, (int(screen_width*0.289), int(screen_height*0.927)))

main_elf = pygame.image.load('images/__game_picture__/heroes/main_elf.png')
main_elf = pygame.transform.scale(main_elf, (int(screen_width*0.172 + 331*0.3),int(screen_height*0.469 + 507*0.3)))

elf1 = pygame.image.load('images/__game_picture__/heroes/hero_1.png')
elf1 = pygame.transform.scale(elf1, (int(screen_width*0.172 + 331*0.3),int(screen_height*0.469 + 507*0.3)))
elf1 = pygame.transform.flip(elf1, True, False)

elf2 = pygame.image.load('images/__game_picture__/heroes/hero_2.png')
elf2 = pygame.transform.scale(elf2, (int(screen_width*0.172 + 331*0.3),int(screen_height*0.429 + 507*0.3)))
elf2 = pygame.transform.flip(elf2, True, False)

elf3 = pygame.image.load('images/__game_picture__/heroes/hero_3.png')
elf3 = pygame.transform.scale(elf3, (int(screen_width*0.172 + 331*0.3),int(screen_height*0.469 + 507*0.3)))
elf3 = pygame.transform.flip(elf3, True, False)

main_elf_black = pygame.image.load('images/shadow/main_elf_black.png')
main_elf_black = pygame.transform.scale(main_elf_black, (int(screen_width*0.172 + 331*0.3),int(screen_height*0.469 + 507*0.3)))
main_elf_black.set_alpha(opacity)

elf2_black = pygame.image.load('images/shadow/hero_2_black.png')
elf2_black = pygame.transform.scale(elf2_black, (int(screen_width*0.172 + 331*0.3),int(screen_height*0.429 + 507*0.3)))
elf2_black = pygame.transform.flip(elf2_black, True, False)
elf2_black.set_alpha(opacity)

elf1_black = pygame.image.load('images/shadow/hero_1_black.png')
elf1_black = pygame.transform.scale(elf1_black, (int(screen_width*0.172 + 331*0.3),int(screen_height*0.469 + 507*0.3)))
elf1_black = pygame.transform.flip(elf1_black, True, False)
elf1_black.set_alpha(opacity)

elf3_black = pygame.image.load('images/shadow/hero_3_black.png')
elf3_black = pygame.transform.scale(elf3_black, (int(screen_width*0.172 + 331*0.3),int(screen_height*0.469 + 507*0.3)))
elf3_black = pygame.transform.flip(elf3_black, True, False)
elf3_black.set_alpha(opacity)

santa_black = pygame.image.load('images/shadow/santa_black.png')
santa_black = pygame.transform.scale(santa_black, (int(screen_width*0.289), int(screen_height*0.927)))
santa_black.set_alpha(opacity)
#=-=-=-=-=-=-=-=-=-


# ==============================================================================================================================================

text_font = pygame.font.SysFont('comicsansms', 45)

#BUTTONS -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
start_button = Button(screen_width*0.17, screen_height*0.3, screen_width*0.028, screen_height*0.43, 'images/button_play.png', 'images/button_play_hover.png')
opt_button = Button(screen_width*0.156, screen_height*0.277, screen_width*0.25, screen_height*0.599, 'images/button_settings.png', 'images/button_settings_hover.png')
exit_button_menu = Button(screen_width*0.156, screen_height*0.277, screen_width*0.48, screen_height*0.648, 'images/button_exit.png', 'images/button_exit-hover.png')
return_button = Button(screen_width*0.078, screen_height*0.138, 10, 10, 'images/button_return.png', 'images/button_return_hover.png')
#BUTTONS -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# =================================================================DIALOG=====================================================================================   

diologfont_img = pygame.image.load('images/background.jpg')
diologfont_img = pygame.transform.scale(diologfont_img, (screen_width, screen_height))

dialogfont2_img = pygame.image.load('images/background_dialog.jpg')
dialogfont2_img = pygame.transform.scale(dialogfont2_img, (screen_width, screen_height))

text_field = Object('images/__game_picture__/tab_for_dialog.png', 0, screen_height-screen_height*0.314, screen_width, screen_height*0.324, (200,200,200))
text_field2 = Object('images/__game_picture__/tab_for_dialog.png', 0, screen_height-screen_height*0.314, screen_width, screen_height*0.324, (200,200,200))

# ====================================================================================================================================================== 

#ESCAPE-=-=-=-=-MENU
tab = Object('images/tab.png', screen_width*0.369, screen_height*0.153, screen_width*0.261, screen_height*0.648, None)
restart_button = Button(screen_width*0.104,screen_height*0.185,tab.hitbox.bottomright[0]-screen_width*0.104/2,tab.hitbox.bottomright[1]-screen_height*0.185/2, 'images/button_restart.png', 'images/button_restart_hover.png')
exit_button_game = Button(screen_width*0.104, screen_height*0.185, tab.hitbox.bottomleft[0]-screen_width*0.104/2,tab.hitbox.bottomleft[1]-screen_height*0.185/2, 'images/button_exit.png', 'images/button_exit-hover.png')
bg = Object('images/black_background.png', 0, 0, screen_width, screen_height, None)
#ESCAPE-=-=-=-=-MENU

# ===============================================================================================================================================

#SETTINGS -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
control = Object('images/__game_picture__/help.png', screen_width*0.312, screen_height*0.155, screen_width*0.672, screen_height*0.689, (0,0,0))
#SETTINGS -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def main_menu():
    bg_img = pygame.image.load('images/background.png')
    bg_img2 = pygame.image.load('images/background2.png')
    bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height))
    bg_img2 = pygame.transform.scale(bg_img2, (screen_width, screen_height))

    show_on = 0
    show = False
    transition = Transition(None, 'images/__game_picture__/transitions/1.jpg')

    volume = round(read('json/settings.json')['volume']['music_volume'], 1)
    music_list[0].play(loops=-1)

    main = True
    while main:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONUP:
                start_button.action('press')
                if start_button.pressed == True:
                    show = True
                if not show:
                    opt_button.action(options)
                    exit_button_menu.action(pygame.quit)

    # =================================================
        if show_on < 30:
            screen.blit(bg_img, (0, 0))
        elif show_on > 30:
            screen.blit(bg_img2, (0, 0))
        if show_on == 60:
            show_on = 0

        if not show:
            show_on += 1

        music_list[0].set_volume(round(volume, 2))

        start_button.animate(screen)
        opt_button.animate(screen)
        exit_button_menu.animate(screen)

        if show:
            transition.transition_end(screen)
            if round(volume, 2) > 0.00:
                volume -= 0.01
            if transition.stop_counter == 900:
                start_button.pressed = False
                music_list[0].stop()
                dialog()

    # =================================================


        pygame.display.update()
        clock.tick(60)

# ===============================================================================================================================================

def dialog():

    counter = 1
    dialog_start = True
    
    transition = Transition('images/__game_picture__/transitions/1.jpg','images/__game_picture__/transitions/2.jpg')
    music_list[1].play(loops=-1)

    while dialog_start:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONUP:
                if counter < 6:
                    counter += 1

        screen.blit(diologfont_img, (0, 0))
        
        if counter == 6:
            if transition.stop_counter != 900:
                transition.transition_end(screen)
            else:
                dialog2()
        else:
            text_field.animate(screen)

        if counter < 6:
            screen.blit(main_elf, (0,screen_height-int(screen_height*0.469 + 507*0.3)))

            #KATYA =========================
            if counter == 1 or counter == 2:
                screen.blit(elf2, (screen_width-int(screen_width*0.172 + 331*0.3),screen_height-int(screen_height*0.429 + 507*0.3)))
                screen.blit(elf2_black, (screen_width-int(screen_width*0.172 + 331*0.3),screen_height-int(screen_height*0.429 + 507*0.3)))
            #KATYA =========================

            #OLEG ==========================
            elif counter == 3 or counter == 4:
                screen.blit(elf1, (screen_width-int(screen_width*0.172 + 331*0.3),screen_height-int(screen_height*0.469 + 507*0.3)))
                screen.blit(elf1_black, (screen_width-int(screen_width*0.172 + 331*0.3),screen_height-int(screen_height*0.469 + 507*0.3)))
            #OLEG ==========================

            #NIKOLAY =======================
            elif counter == 5 or counter == 6:
                screen.blit(elf3, (screen_width-int(screen_width*0.172 + 331*0.3),screen_height-int(screen_height*0.469 + 507*0.3)))
                screen.blit(elf3_black, (screen_width-int(screen_width*0.172 + 331*0.3),screen_height-int(screen_height*0.469 + 507*0.3)))
            #NIKOLAY =======================
            
            text.draw_text(counter, screen_width*0.338, text_field2.hitbox.y + screen_height*0.069)
        if transition.opacity_s != 0:
            transition.transition_start(screen)

        pygame.display.update()
        pygame.display.flip()
#=====================================================================================================================





#=====================================================================================================================
def dialog2():

    counter = 1
    dialog_start = True
    volume = round(read('json/settings.json')['volume']['music_volume'], 1)
    end = False

    transition = Transition('images/__game_picture__/transitions/2.jpg','images/__game_picture__/transitions/3.jpg')

    while dialog_start:

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONUP:
                if counter < 40:
                    counter += 1

        screen.blit(dialogfont2_img, (0, 0))

        if end:
            if round(volume,2) > 0.00:
                volume -= 0.01

        music_list[1].set_volume(round(volume, 2))
        
        if counter == 40:
            if transition.stop_counter != 900:
                transition.transition_end(screen)
                end = True
            else:
                music_list[1].stop()
                music_list[1].set_volume(round(read('json/settings.json')['volume']['music_volume'], 1))
                first_level()
        else:
            text_field2.animate(screen)

        if counter <= 39:
            screen.blit(santa, (0,screen_height*0.069))

            #NIKOLAY =======================
            if counter == 1 or counter == 21 or counter == 24 or counter == 26 or counter == 30 or counter == 37:
                screen.blit(elf3, (screen_width-int(screen_width*0.172 + 331*0.3),screen_height-int(screen_height*0.469 + 507*0.3)))
                screen.blit(santa_black, (0,screen_height*0.069))
            if counter == 2 or counter == 20 or counter == 22 or counter == 23 or counter == 25 or counter == 29 or (counter >= 31 and counter <=  36) or counter == 38 or counter == 39:
                screen.blit(elf3, (screen_width-int(screen_width*0.172 + 331*0.3),screen_height-int(screen_height*0.469 + 507*0.3)))
                screen.blit(elf3_black, (screen_width-int(screen_width*0.172 + 331*0.3),screen_height-int(screen_height*0.469 + 507*0.3)))
            #NIKOLAY =======================

            #KATYA =========================
            if counter == 3 or counter == 13 or counter == 15 or counter == 17 or counter == 19 or counter == 28:
                screen.blit(elf2, (screen_width-int(screen_width*0.172 + 331*0.3),screen_height-int(screen_height*0.429 + 507*0.3)))
                screen.blit(santa_black, (0,screen_height*0.069))
            if counter == 4 or counter == 5 or counter == 11 or counter == 12 or counter == 14 or counter == 16 or counter == 18:
                screen.blit(elf2, (screen_width-int(screen_width*0.172 + 331*0.3),screen_height-int(screen_height*0.429 + 507*0.3)))
                screen.blit(elf2_black, (screen_width-int(screen_width*0.172 + 331*0.3),screen_height-int(screen_height*0.429 + 507*0.3)))
            #KATYA =========================

            #OLEG ==========================
            if counter == 9 or counter == 27:
                screen.blit(elf1, (screen_width-int(screen_width*0.172 + 331*0.3),screen_height-int(screen_height*0.469 + 507*0.3)))
                screen.blit(santa_black, (0,screen_height*0.069))
            if counter == 6 or counter == 7 or counter == 8 or counter == 10:
                screen.blit(elf1, (screen_width-int(screen_width*0.172 + 331*0.3),screen_height-int(screen_height*0.469 + 507*0.3)))
                screen.blit(elf1_black, (screen_width-int(screen_width*0.172 + 331*0.3),screen_height-int(screen_height*0.469 + 507*0.3)))
            #OLEG ==========================

            text2.draw_text(counter, screen_width*0.338, text_field2.hitbox.y + screen_height*0.069)

        if transition.opacity_s != 0:
            transition.transition_start(screen)

        pygame.display.update()
        clock.tick(60)
#=====================================================================================================================





#=====================================================================================================================
def dialog3():
    counter = 1
    dialog_start = True
    transition = Transition('images/__game_picture__/transitions/7.jpg','images/__game_picture__/transitions/8.png')

    music_list[1].play(loops=-1)

    volume = round(read('json/settings.json')['volume']['music_volume'], 1)
    end = False

    while dialog_start:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONUP:
                if counter < 21:
                    counter += 1
        screen.blit(diologfont_img, (0, 0))

        if end:
            if round(volume,2) > 0.00:
                volume -= 0.01

        music_list[1].set_volume(round(volume, 2))

        if counter == 21:
            if transition.stop_counter != 900:
                transition.transition_end(screen)
                end = True
            else:
                music_list[1].stop()
                music_list[1].set_volume(round(read('json/settings.json')['volume']['music_volume'], 1))
                credits()
        else:
            text_field.animate(screen)

        if counter <= 20:
            screen.blit(santa, (0,screen_height*0.069))

            #OLEG ==========================
            if counter == 4 or counter == 12 or counter == 18:
                screen.blit(elf1, (screen_width-int(screen_width*0.172 + 331*0.3),screen_height-int(screen_height*0.469 + 507*0.3)))
                screen.blit(santa_black, (0,screen_height*0.069))
            if (counter >= 1 and counter <= 3) or counter == 11 or counter == 13:
                screen.blit(elf1, (screen_width-int(screen_width*0.172 + 331*0.3),screen_height-int(screen_height*0.469 + 507*0.3)))
                screen.blit(elf1_black, (screen_width-int(screen_width*0.172 + 331*0.3),screen_height-int(screen_height*0.469 + 507*0.3)))
            #OLEG ==========================

            #KATYA =========================
            if counter == 5 or counter == 14 or counter == 19:
                screen.blit(elf2, (screen_width-int(screen_width*0.172 + 331*0.3),screen_height-int(screen_height*0.429 + 507*0.3)))
                screen.blit(santa_black, (0,screen_height*0.069))
            if counter == 6:
                screen.blit(elf2, (screen_width-int(screen_width*0.172 + 331*0.3),screen_height-int(screen_height*0.429 + 507*0.3)))
                screen.blit(elf2_black, (screen_width-int(screen_width*0.172 + 331*0.3),screen_height-int(screen_height*0.429 + 507*0.3)))
            #KATYA =========================

            #NIKOLAY =======================
            if counter == 8 or counter == 15 or counter == 20:
                screen.blit(elf3, (screen_width-int(screen_width*0.172 + 331*0.3),screen_height-int(screen_height*0.469 + 507*0.3)))
                screen.blit(santa_black, (0,screen_height*0.069))
            if counter == 7 or counter == 9 or counter == 10 or counter == 16 or counter == 17:
                screen.blit(elf3, (screen_width-int(screen_width*0.172 + 331*0.3),screen_height-int(screen_height*0.469 + 507*0.3)))
                screen.blit(elf3_black, (screen_width-int(screen_width*0.172 + 331*0.3),screen_height-int(screen_height*0.469 + 507*0.3)))
            #NIKOLAY =======================

            text3.draw_text(counter, screen_width*0.338, text_field2.hitbox.y + screen_height*0.069)

        if transition.opacity_s != 0:
            transition.transition_start(screen)

        pygame.display.update()
        clock.tick(60)
#=====================================================================================================================





#=====================================================================================================================
def first_level():

    game = True

    level = Level(level_map1, sounds_list)
    menu_open = False
    can_move = False
    level_end = False


    volume = round(read('json/settings.json')['volume']['music_volume'], 1)
    music_list[5].play(loops=-1)

    back = pygame.image.load('images/__game_picture__/background.png')
    back = pygame.transform.scale(back, (screen_width, screen_height))
    transition = Transition('images/__game_picture__/transitions/3.jpg','images/__game_picture__/transitions/4.jpg')

    mision_text = Text([
        "Збери всі 10 подарунків."
    ], (255,255,255), int(screen_width*0.018))
    menu_text = Text(['Меню'],(255,255,255),int(screen_width*0.026))

    while game:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.KEYUP:
                if ev.key == pygame.K_ESCAPE:
                    if menu_open == True:
                        menu_open = False
                    else:
                        menu_open = True
                if ev.key == pygame.K_e:
                    if level.player.hitbox.colliderect(level.exit.hitbox):
                        if len(level.drop_list) == 0:
                            level_end = True
            if ev.type == pygame.MOUSEBUTTONUP and menu_open == True:
                exit_button_game.action(main_menu, [music_list[5]])
                restart_button.action(first_level, [music_list[5]])

        screen.fill((55, 55, 55))
        level.show_background(screen, back)

        if menu_open:
            can_move = False
        else:
            can_move = True

        level.run(can_move, level_end)

        music_list[5].set_volume(round(volume, 2))

        if menu_open == True:
            bg.animate(screen)
            tab.animate(screen)
            exit_button_game.animate(screen)
            restart_button.animate(screen)
            menu_text.draw_game_text(tab.hitbox.x + screen_width*0.091, tab.hitbox.y + screen_height*0.027)
            mision_text.draw_game_text(tab.hitbox.x + screen_width*0.023, tab.hitbox.y + screen_height*0.138)

        if level_end == True:
            if transition.stop_counter == 900:
                music_list[5].stop()
                second_level()
            if round(volume,2) > 0.00:
                volume -= 0.01
            transition.transition_end(screen)

        if transition.opacity_s != 0:
            transition.transition_start(screen)
        else:
            can_move = True


        pygame.display.update()
        clock.tick(60)
#=====================================================================================================================





#=====================================================================================================================
def second_level(): 

    game = True

    volume = round(read('json/settings.json')['volume']['music_volume'], 1)
    music_list[6].play(loops=-1)

    level = Level(level_map2, sounds_list)
    menu_open = False
    level_end = False
    can_move = False

    back = pygame.image.load('images/__game_picture__/background.png')
    back = pygame.transform.scale(back, (screen_width, screen_height))

    transition = Transition('images/__game_picture__/transitions/4.jpg','images/__game_picture__/transitions/5.jpg')

    mision_text =Text([
        "  Збери всі інгредієнти",
        "  для чаю."
    ], (255,255,255), int(screen_width*0.018))
    menu_text = Text(['Меню'],(255,255,255),int(screen_width*0.026))

    while game:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.KEYUP:
                if ev.key == pygame.K_ESCAPE:
                    if menu_open == True:
                        menu_open = False
                    else:
                        menu_open = True
                if ev.key == pygame.K_e:
                    if level.player.hitbox.colliderect(level.exit.hitbox):
                        if len(level.drop_list) == 0:
                            level_end = True
            if ev.type == pygame.MOUSEBUTTONUP and menu_open == True:
                exit_button_game.action(main_menu,[music_list[6]])
                restart_button.action(second_level,[music_list[6]])

        screen.fill((55,55,55))
        level.show_background(screen, back)

        if menu_open:
            can_move = False
        else:
            can_move = True

        level.run(can_move, level_end)

        music_list[6].set_volume(round(volume, 2))

        if menu_open == True:
            bg.animate(screen)
            tab.animate(screen)
            exit_button_game.animate(screen)
            restart_button.animate(screen)
            menu_text.draw_game_text(tab.hitbox.x + screen_width*0.091, tab.hitbox.y + screen_height*0.027)
            mision_text.draw_game_text(tab.hitbox.x + screen_width*0.023, tab.hitbox.y + screen_height*0.138)

        if level_end == True:
            if transition.stop_counter == 900:
                music_list[6].stop()
                third_level()
            if round(volume,2) > 0.00:
                volume -= 0.01
            transition.transition_end(screen)
        
        if transition.opacity_s != 0:
            transition.transition_start(screen)
        else:
            can_move = True

        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)
#=====================================================================================================================





#=====================================================================================================================
def third_level():

    game = True
    background = pygame.image.load('images/__game_picture__/sled_background.png')
    background = pygame.transform.scale(background, (int(screen_width*2.083), screen_height))
    x = 0
    y = 0
    nikolay_sled.hitbox.x = nikolay_sled.start_x
    nikolay_sled.hitbox.y = nikolay_sled.start_y

    pigeon1 = Pigeon(window_size[0] + 400, random.randint(50, screen_height - int(screen_height*0.074) - 10), screen_width*0.059,screen_height*0.074,(10,10,10), "images/__game_picture__/bird.png", pigeon_animation, random.randint(int(screen_width*0.005), int(screen_width*0.008)))
    pigeon2 = Pigeon(window_size[0] + 400, random.randint(50, screen_height - int(screen_height*0.074) - 10), screen_width*0.059,screen_height*0.074,(10,10,10), "images/__game_picture__/bird.png", pigeon_animation, random.randint(int(screen_width*0.005), int(screen_width*0.008)))
    pigeon3 = Pigeon(window_size[0] + 400, random.randint(50, screen_height - int(screen_height*0.074) - 10), screen_width*0.059,screen_height*0.074,(10,10,10), "images/__game_picture__/bird.png", pigeon_animation, random.randint(int(screen_width*0.005), int(screen_width*0.008)))

    pigeons_lits = [pigeon1, pigeon2, pigeon3]

    for pigeons in pigeons_lits:
        pigeons.hitbox.x = pigeons.start_x
        pigeons.hitbox.y = pigeons.start_y
    menu_open = False
    end_game = False
    next_level = False
    timer = 0
    music_volume = round(read('json/settings.json')['volume']['music_volume'], 1)
    sounds_volume = round(read('json/settings.json')['volume']['sounds_volume'], 1)
    menu_text = Text(['Меню'],(255,255,255),int(screen_width*0.026))
    mision_text =Text([
        'Тримайся далі від',
        'пташок! Миколі потрібно',
        'доставити всі подарунки',
        'в цілості.'
    ], (255,255,255), int(screen_width*0.018))
    music_list[3].play(loops=-1)
    sounds_list[1].play(loops=-1)

    transition = Transition('images/__game_picture__/transitions/5.jpg','images/__game_picture__/transitions/6.jpg')

    tick_to_go = 0

    while game:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.KEYUP:
                if ev.key == pygame.K_ESCAPE and end_game is False:
                    if menu_open == True:
                        menu_open = False
                    else:
                        menu_open = True
            if ev.type == pygame.MOUSEBUTTONUP and menu_open == True:
                exit_button_game.action(main_menu, [music_list[3], sounds_list[1]])
                restart_button.action(third_level, [music_list[3], sounds_list[1]])
                

        screen.blit(background, (x,y))
        if menu_open == False:
            x -= 0.5
            nikolay_sled.move_sled()
            for pigeons in pigeons_lits:
                pigeons.fly()

        nikolay_sled.animate(screen)

        for pigeons in pigeons_lits:
            pigeons.animate(screen)
            if pigeons.hitbox.colliderect(nikolay_sled.hitbox) and tick_to_go < 1800:
                end_game = True
                menu_open = True

        music_list[3].set_volume(round(music_volume, 2))
        sounds_list[1].set_volume(round(sounds_volume, 2))

        if tick_to_go == 1800:
            menu_open = True
            next_level = True
            transition.transition_end(screen)

            timer += 1

            if round(music_volume,2) > 0.00:
                music_volume -= 0.02

            if round(sounds_volume,2) > 0.00:
                sounds_volume -= 0.02

            if transition.stop_counter >= 900:
                music_list[3].stop()
                sounds_list[1].stop()

                fourth_level()
        elif menu_open == False:
            tick_to_go += 1

        if (menu_open == True or end_game == True) and next_level == False:
            bg.animate(screen)
            tab.animate(screen)
            menu_text.draw_game_text(tab.hitbox.x + screen_width*0.091, tab.hitbox.y + screen_height*0.027)
            mision_text.draw_game_text(tab.hitbox.x + screen_width*0.023, tab.hitbox.y + screen_height*0.138)
            exit_button_game.animate(screen)
            restart_button.animate(screen)

        if transition.opacity_s != 0:
            transition.transition_start(screen)

        pygame.display.update()
        clock.tick(60)
#=====================================================================================================================





#=====================================================================================================================
def fourth_level():
    game = True

    level = Level(level_map3, sounds_list)
    menu_open = False
    level_end = False
    background = pygame.image.load('images/__game_picture__/background4.png')
    background = pygame.transform.scale(background, (int(screen_width*2.925), screen_height))

    volume = round(read('json/settings.json')['volume']['music_volume'], 1)
    music_list[4].play(loops=-1)

    transition = Transition('images/__game_picture__/transitions/6.jpg','images/__game_picture__/transitions/7.jpg')

    mision_text = Text([
        "Треба подалі",
        "триматися від людей,",
        "щоб вони тебе",
        "не побачили. Забери хліб",
        "та тікай через невидемі",
        "для людей двері."
    ], (255,255,255), int(screen_width*0.018))
    menu_text = Text(['Меню'],(255,255,255),int(screen_width*0.026))

    while game:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.KEYUP:
                if ev.key == pygame.K_ESCAPE:
                    if menu_open == True:
                        menu_open = False
                    elif level.stop_counter == 0:
                        menu_open = True
                if ev.key == pygame.K_e:
                    if level.player.hitbox.colliderect(level.exit.hitbox):
                        if len(level.drop_list) == 0:
                            level_end = True
            if ev.type == pygame.MOUSEBUTTONUP and (menu_open == True or level.stop_game == True):
                exit_button_game.action(main_menu, [music_list[4]])
                restart_button.action(fourth_level, [music_list[4]])

        screen.fill((55, 55, 55))
        level.show_background(screen, background, True)

        level.level_with_npc(menu_open, level_end)

        music_list[4].set_volume(round(volume, 2))

        if menu_open == True or level.stop_game == True:
            bg.animate(screen)
            tab.animate(screen)
            exit_button_game.animate(screen)
            restart_button.animate(screen)
            menu_text.draw_game_text(tab.hitbox.x + screen_width*0.091, tab.hitbox.y + screen_height*0.027)
            mision_text.draw_game_text(tab.hitbox.x + screen_width*0.023, tab.hitbox.y + screen_height*0.138)

        if level_end == True:
            if transition.stop_counter == 900:
                music_list[4].stop()
                dialog3()
            if round(volume,2) > 0.00:
                volume -= 0.01
            transition.transition_end(screen)

        if transition.opacity_s != 0:
            transition.transition_start(screen)

        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)
#=====================================================================================================================





#=====================================================================================================================
def credits():

    run = True
    length = credits_text.font.size(credits_text.text[0])[1]*len(credits_text.text)
    y = screen_height + screen_height*0.092
    skip = False
    transition = Transition('images/__game_picture__/transitions/8.png','images/__game_picture__/transitions/8.png')

    volume = round(read('json/settings.json')['volume']['music_volume'], 1)
    music_list[7].play(loops=-1)

    while run:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.KEYUP:
                if ev.key == pygame.K_ESCAPE:
                    skip = True

        screen.fill((0, 0, 0))
        y -= 1.5
        length -= 1.5

        music_list[7].set_volume(round(volume, 2))

        credits_text.draw_credits_text(y)

        if length < 100:
            if round(volume,2) > 0.00:
                volume -= 0.01

        if length < -50 or skip == True:
            music_list[7].stop()
            main_menu()

        if transition.opacity_s != 0:
            transition.transition_start(screen)

        pygame.display.update()
        clock.tick(60)
#=====================================================================================================================





#=====================================================================================================================
def options():

    background =  pygame.image.load('images/settings_background.png')
    background = pygame.transform.scale(background, (screen_width, screen_height))
    opt = True

    volume = read('json/settings.json')['volume']['music_volume']
    sounds = read('json/settings.json')['volume']['sounds_volume']

    music_volume = Text(['Музика'], (255, 255, 255), int(screen_width*0.036))
    sounds_volume = Text(['Звуки'], (255, 255, 255), int(screen_width*0.036))
    screen_settings = Text(['Розширення'], (255, 255, 255), int(screen_width*0.031))

    current_text = str(read('json/settings.json')['screen_size']['screen_width']) + ' x ' + str(read('json/settings.json')['screen_size']['screen_height'])
    current_size = [read('json/settings.json')['screen_size']['screen_width'],read('json/settings.json')['screen_size']['screen_height']]
    available_size = [[1280, 720],[1536, 864],[1920, 1080]]
    counter = 0
    screen_value = Text([current_text], (255, 255, 255), int(screen_width*0.021))
    reload_text = Text(['Перезаванажте гру, щоб зміни вступили в дію'], (240,0,0), int(screen_width*0.02))

    
    volume_minus_button = Button(screen_width*0.039, screen_height*0.069, screen_width*0.035, screen_height*0.324, 'images/__game_picture__/minus.png', 'images/__game_picture__/minus.png')
    volume_plus_button = Button(screen_width*0.039, screen_height*0.069, volume_minus_button.hitbox.right + screen_width*0.148, volume_minus_button.hitbox.y, 'images/__game_picture__/plus.png', 'images/__game_picture__/plus.png')

    volume_minus_button2 = Button(screen_width*0.039, screen_height*0.069, screen_width*0.035, screen_height*0.601, 'images/__game_picture__/minus.png', 'images/__game_picture__/minus.png')
    volume_plus_button2 = Button(screen_width*0.039, screen_height*0.069, volume_minus_button2.hitbox.right + screen_width*0.148, volume_minus_button2.hitbox.y, 'images/__game_picture__/plus.png', 'images/__game_picture__/plus.png')

    decrease = Button(screen_width*0.039, screen_height*0.069, screen_width*0.035, screen_height*0.878, 'images/__game_picture__/minus.png', 'images/__game_picture__/minus.png')
    increase = Button(screen_width*0.039, screen_height*0.069, decrease.hitbox.right + screen_width*0.148, decrease.hitbox.y, 'images/__game_picture__/plus.png', 'images/__game_picture__/plus.png')

    line = Object(None, volume_minus_button.hitbox.x + screen_width*0.039, volume_minus_button.hitbox.y + (volume_minus_button.hitbox.height//2-15), screen_width*0.148, 30, (0,0,0))
    line_into = Object(None, line.hitbox.x + 5, line.hitbox.y + 5, (line.hitbox.width - 10) * volume, 20, (255,255,255))

    line2 = Object(None, volume_minus_button2.hitbox.x + screen_width*0.039, volume_minus_button2.hitbox.y + (volume_minus_button2.hitbox.height//2-15), screen_width*0.148, 30, (0,0,0))
    line_into2 = Object(None, line2.hitbox.x + 5, line2.hitbox.y + 5, (line2.hitbox.width - 10) * sounds, 20, (255,255,255))

    while opt:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONUP:

                #-=-=-=-=-=-=-=-=- return to menu and saving
                return_button.action('press')
                if return_button.pressed == True:
                    data = {'volume': {'music_volume': round(volume, 1), 'sounds_volume': round(sounds, 1)}, 'screen_size': {'screen_width': current_size[0], 'screen_height': current_size[1]}}
                    write(data, 'json/settings.json')
                    return_button.pressed = False
                    music_list[0].stop()
                    main_menu()
                #-=-=-=-=-=-=-=-=- return to menu and saving
                increase.action('press')
                decrease.action('press')
                if increase.pressed == True:
                    for el in available_size:
                        if el != current_size and available_size[counter] != current_size:
                            counter += 1
                    if counter < len(available_size) - 1:
                        counter += 1
                        current_size = available_size[counter]
                        screen_value.text_list = [f'{current_size[0]} x {current_size[1]}']
                        
                    increase.pressed = False

                if decrease.pressed == True:
                    for el in available_size:
                        if el != current_size and available_size[counter] != current_size:
                            counter += 1
                    if counter > 0:
                        counter -= 1
                        current_size = available_size[counter]
                        screen_value.text_list = [f'{current_size[0]} x {current_size[1]}']
                        
                    decrease.pressed = False


                volume_minus_button.music_minus()
                volume_plus_button.music_minus()
                if volume_minus_button.pressed:
                    volume -= 0.1
                    volume_minus_button.pressed = False
                if volume_plus_button.pressed:
                    volume += 0.1
                    volume_plus_button.pressed = False

                volume_minus_button2.music_minus()
                volume_plus_button2.music_minus()
                if volume_minus_button2.pressed:
                    sounds -= 0.1
                    volume_minus_button2.pressed = False
                if volume_plus_button2.pressed:
                    sounds += 0.1
                    volume_plus_button2.pressed = False

        if round(volume, 1) <= 0:
            volume = 0
        elif round(volume, 1) >= 1:
            volume = 1

        if round(sounds, 1) <= 0:
            sounds = 0
        elif round(sounds, 1) >= 1:
            sounds = 1

        for music in music_list:
            music.set_volume(round(volume, 1))
        for sound in sounds_list:
            sound.set_volume(round(sounds, 1))

        screen.blit(background, (0,0))

        control.animate(screen)

        line_into.hitbox.width = (line.hitbox.width - 10) * volume
        line_into2.hitbox.width = (line2.hitbox.width - 10) * sounds
        line.draw(screen)
        line_into.draw(screen)
        line2.draw(screen)
        line_into2.draw(screen)
        music_volume.draw_game_text(volume_minus_button.hitbox.x + screen_width*0.052, volume_minus_button.hitbox.y - decrease.hitbox.height - screen_height*0.027)
        sounds_volume.draw_game_text(volume_minus_button2.hitbox.x + screen_width*0.065, volume_minus_button2.hitbox.y - decrease.hitbox.height - screen_height*0.027)
        screen_settings.draw_game_text(volume_minus_button2.hitbox.x + screen_width*0.0265, decrease.hitbox.y - decrease.hitbox.height - screen_height*0.027)
        screen_value.draw_game_text((decrease.hitbox.x + increase.hitbox.right - screen_value.width)/2, decrease.hitbox.y + screen_height*0.005)
        if current_size[0] != screen_width:
            reload_text.draw_game_text(screen_width*0.5,screen_height*0.05)

        return_button.animate(screen)
        volume_minus_button.animate(screen)
        volume_plus_button.animate(screen)
        volume_minus_button2.animate(screen)
        volume_plus_button2.animate(screen)
        increase.animate(screen)
        decrease.animate(screen)

        pygame.display.update()
        pygame.display.flip()
#=====================================================================================================================


main_menu()