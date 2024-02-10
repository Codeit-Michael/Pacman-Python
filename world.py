import pygame

from pac import Pac
from settings import WIDTH, HEIGHT, CHAR_SIZE, MAP, PLAYER_SPEED
from cell import Cell

class World:
	def __init__(self, screen):
		self.screen = screen

		self.player = pygame.sprite.GroupSingle()
		# self.ghosts = pygame.sprite.Group()
		self.walls = pygame.sprite.Group()
		self.path = pygame.sprite.Group()

		# self.display = Display(self.screen)

		self.game_over = False
		self.player_score = 0
		self.game_level = 1

		self.directions = {'a': (-PLAYER_SPEED, 0), 'd': (PLAYER_SPEED, 0), 'w': (0, -PLAYER_SPEED), 's': (0, PLAYER_SPEED)}
		self.keys = {'a': pygame.K_a, 'd': pygame.K_d, 'w': pygame.K_w, 's': pygame.K_s}
		self.direction = (0, 0)

		self._generate_world()


	# create and add player to the screen
	def _generate_world(self):
		player_pos = ((WIDTH // 2) - (CHAR_SIZE // 2), (HEIGHT // 2) - (CHAR_SIZE // 2))
		self.player.add(Pac(player_pos, CHAR_SIZE))
		
		# renders obstacle from the MAP table
		for y_index, col in enumerate(MAP):
			for x_index, char in enumerate(col):
				if char == "1":
					self.walls.add(Cell(x_index, y_index, (CHAR_SIZE, CHAR_SIZE)))
				elif char == " ":
					self.path.add(Cell(x_index, y_index, (CHAR_SIZE, CHAR_SIZE), is_open = True))

		self.walls_collide_list = [wall.rect for wall in self.walls.sprites()]


	# display nav
	def add_additionals(self):
		pass


	def is_collide(self, x, y):
		tmp_rect = self.player.sprite.rect.move(x, y)
		if tmp_rect.collidelist(self.walls_collide_list) == -1:
			return False
		return True


	def player_move(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_a] and not self.game_over or keys[pygame.K_LEFT] and not self.game_over:
			if self.player.sprite.rect.left > 0:
				self.player.sprite.move_left()
		elif keys[pygame.K_d] and not self.game_over or keys[pygame.K_RIGHT] and not self.game_over:
			if self.player.sprite.rect.right < WIDTH:
				self.player.sprite.move_right()
		elif keys[pygame.K_w] and not self.game_over or keys[pygame.K_UP] and not self.game_over:
			if self.player.sprite.rect.top > 0:
				self.player.sprite.move_up()		
		elif keys[pygame.K_s] and not self.game_over or keys[pygame.K_DOWN] and not self.game_over:
			if self.player.sprite.rect.bottom < HEIGHT:
				self.player.sprite.move_bottom()


	def update(self):
		[path.update(self.screen) for path in self.path.sprites()]
		[wall.update(self.screen) for wall in self.walls.sprites()]

		pressed_key = pygame.key.get_pressed()
		for key, key_value in self.keys.items():
			if pressed_key[key_value] and not self.is_collide(*self.directions[key]):
				self.direction = self.directions[key]
				break
		if not self.is_collide(*self.direction):
				self.player.sprite.rect.move_ip(self.direction)

		# player ship rendering
		self.player.update(self.screen)
		# self.player.draw(self.screen)		# temporarily removed
	