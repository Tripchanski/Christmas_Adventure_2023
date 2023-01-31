import pygame
import random
from modules.level_map import wall_size, window_size, screen, screen_height, screen_width
from modules.object import Object
from modules.hero import Hero
from modules.level_arm import Level_arm
from modules.door import Door
from modules.pickup import Pickup
from modules.platform import Platform
from modules.barrel import Barrel
from modules.npc import Npc
from modules.exit import Exit
from modules.make_text import Text

player1_images = ['images/animations/hero_1_1.png', 'images/animations/hero_1_2.png', 'images/animations/hero_1_3.png', 'images/animations/hero_1_1.png', 'images/animations/hero_1_4.png', 'images/animations/hero_1_5.png']
player2_images = ['images/animations/hero_2.png', 'images/animations/hero_2_3.png', 'images/animations/hero_2_4.png', 'images/animations/hero_2.png', 'images/animations/hero_2_1.png', 'images/animations/hero_2_2.png']
player3_images = ['images/animations/hero_3_1.png', 'images/animations/hero_3_2.png', 'images/animations/hero_3_3.png', 'images/animations/hero_3_1.png', 'images/animations/hero_3_4.png', 'images/animations/hero_3_5.png']
npc_images = ['images/animations/human.png', 'images/animations/human_3.png', 'images/animations/human_4.png', 'images/animations/human.png', 'images/animations/human_2.png', 'images/animations/human_1.png']

