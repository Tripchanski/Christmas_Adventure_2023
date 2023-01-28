from modules.object import Object
from modules.level_map import wall_size

class Platform(Object):
	def __init__(self, start_from, block_to_go, speed, direction, image, x, y, width, height, color, pk=None):
		super().__init__(image, x, y, width, height, color, pk)
		self.direction = direction
		self.start_from = start_from
		self.block_to_go = block_to_go
		self.move_counter = wall_size * block_to_go
		self.speed = speed
		self.const_speed = speed
		if self.start_from == 'down':
			self.move_direction = 'up'
		elif self.start_from == 'up':
			self.move_direction = 'down'
			self.speed = self.const_speed * -1

	def move(self):
		if self.direction == 'y':
			if self.move_direction == 'up':
				if self.move_counter > 0:
					self.hitbox.y -= self.speed
					self.move_counter -= abs(self.speed)
				else:
					self.move_direction = 'down'
					self.move_counter = wall_size * self.block_to_go
					self.speed = self.const_speed * -1
			elif self.move_direction == 'down':
				if self.move_counter > 0:
					self.hitbox.y -= self.speed
					self.move_counter -= abs(self.speed)
				else:
					self.move_direction = 'up'
					self.move_counter = wall_size * self.block_to_go
					self.speed = self.const_speed



		elif self.direction == 'x':
			if self.move_direction == 'up':
				if self.move_counter > 0:
					self.hitbox.x -= self.speed
					self.move_counter -= abs(self.speed)
				else:
					self.move_direction = 'down'
					self.move_counter = wall_size * self.block_to_go
					self.speed = self.const_speed * -1
			elif self.move_direction == 'down':
				if self.move_counter > 0:
					self.hitbox.x -= self.speed
					self.move_counter -= abs(self.speed)
				else:
					self.move_direction = 'up'
					self.move_counter = wall_size * self.block_to_go
					self.speed = self.const_speed