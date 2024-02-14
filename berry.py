import pygame

from settings import CHAR_SIZE, PLAYER_SPEED

class Berry(pygame.sprite.Sprite):
	def __init__(self, pos, size):
		super().__init__()
		self.row = pos[0]
		self.col= pos[1]
		self.size = size
		self.color = pygame.Color("red")
		self.thickness = size
		self.abs_x = (self.row * CHAR_SIZE) + (CHAR_SIZE // 2)
		self.abs_y = (self.col * CHAR_SIZE) + (CHAR_SIZE // 2)

	def update(self, screen):
		self.rect = pygame.draw.circle(screen, self.color, (self.abs_x, self.abs_y), self.size, self.thickness)
		