class Level:
    def __init__(self, level_data, sounds):
        self.layout = level_data
        self.setup_level(level_data)
        self.setup_camera(level_data)
        self.world_shift_x = 0
        self.world_shift_y = 0
        self.stop_move = False
        self.stop_game = False
        self.camera_move_y = False
        self.camera_move_x = False
        self.latest_platform = None
        self.stop_counter = 0
        self.sounds_counter = 0
        self.sounds = sounds
        self.const_drop_amount = len(self.drop_list)

    def setup_level(self, layout):
        self.wall_list = []
        self.level_arm_list = []
        self.door_list = []
        self.collide__list = []
        self.drop_list = []
        self.platform_list = []
        self.barrel_list = []
        self.npc_list = []
        self.info_image = None
        self.player = None
        self.exit = None
        self.background_x = 0
        self.background_y = (len(self.layout) - 10 * wall_size)-wall_size*2-30
        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                x = col_index * wall_size
                y = row_index * wall_size
                self.g_width = len(row) * 108
                if col == 'PO':
                    self.player = Hero(x, y - 42, 66, 160, (255, 0, 0), "images/__game_picture__/heroes/hero_1.png", player1_images, 5, 1)
                if col == 'PK':
                    self.player = Hero(x, y - 42, 56, 150, (255, 0, 0), "images/__game_picture__/heroes/hero_2.png", player2_images, 5, 2)
                if col == 'PN':
                    self.player = Hero(x, y - 42, 66, 160, (255, 0, 0), "images/__game_picture__/heroes/hero_3.png", player3_images, 5, 3)
                if col == 'SS':
                    self.exit = Exit('images/__game_picture__/door.png', x, y - wall_size*0.5, wall_size, wall_size + (wall_size*0.5), (0,0,0))
                if col == 'WV':
                    wall = Object('images/__game_picture__/fence_v_zipped.png', x, y, wall_size, wall_size, (119,136,153))
                    self.wall_list.append(wall)
                    self.collide__list.append(wall)
                if col == 'WS':
                    wall = Object('images/__game_picture__/snow2.png', x, y, wall_size, wall_size, (119,136,153))
                    self.wall_list.append(wall)
                    self.collide__list.append(wall)
                if col == 'WH':
                    wall = Object('images/__game_picture__/fence_h_zipped.png', x, y, wall_size, wall_size, (119,136,153))
                    self.wall_list.append(wall)
                    self.collide__list.append(wall)
                if col == 'WA':
                    wall = Object('images/__game_picture__/fence_center_zipped.png', x, y, wall_size, wall_size, (119,136,153))
                    self.wall_list.append(wall)
                    self.collide__list.append(wall)
                if col == 'PL':
                    wall = Object('images/__game_picture__/wall_v_left.png', x, y, wall_size, wall_size, (119,136,153))
                    self.wall_list.append(wall)
                    self.collide__list.append(wall)
                if col == 'PR':
                    wall = Object('images/__game_picture__/wall_v_right.png', x, y, wall_size, wall_size, (119,136,153))
                    self.wall_list.append(wall)
                    self.collide__list.append(wall)
                if col == 'PH':
                    wall = Object('images/__game_picture__/wall_h.png', x, y, wall_size, wall_size, (119,136,153))
                    self.wall_list.append(wall)
                    self.collide__list.append(wall)
                if col == 'P7':
                    wall = Object('images/__game_picture__/wall_h_reverse.png', x, y, wall_size, wall_size, (119,136,153))
                    self.wall_list.append(wall)
                    self.collide__list.append(wall)
                if col == 'P8':
                    wall = Object('images/__game_picture__/wall_end_up_reverse.png', x, y, wall_size, wall_size, (119,136,153))
                    self.wall_list.append(wall)
                    self.collide__list.append(wall)
                if col == 'PD':
                    wall = Object('images/__game_picture__/wall_v_end_down.png', x, y, wall_size, wall_size, (119,136,153))
                    self.wall_list.append(wall)
                    self.collide__list.append(wall)
                if col == 'PU':
                    wall = Object('images/__game_picture__/wall_h_end_up.png', x, y, wall_size, wall_size, (119,136,153))
                    self.wall_list.append(wall)
                    self.collide__list.append(wall)
                if col == 'P1':
                    wall = Object('images/__game_picture__/wall_corner_left.png', x, y, wall_size, wall_size, (119,136,153))
                    self.wall_list.append(wall)
                    self.collide__list.append(wall)
                if col == 'P2':
                    wall = Object('images/__game_picture__/wall_corner_right.png', x, y, wall_size, wall_size, (119,136,153))
                    self.wall_list.append(wall)
                    self.collide__list.append(wall)
                if col == 'P3':
                    wall = Object('images/__game_picture__/wall_h_end_right.png', x, y, wall_size, wall_size, (119,136,153))
                    self.wall_list.append(wall)
                    self.collide__list.append(wall)
                if col == 'P4':
                    wall = Object('images/__game_picture__/wall_h_end_left.png', x, y, wall_size, wall_size, (119,136,153))
                    self.wall_list.append(wall)
                    self.collide__list.append(wall)
                if col == 'P5':
                    wall = Object('images/__game_picture__/wall_corner_right_b.png', x, y, wall_size, wall_size, (119,136,153))
                    self.wall_list.append(wall)
                    self.collide__list.append(wall)
                if col == 'P6':
                    wall = Object('images/__game_picture__/wall_corner_left_b.png', x, y, wall_size, wall_size, (119,136,153))
                    self.wall_list.append(wall)
                    self.collide__list.append(wall)
                if col == 'MF':
                    wall = Object('images/__game_picture__/metal_block_full.png', x, y, wall_size, wall_size, (119,136,153))
                    self.wall_list.append(wall)
                    self.collide__list.append(wall)
                if col == 'M1':
                    wall = Object('images/__game_picture__/metal_block_left_end.png', x, y, wall_size, wall_size, (119,136,153))
                    self.wall_list.append(wall)
                    self.collide__list.append(wall)
                if col == 'M2':
                    wall = Object('images/__game_picture__/metal_block_right_end.png', x, y, wall_size, wall_size, (119,136,153))
                    self.wall_list.append(wall)
                    self.collide__list.append(wall)
                if col == 'MD':
                    wall = Object('images/__game_picture__/metal_block_bottom_end.png', x, y, wall_size, wall_size, (119,136,153))
                    self.wall_list.append(wall)
                    self.collide__list.append(wall)
                if col == 'MU':
                    wall = Object('images/__game_picture__/metal_block_top_end.png', x, y, wall_size, wall_size, (119,136,153))
                    self.wall_list.append(wall)
                    self.collide__list.append(wall)
                if col == 'MV':
                    wall = Object('images/__game_picture__/metal_block_v.png', x, y, wall_size, wall_size, (119,136,153))
                    self.wall_list.append(wall)
                    self.collide__list.append(wall)
                if col == 'MH':
                    wall = Object('images/__game_picture__/metal_block_h.png', x, y, wall_size, wall_size, (119,136,153))
                    self.wall_list.append(wall)
                    self.collide__list.append(wall)
                if col == 'M3':
                    wall = Object('images/__game_picture__/metal_block_corner_l.png', x, y, wall_size, wall_size, (119,136,153))
                    self.wall_list.append(wall)
                    self.collide__list.append(wall)
                if col == 'M4':
                    wall = Object('images/__game_picture__/metal_block_corner_r.png', x, y, wall_size, wall_size, (119,136,153))
                    self.wall_list.append(wall)
                    self.collide__list.append(wall)
                if col == 'M5':
                    wall = Object('images/__game_picture__/metal_block_corner_r_b.png', x, y, wall_size, wall_size, (119,136,153))
                    self.wall_list.append(wall)
                    self.collide__list.append(wall)
                if col == 'M6':
                    wall = Object('images/__game_picture__/metal_block_corner_l_b.png', x, y, wall_size, wall_size, (119,136,153))
                    self.wall_list.append(wall)
                    self.collide__list.append(wall)
                if col == 'WC':
                    wall = Object('images/__game_picture__/crate2.png', x, y, wall_size, wall_size, (119,136,153))
                    self.wall_list.append(wall)
                    self.collide__list.append(wall)
                if col == 'WW':
                    wall = Object('images/__game_picture__/wood.png', x, y, wall_size, wall_size*0.25, (119,136,153))
                    self.wall_list.append(wall)
                    self.collide__list.append(wall)
                if col == 'G1':
                    wall = Object('images/__game_picture__/ground.png', x, y, self.g_width, wall_size, (255, 255, 255), 'g')
                    self.wall_list.append(wall)
                    self.ground = wall
                if col == 'BB':
                    self.barrel_list.append(Barrel('images/__game_picture__/crate.png',x, y, wall_size, wall_size, (255, 0, 0)))
                if col == 'DG':
                    i = random.randint(1, 9)
                    drop = Pickup(f'images/gifts/gift_{i}.png', x + ((wall_size - 65) // 2), y + ((wall_size - 65) // 2), 65, 65, (222, 0, 255), 1)
                    self.drop_list.append(drop)
                    self.info_image = Object('images/gifts/gift_10.png', screen_width*0.010, screen_height*0.018, screen_width*0.056, screen_height*0.1, (119,136,153))
                if col == 'BD':
                    drop = Pickup('images/gifts/bread.png', x + ((wall_size - 100) // 2), y + (wall_size - 45), 100, 45, (222, 0, 255), 1)
                    self.drop_list.append(drop)
                if col == 'DC':
                    drop = Pickup('images/gifts/cup.png', x + ((wall_size - 65) // 2), y + ((wall_size - 65) // 2), 65, 65, (222, 0, 255), 1)
                    self.drop_list.append(drop)
                if col == 'DJ':
                    drop = Pickup('images/gifts/jar_of_jam.png', x + ((wall_size - 65) // 2), y + ((wall_size - 65) // 2), 65, 65, (222, 0, 255), 1)
                    self.drop_list.append(drop)
                if col == 'DW':
                    drop = Pickup('images/gifts/water.png', x + ((wall_size - 65) // 2), y + ((wall_size - 65) // 2), 65, 65, (222, 0, 255), 1)
                    self.drop_list.append(drop)
                if col == 'DB':
                    drop = Pickup('images/gifts/berry_plate.png', x + ((wall_size - 65) // 2), y + ((wall_size - 65) // 2), 65, 65, (222, 0, 255), 1)
                    self.drop_list.append(drop)
                if col == 'DT':
                    drop = Pickup('images/gifts/tea_leaf.png', x + ((wall_size - 65) // 2), y + ((wall_size - 65) // 2), 65, 65, (222, 0, 255), 1)
                    self.drop_list.append(drop)
                if col == 'DE':
                    drop = Pickup('images/gifts/teapot.png', x + ((wall_size - 90) // 2), y + ((wall_size - 68) // 2), 86, 64, (222, 0, 255), 1)
                    self.drop_list.append(drop)
                    self.info_image = Object('images/gifts/teapot.png', screen_width*0.010, screen_height*0.018, screen_height*0.116, screen_width*0.053, (119,136,153))
                if col == 'NR':
                    self.npc_list.append(Npc(-5, 'r', 'images/__game_picture__/heroes/elf.png', npc_images, x, y - 92, 56, 200, (255, 0, 0)))
                if col == 'NL':
                    self.npc_list.append(Npc(-5, 'l', 'images/__game_picture__/heroes/elf.png', npc_images, x, y - 92, 56, 200, (255, 0, 0)))
                if col == 'EE':
                    platform = Platform('down', 3, 2, 'y', 'images/__game_picture__/elevator.png', x, y, wall_size, 20, (47,79,79))
                    self.platform_list.append(platform)
                if col == 'ER':
                    platform = Platform('up', 2, 2, 'y', 'images/__game_picture__/elevator.png', x, y, wall_size, 20, (47,79,79))
                    self.platform_list.append(platform)
                if col == 'EF':
                    platform = Platform('up', 2, 2, 'y', 'images/__game_picture__/elevator.png',x, y, wall_size, 20, (47,79,79))
                    self.platform_list.append(platform)
                if col == 'EC':
                    platform = Platform('down', 4, 2, 'x', 'images/__game_picture__/elevator.png',x, y, wall_size, 20, (47,79,79))
                    self.platform_list.append(platform)
                if col == 'EG':
                    platform = Platform('up', 6, 2, 'y', 'images/__game_picture__/elevator.png',x, y, wall_size, 20, (47,79,79))
                    self.platform_list.append(platform)
                if col == 'EB':
                    platform = Platform('down', 8, 2, 'y', 'images/__game_picture__/elevator.png',x, y, wall_size * 2, 20, (47,79,79))
                    self.platform_list.append(platform)
                if col == 'EH':
                    platform = Platform('up', 3, 2, 'x', 'images/__game_picture__/elevator.png',x, y, wall_size, 20, (47,79,79))
                    self.platform_list.append(platform)
                if col == 'EA':
                    platform = Platform('up', 6, 2, 'x', 'images/__game_picture__/elevator.png',x, y, wall_size, 20, (47,79,79))
                    self.platform_list.append(platform)
                if col == 'ED':
                    platform = Platform('up', 5, 2, 'x', 'images/__game_picture__/elevator.png',x, y, wall_size, 20, (47,79,79))
                    self.platform_list.append(platform)
                if col == 'E0':
                    platform = Platform('down', 2, 2, 'y', 'images/__game_picture__/elevator.png', x, y, wall_size, 20, (47,79,79))
                    self.platform_list.append(platform)
                if col == 'E1':
                    platform = Platform('down', 4, 2, 'y', 'images/__game_picture__/elevator.png',x, y, wall_size, 20, (47,79,79))
                    self.platform_list.append(platform)
                if col == 'E2':
                    platform = Platform('down', 3, 2, 'y', 'images/__game_picture__/elevator.png',x, y, wall_size, 20, (47,79,79))
                    self.platform_list.append(platform)
                if col == 'E3':
                    platform = Platform('down', 5, 4, 'y', 'images/__game_picture__/elevator.png',x, y, wall_size * 2, 20, (47,79,79))
                    self.platform_list.append(platform)
                if col == 'E4':
                    platform = Platform('up', 5, 2, 'y', 'images/__game_picture__/elevator.png',x, y, wall_size, 20, (47,79,79))
                    self.platform_list.append(platform)
                if col == 'E5':
                    platform = Platform('up', 3, 2, 'y', 'images/__game_picture__/elevator.png',x, y, wall_size, 20, (47,79,79))
                    self.platform_list.append(platform)
                if col == 'E6':
                    platform = Platform('up', 4, 2, 'y', 'images/__game_picture__/elevator.png',x, y, wall_size, 20, (47,79,79))
                    self.platform_list.append(platform)
                if col == 'E7':
                    platform = Platform('down', 3, 2, 'x', 'images/__game_picture__/elevator.png',x, y, wall_size, 20, (47,79,79))
                    self.platform_list.append(platform)
                if col == 'E8':
                    platform = Platform('down', 2, 2, 'x', 'images/__game_picture__/elevator.png',x, y, wall_size, 20, (47,79,79))
                    self.platform_list.append(platform)
                if col == 'E9':
                    platform = Platform('up', 2, 2, 'x', 'images/__game_picture__/elevator.png',x, y, wall_size, 20, (47,79,79))
                    self.platform_list.append(platform)
                if col == 'D1':
                    door = Door('images/__game_picture__/force_door_zipped.png', x + ((wall_size - 60) // 2), y, 60, wall_size * 2, (139, 69, 19), 1)
                    self.door_list.append(door)
                    self.collide__list.append(door)
                if col == 'B1':
                    self.level_arm_list.append(Level_arm('images/__game_picture__/button_on.png', 'images/__game_picture__/button_off.png', x + ((wall_size - 54) // 2), y + ((wall_size - 54) // 2), 54, 54, 1))
                if col == 'D2':
                    door = Door('images/__game_picture__/force_door_zipped.png',x + ((wall_size - 60) // 2), y, 60, wall_size * 2, (139, 69, 19), 2)
                    self.door_list.append(door)
                    self.collide__list.append(door)
                if col == 'B2':
                    self.level_arm_list.append(Level_arm('images/__game_picture__/button_on.png', 'images/__game_picture__/button_off.png', x + ((wall_size - 54) // 2), y + ((wall_size - 54) // 2), 54, 54, 2))
                if col == 'D3':
                    door = Door('images/__game_picture__/force_door_zipped.png',x + ((wall_size - 60) // 2), y, 60, wall_size * 2, (139, 69, 19), 3)
                    self.door_list.append(door)
                    self.collide__list.append(door)
                if col == 'B3':
                    self.level_arm_list.append(Level_arm('images/__game_picture__/button_on.png', 'images/__game_picture__/button_off.png', x + ((wall_size - 54) // 2), y + ((wall_size - 54) // 2), 54, 54, 3))
                if col == 'D4':
                    door = Door('images/__game_picture__/force_door_zipped.png',x + ((wall_size - 60) // 2), y, 60, wall_size * 2, (139, 69, 19), 4)
                    self.door_list.append(door)
                    self.collide__list.append(door)
                if col == 'B4':
                    self.level_arm_list.append(Level_arm('images/__game_picture__/button_on.png', 'images/__game_picture__/button_off.png', x + ((wall_size - 54) // 2), y + ((wall_size - 54) // 2), 54, 54, 4))
                if col == 'D5':
                    door = Door('images/__game_picture__/force_door_zipped.png',x + ((wall_size - 60) // 2), y, 60, wall_size * 2, (139, 69, 19), 5)
                    self.door_list.append(door)
                    self.collide__list.append(door)
                if col == 'B5':
                    self.level_arm_list.append(Level_arm('images/__game_picture__/button_on.png', 'images/__game_picture__/button_off.png', x + ((wall_size - 54) // 2), y + ((wall_size - 54) // 2), 54, 54, 5))
                if col == 'D6':
                    door = Door('images/__game_picture__/force_door_zipped.png',x + ((wall_size - 60) // 2), y, 60, wall_size * 2, (139, 69, 19), 6)
                    self.door_list.append(door)
                    self.collide__list.append(door)
                if col == 'B6':
                    self.level_arm_list.append(Level_arm('images/__game_picture__/button_on.png', 'images/__game_picture__/button_off.png', x + ((wall_size - 54) // 2), y + ((wall_size - 54) // 2), 54, 54, 6))
                if col == 'D7':
                    door = Door('images/__game_picture__/force_door_zipped.png',x + ((wall_size - 60) // 2), y, 60, wall_size * 2, (139, 69, 19), 7)
                    self.door_list.append(door)
                    self.collide__list.append(door)
                if col == 'B7':
                    self.level_arm_list.append(Level_arm('images/__game_picture__/button_on.png', 'images/__game_picture__/button_off.png',x + ((wall_size - 54) // 2), y + ((wall_size - 54) // 2), 54, 54, 7))

    def setup_camera(self, layout):
        length = len(layout)
        wall_index = round(screen_height * (wall_size / screen_height), 0)
        camera_start = (length - (screen_height / wall_index)) * wall_index
        self.player.hitbox.y -= camera_start
        self.exit.hitbox.y -= camera_start
        for wall in self.wall_list:
            wall.hitbox.y -= camera_start
        for lv in self.level_arm_list:
            lv.hitbox.y -= camera_start
        for door in self.door_list:
            door.hitbox.y -= camera_start
        for drop in self.drop_list:
            drop.hitbox.y -= camera_start
        for platform in self.platform_list:
            platform.hitbox.y -= camera_start
        for barrel in self.barrel_list:
            barrel.hitbox.y -= camera_start
        for npc in self.npc_list:
            npc.hitbox.y -= camera_start

    def scroll_x(self):
        player_x = self.player.hitbox.centerx
        direction_x = self.player.direction.x

        if player_x < window_size[0] / 4 and direction_x < 0:
            self.world_shift_x = 5
            self.player.speed = 0
        elif player_x > window_size[0] - (window_size[0] / 4) and direction_x > 0:
            self.world_shift_x = -5
            self.player.speed = 0
        elif player_x < window_size[0] / 4 and direction_x == 0.0 and self.camera_move_x is True:
            self.world_shift_x = 2
            self.player.hitbox.x += 2
        elif player_x > window_size[0] - (window_size[0] / 4) and direction_x == 0.0 and self.camera_move_x is True:
            self.world_shift_x = -2
            self.player.hitbox.x -= 2
        else:
            self.world_shift_x = 0
            self.player.speed = 5

        if self.ground.hitbox.x >= 0 and direction_x < 0:
            self.world_shift_x = 0
            self.background_x = 0
            self.player.speed = 5
        elif self.ground.hitbox.right <= window_size[0] and direction_x > 0:
            self.world_shift_x = 0
            self.player.speed = 5

    def scroll_y(self):
        player_y = self.player.hitbox.centery
        direction_y = self.player.direction.y

        if player_y < window_size[1] / 4 and direction_y < 0:
            self.world_shift_y = (self.player.direction.y) * -1
            self.stop_move = True
        elif player_y > window_size[1] - (window_size[1] / 4) and direction_y > 0:
            self.world_shift_y = (self.player.direction.y) * -1
            self.stop_move = True
        elif player_y < window_size[1] / 4 and direction_y == 0.0 and self.camera_move_y is True:
            if self.latest_platform != None:
                self.world_shift_y = self.latest_platform.speed * 2
            self.stop_move = True
        else:
            self.world_shift_y = 0
            self.stop_move = False

        if self.ground.hitbox.bottom <= window_size[1] + self.player.direction.y and direction_y > 0:
            self.world_shift_y = 0
            self.stop_move = False

    def x_movement_collision(self):
        player = self.player
        player.hitbox.x += player.direction.x * player.speed

        if player.hitbox.left + 5 <= 0:
            player.hitbox.x = 0
            player.direction.x = 0
        elif player.hitbox.right - 5 >= window_size[0]:
            player.hitbox.x = window_size[0] - player.hitbox.width
            player.direction.x = 0

        for wall in self.collide__list:
            if wall.hitbox.colliderect(self.player.hitbox):
                if player.hitbox.right >= wall.hitbox.left and player.hitbox.right <= wall.hitbox.left + 5:
                    player.hitbox.right = wall.hitbox.left
                    self.world_shift_x = 0
                elif player.hitbox.left <= wall.hitbox.right and player.hitbox.left >= wall.hitbox.right - 5:
                    player.hitbox.left = wall.hitbox.right
                    self.world_shift_x = 0

    def y_movement_collision(self):
        player = self.player
        player.turnon_gravity(self.stop_move)

        for wall in self.wall_list:
            if wall.hitbox.colliderect(self.player.hitbox):
                if player.hitbox.top <= wall.hitbox.bottom and player.hitbox.bottom <= wall.hitbox.bottom - player.direction.y:
                    player.hitbox.bottom = wall.hitbox.top
                    player.direction.y = 0
                    player.on_ground = True
                    player.jumped = False

                elif player.hitbox.bottom >= wall.hitbox.top and player.hitbox.top <= wall.hitbox.bottom - player.jump_speed:
                    player.hitbox.top = wall.hitbox.bottom
                    player.direction.y = 0

        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False

    def platform_collision(self):
        player = self.player
        camera_x = 0
        camera_y = 0

        for platform in self.platform_list:
            if platform.hitbox.colliderect(self.player.hitbox):
                # X -=-=-
                if platform.direction == 'x':
                    if player.hitbox.right >= platform.hitbox.left and player.hitbox.right <= platform.hitbox.left + 5 + 2:
                        player.hitbox.right = platform.hitbox.left
                        self.world_shift_x = 0
                    elif player.hitbox.left <= platform.hitbox.right and player.hitbox.left >= platform.hitbox.right - 5 - 2:
                        player.hitbox.left = platform.hitbox.right
                        self.world_shift_x = 0
                elif platform.direction == 'y':
                    if player.hitbox.right >= platform.hitbox.left and player.hitbox.right <= platform.hitbox.left + 5:
                        player.hitbox.right = platform.hitbox.left
                        self.world_shift_x = 0
                    elif player.hitbox.left <= platform.hitbox.right and player.hitbox.left >= platform.hitbox.right - 5:
                        player.hitbox.left = platform.hitbox.right
                        self.world_shift_x = 0

                # Y -=-=-
                if platform.direction == 'x':
                    if player.hitbox.top <= platform.hitbox.bottom and player.hitbox.bottom <= platform.hitbox.top + player.direction.y:
                        player.hitbox.bottom = platform.hitbox.top
                        player.direction.y = 0
                        player.on_ground = True
                        player.hitbox.x -= platform.speed
                        camera_x += 1

                elif platform.direction == 'y':
                    if player.hitbox.top <= platform.hitbox.bottom and player.hitbox.bottom <= platform.hitbox.top + player.direction.y + platform.speed + 1:
                        player.hitbox.bottom = platform.hitbox.top
                        player.jumped = False
                        if platform.move_direction == 'down':
                            player.direction.y = abs(platform.speed)
                        else:
                            player.direction.y = 0
                        camera_y += 1
                        self.latest_platform = platform
                        player.on_ground = True
        if camera_x == 0:
            self.camera_move_x = False
        else:
            self.camera_move_x = True
        if camera_y == 0:
            self.camera_move_y = False
        else:
            self.camera_move_y = True


    def run(self, can_move, level_end):
        draw_hint = False
        btn = None

        for lv in self.level_arm_list:
            lv.animate(screen)
            lv.interaction(self.player)
            lv.update(self.world_shift_x, self.world_shift_y)
            if lv.is_on == False and self.player.hitbox.colliderect(lv.hitbox):
                draw_hint = True
                btn = lv
            for door in self.door_list:
                door.animate(screen)
                door.open(lv)
        for door in self.door_list:
            door.update(self.world_shift_x, self.world_shift_y)
        for wall in self.wall_list:
            wall.animate(screen)
            wall.update(self.world_shift_x, self.world_shift_y)
        for drop in self.drop_list:
            drop.animate(screen)
            drop.update(self.world_shift_x, self.world_shift_y)
            drop.collide(self.player, self.drop_list, drop)
        for platform in self.platform_list:
            platform.animate(screen)
            platform.update(self.world_shift_x, self.world_shift_y)
            if can_move:
                platform.move()

        self.exit.update(self.world_shift_x, self.world_shift_y)
        self.exit.animate(screen)

        if can_move:
            self.x_movement_collision()
        else:
            self.player.direction.y = 0
            self.player.direction.x = 0
            self.player.animCounter = 0

        if not level_end:
            if can_move:
                self.player.update()
            self.player.animate(screen)
        else:
            self.world_shift_x = 0
            self.world_shift_y = 0

        if self.player.direction.x != 0 and not self.camera_move_x and self.player.on_ground:
            if self.sounds_counter == 20:
                self.sounds[0].play()
                self.sounds_counter = 0

        if self.sounds_counter == 20:
            self.sounds_counter = 0
        self.sounds_counter += 1
        
        if draw_hint == True:
            screen.blit(btn.hint_image, (btn.hint.x, btn.hint.y))

        if can_move:
            self.y_movement_collision()
        self.platform_collision()

        self.info_image.animate(screen)
        self.info_text = Text([f'{self.const_drop_amount-len(self.drop_list)}/{self.const_drop_amount}'],(255,255,255),int(screen_width*0.019))
        self.info_text.draw_game_text(self.info_image.hitbox.x + (self.info_image.hitbox.width - self.info_text.width)/2, self.info_image.hitbox.y + (self.info_image.hitbox.height - self.info_text.height)/2)

    #=================================================================
    def show_background(self, screen, background, move=False):
        self.scroll_x()
        self.scroll_y()
        if move == True:
            if self.world_shift_x < 0:
                self.background_x += -screen_width*0.002
            elif self.world_shift_x > 0:
                self.background_x += screen_width*0.002
        
        if background != None:
            screen.blit(background, (self.background_x,0))
    #=================================================================

    #=================================================================
    def level_with_npc(self, menu_open, level_ended):

        self.ground.animate(screen)
        hiding = False

        if not menu_open and not self.stop_game and self.stop_counter == 0 and not level_ended:
            self.x_movement_collision()

        self.exit.animate(screen)

        if len(self.barrel_list) > 0:
            for barrel in self.barrel_list:
                barrel.animate(screen)
                barrel.update(self.world_shift_x, self.world_shift_y)
                if not menu_open and not self.stop_game and self.stop_counter == 0:
                    barrel.interaction(self.player, screen, self.barrel_list)
                if barrel.is_in == False:
                    if not menu_open and not self.stop_game and self.stop_counter == 0 and not level_ended:
                        self.player.update()
                    else:
                        self.player.animCounter = 0
                        self.player.direction.y = 0
                        self.player.direction.x = 0
                    hiding = False
                else:
                    hiding = True
                    self.player.direction.y = 0
                    self.player.direction.x = 0
        for drop in self.drop_list:
            drop.animate(screen)
            drop.update(self.world_shift_x, self.world_shift_y)
            drop.collide(self.player, self.drop_list, drop)

        if hiding == False and not level_ended:
            self.player.animate(screen)

        self.exit.update(self.world_shift_x, self.world_shift_y)

        for npc in self.npc_list:
            npc.update(self.world_shift_x, self.world_shift_y)
            if not menu_open:
                npc.walk(self.player, screen)
            if npc.direction == 'l':
                if npc.hitbox.right < random.randint(int(screen_width*0.156), int(screen_width*0.781))*-1 and not (self.ground.hitbox.right <= screen_width):
                    npc.hitbox.x = screen_width + random.randint(int(screen_width*0.494), int(screen_width*1.119))
            elif npc.direction == 'r':
                if npc.hitbox.x > screen_width + random.randint(int(screen_width*0.005), int(screen_width*0.781)) and not (self.ground.hitbox.right <= screen_width):
                    npc.hitbox.x = 0 - random.randint(int(screen_width*0.494), int(screen_width*1.119))
            if npc.stop_game or menu_open:
                npc.animCounter = 0
            npc.animate(screen)
            if npc.stop_game == True:
                for npcyara in self.npc_list:
                    npcyara.stop_game = True
                if self.stop_counter < 120:
                    self.stop_counter += 1
                else:
                    self.stop_game = True

        if self.player.direction.x != 0 and not self.camera_move_x and self.player.on_ground:
            if self.sounds_counter == 20:
                self.sounds[2].play()
                self.sounds_counter = 0

        if self.sounds_counter == 20:
            self.sounds_counter = 0
        self.sounds_counter += 1

        for wall in self.wall_list:
            wall.animate(screen)
            wall.update(self.world_shift_x, self.world_shift_y)
        
        self.y_movement_collision()
    #=================================================================