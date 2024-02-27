import pygame
import random
import time

from settings import CHAR_SIZE, PLAYER_SPEED

class Ghost(pygame.sprite.Sprite):
	def __init__(self, row, col):
		super().__init__()
		self.abs_x = (row * CHAR_SIZE)
		self.abs_y = (col * CHAR_SIZE)

		self.rect = pygame.Rect(self.abs_x, self.abs_y, CHAR_SIZE, CHAR_SIZE)
		self.pac_speed = PLAYER_SPEED
		self.color = pygame.Color("gray48")
		self.move_directions = [(-1,0), (0,-1), (1,0), (0,1)]

	def update(self, screen, wall_id_list):
		while True:
			direction = random.choice(self.move_directions)
			curr_x, curr_y = self.rect.x // CHAR_SIZE, self.rect.y // CHAR_SIZE
			new_id = (curr_x + direction[0], curr_y  + direction[1])
			if new_id not in wall_id_list:
				self.rect.move_ip(direction)

				pygame.draw.rect(screen, self.color, self.rect)
				break	

