import pygame
from modules.level_map import wall_size, Wall, window_size, screen
from modules.hero import Hero

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
    
    def setup_level(self, layout):
        self.wall_list = []
        self.player = None
        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                x = col_index * wall_size
                y = row_index * wall_size
                if col == 'X':
                    wall = Wall(x, y, wall_size, wall_size, (190, 20, 190))
                    self.wall_list.append(wall)
                if col == 'G':
                    wall = Wall(x, y, wall_size, wall_size, (255, 255, 255))
                    self.wall_list.append(wall)
                if col == 'P':
                    self.player = Hero(x, y - 92, 56, 200, (255,0,0), "hero_2.png", None, 5)

    def scroll_x(self):
        player_x = self.player.hitbox.centerx
        direction_x = self.player.direction.x

        if player_x < window_size[0] / 4 and direction_x < 0:
            self.world_shift = 5
            self.player.speed = 0
        elif player_x > window_size[0] - (window_size[0] / 4) and direction_x > 0:
            self.world_shift = -5
            self.player.speed = 0
        else:
            self.world_shift = 0
            self.player.speed = 5

    def x_movement_collision(self):
        player = self.player
        player.hitbox.x += player.direction.x * player.speed
        
        for wall in self.wall_list:
            if wall.hitbox.colliderect(self.player.hitbox):
                if player.direction.x < 0:
                    player.hitbox.left = wall.hitbox.right
                elif player.direction.x > 0:
                    player.hitbox.right = wall.hitbox.left

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
            wall.update(self.world_shift)
        self.scroll_x()

        self.x_movement_collision()
        self.player.animate(screen)
        self.player.update()
        self.y_movement_collision()