import pygame

from settings import CHAR_SIZE, PLAYER_SPEED

class Pac(pygame.sprite.Sprite):
	def __init__(self, pos, size):
		super().__init__()
		self.row = pos[0]
		self.col = pos[1]
		self.abs_x = (self.row * CHAR_SIZE)
		self.abs_y = (self.col * CHAR_SIZE)

		# pac info 
		# img_path = 'assets/pac/pac.png'
		# self.image = pygame.image.load(img_path)
		# self.image = pygame.transform.scale(self.image, (size, size))
		# self.rect = self.image.get_rect(topleft = pos)
		# self.mask = pygame.mask.from_surface(self.image)
		self.rect = pygame.Rect(self.abs_x, self.abs_y, CHAR_SIZE, CHAR_SIZE)
		self.pac_speed = PLAYER_SPEED
		self.color = pygame.Color("yellow")
	
		# pac status
		self.life = 3


	def update(self, screen):
		pygame.draw.rect(screen, self.color, self.rect)