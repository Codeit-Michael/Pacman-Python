import pygame
import random
import time

from settings import WIDTH, CHAR_SIZE, PLAYER_SPEED

class Ghost(pygame.sprite.Sprite):
	def __init__(self, row, col):
		super().__init__()
		self.abs_x = (row * CHAR_SIZE)
		self.abs_y = (col * CHAR_SIZE)

		self.rect = pygame.Rect(self.abs_x, self.abs_y, CHAR_SIZE, CHAR_SIZE)
		self.pac_speed = PLAYER_SPEED
		self.color = pygame.Color("gray48")
		self.move_directions = [(-1,0), (0,-1), (1,0), (0,1)]

		self.directions = {'left': (-PLAYER_SPEED, 0), 'right': (PLAYER_SPEED, 0), 'up': (0, -PLAYER_SPEED), 'down': (0, PLAYER_SPEED)}
		self.keys = ['left', 'right', 'up', 'down']
		self.direction = (0, 0)


	def is_collide(self, x, y, walls_collide_list):
		tmp_rect = self.rect.move(x, y)
		if tmp_rect.collidelist(walls_collide_list) == -1:
			return False
		return True


	def update(self, screen, walls_collide_list):
		# ghost movement
		random_move = random.choice(self.keys)
		if not self.is_collide(*self.directions[random_move], walls_collide_list):
			self.direction = self.directions[random_move]
		if not self.is_collide(*self.direction, walls_collide_list):
			self.rect.move_ip(self.direction)

		# teleporting to the other side of the map
		if self.rect.right <= 0:
			self.rect.x = WIDTH
		elif self.rect.left >= WIDTH:
			self.rect.x = 0

		pygame.draw.rect(screen, self.color, self.rect)
