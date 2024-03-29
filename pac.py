import pygame

from settings import CHAR_SIZE, PLAYER_SPEED

class Pac(pygame.sprite.Sprite):
	def __init__(self, row, col):
		super().__init__()

		self.abs_x = (row * CHAR_SIZE)
		self.abs_y = (col * CHAR_SIZE)

		# pac info 
		# img_path = 'assets/pac/pac.png'
		# self.image = pygame.image.load(img_path)
		# self.image = pygame.transform.scale(self.image, (CHAR_SIZE, CHAR_SIZE))
		# self.rect = self.image.get_rect(topleft = pos)
		# self.mask = pygame.mask.from_surface(self.image)
		self.rect = pygame.Rect(self.abs_x, self.abs_y, CHAR_SIZE, CHAR_SIZE)
		self.pac_speed = PLAYER_SPEED
		self.color = pygame.Color("yellow")
		self.immune_time = 0
		self.immune = False
	
		# pac status
		self.life = 3
		self.pac_score = 0


	def move_to_start_pos(self):
		self.rect.x = self.abs_x
		self.rect.y = self.abs_y


	def update(self, screen):
		pygame.draw.rect(screen, self.color, self.rect)

		# convert to countdown instead of FPS if possible
		self.immune = True if self.immune_time > 0 else False
		self.immune_time -= 1 if self.immune_time > 0 else 0