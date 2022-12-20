import pygame
from modules.level_map import wall_size, window_size, screen
from modules.wall import Wall
from modules.hero import Hero

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.setup_camera(level_data)
        self.world_shift_x = 0
        self.world_shift_y = 0
    
    def setup_level(self, layout):
        self.wall_list = []
        self.player = None
        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                x = col_index * wall_size
                y = row_index * wall_size
                self.g_width = len(row) * 108
                if col == 'X':
                    wall = Wall(x, y, wall_size, wall_size, (190, 20, 190))
                    self.wall_list.append(wall)
                if col == 'G':
                    wall = Wall(x, y, self.g_width, wall_size, (255, 255, 255), 'g')
                    self.wall_list.append(wall)
                if col == 'P':
                    self.player = Hero(x, y - 92, 56, 200, (255,0,0), "hero_2.png", None, 5)

    def setup_camera(self, layout):
        length = len(layout)
        camera_start = (length - 10) * wall_size
        self.player.hitbox.y -= camera_start
        for wall in self.wall_list:
            wall.hitbox.y -= camera_start

    def scroll_x(self):
        player_x = self.player.hitbox.centerx
        direction_x = self.player.direction.x
        
        if player_x < window_size[0] / 4 and direction_x < 0:
            self.world_shift_x = 5
            self.player.speed = 0
        elif player_x > window_size[0] - (window_size[0] / 4) and direction_x > 0:
            self.world_shift_x = -5
            self.player.speed = 0
        else:
            self.world_shift_x = 0
            self.player.speed = 5

        for wall in self.wall_list:
            if wall.id == 'g':
                if wall.hitbox.x >= 0 and direction_x < 0:
                    self.world_shift_x = 0
                    self.player.speed = 5
                elif wall.hitbox.right <= window_size[0] and direction_x > 0:
                    self.world_shift_x = 0
                    self.player.speed = 5

    def scroll_y(self):
        if self.player.hitbox.bottom < 0:
            self.world_shift_y = window_size[1]
            self.player.hitbox.bottom = window_size[1] - self.player.height
        elif self.player.hitbox.bottom > window_size[1]:
            self.world_shift_y = -window_size[1]
            self.player.hitbox.bottom = 1
        else:
            self.world_shift_y = 0

    def x_movement_collision(self):
        player = self.player
        player.hitbox.x += player.direction.x * player.speed
        
        for wall in self.wall_list:
            if wall.hitbox.colliderect(self.player.hitbox):
                if player.hitbox.right >= wall.hitbox.left and player.hitbox.right <= wall.hitbox.left + 5:
                    player.hitbox.right = wall.hitbox.left
                    self.world_shift_x = 0
                elif player.hitbox.left <= wall.hitbox.right and player.hitbox.left >= wall.hitbox.right - 5:
                    player.hitbox.left = wall.hitbox.right
                    self.world_shift_x = 0

    def y_movement_collision(self):
        player = self.player
        player.turnon_gravity()

        for wall in self.wall_list:
            if wall.hitbox.colliderect(self.player.hitbox):
                if player.direction.y > 0:
                    player.hitbox.bottom = wall.hitbox.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.hitbox.top = wall.hitbox.bottom
                    player.direction.y = 0

        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False


    def run(self):
        for wall in self.wall_list:
            wall.draw(screen)
            wall.update(self.world_shift_x, self.world_shift_y)
        self.scroll_x()
        self.scroll_y()

        self.x_movement_collision()
        self.player.animate(screen)
        self.player.update()
        self.y_movement_collision()