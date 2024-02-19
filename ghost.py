import pygame

from settings import CHAR_SIZE, PLAYER_SPEED

class Ghost(pygame.sprite.Sprite):
	def __init__(self, pos):
		super().__init__()
		self.row = pos[0]
		self.col = pos[1]
		self.abs_x = (self.row * CHAR_SIZE)
		self.abs_y = (self.col * CHAR_SIZE)

		self.rect = pygame.Rect(self.abs_x, self.abs_y, CHAR_SIZE, CHAR_SIZE)
		self.pac_speed = PLAYER_SPEED
		self.color = pygame.Color("gray48")


	def update(self, screen):
		pygame.draw.rect(screen, self.color, self.rect)