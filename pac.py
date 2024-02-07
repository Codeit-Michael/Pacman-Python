import pygame

from settings import CHAR_SIZE, PLAYER_SPEED

class Pac(pygame.sprite.Sprite):
	def __init__(self, pos, size):
		super().__init__()
		self.x = pos[0]
		self.y = pos[1]

		# pac info 
		# img_path = 'assets/pac/pac.png'
		# self.image = pygame.image.load(img_path)
		# self.image = pygame.transform.scale(self.image, (size, size))
		# self.rect = self.image.get_rect(topleft = pos)
		# self.mask = pygame.mask.from_surface(self.image)
		self.rect = pygame.Rect(self.x, self.y, CHAR_SIZE, CHAR_SIZE)
		self.pac_speed = PLAYER_SPEED
		self.color = (250, 120, 60)
	
		self.direction_move = {"left": False, "up": False, "right": False, "down": False}

		# pac status
		self.life = 3


	def move_left(self):
		self.rect.move_ip(-self.pac_speed, 0)

	def move_up(self):
		self.rect.move_ip(0, -self.pac_speed)

	def move_right(self):
		self.rect.move_ip(self.pac_speed, 0)

	def move_bottom(self):
		self.rect.move_ip(0, self.pac_speed)

	def update(self, screen):
		# to change: dont just draw, make the update moving (move and move_ip matter)
		pygame.draw.rect(screen, self.color, self.rect)