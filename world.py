import pygame

from settings import WIDTH, CHAR_SIZE, MAP, PLAYER_SPEED
from pac import Pac
from cell import Cell
from berry import Berry
from ghost import Ghost

class World:
	def __init__(self, screen):
		self.screen = screen

		self.player = pygame.sprite.GroupSingle()
		self.ghosts = pygame.sprite.Group()
		self.walls = pygame.sprite.Group()
		self.berries = pygame.sprite.Group()

		# self.display = Display(self.screen)

		self.game_over = False
		self.player_score = 0
		self.game_level = 1

		self.directions = {'left': (-PLAYER_SPEED, 0), 'right': (PLAYER_SPEED, 0), 'up': (0, -PLAYER_SPEED), 'down': (0, PLAYER_SPEED)}
		self.keys = {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT, 'up': pygame.K_UP, 'down': pygame.K_DOWN}
		self.direction = (0, 0)

		self._generate_world()


	# create and add player to the screen
	def _generate_world(self):
		# renders obstacle from the MAP table
		for y_index, col in enumerate(MAP):
			for x_index, char in enumerate(col):
				if char == "1":	# for walls
					self.walls.add(Cell(x_index, y_index, CHAR_SIZE, CHAR_SIZE))
				elif char == " ":	 # for paths to be filled with berries
					self.berries.add(Berry(x_index, y_index, CHAR_SIZE // 4))
				elif char == "B":	# for big berries
					self.berries.add(Berry(x_index, y_index, CHAR_SIZE // 2))
				elif char == "g":	# for Ghosts's starting position 
					self.ghosts.add(Ghost(x_index, y_index))
				elif char == "p":	# for Pacman's starting position 
					self.player.add(Pac(x_index, y_index))

		self.walls_collide_list = [wall.rect for wall in self.walls.sprites()]


	# display nav
	def add_additionals(self):
		pass


	def is_collide(self, x, y):
		tmp_rect = self.player.sprite.rect.move(x, y)
		if tmp_rect.collidelist(self.walls_collide_list) == -1:
			return False
		return True


	def update(self):
		[wall.update(self.screen) for wall in self.walls.sprites()]
		[berry.update(self.screen) for berry in self.berries.sprites()]
		[ghost.update(self.screen, self.walls_collide_list) for ghost in self.ghosts.sprites()]

		# player movement
		if not self.game_over:
			pressed_key = pygame.key.get_pressed()
			for key, key_value in self.keys.items():
				if pressed_key[key_value] and not self.is_collide(*self.directions[key]):
					self.direction = self.directions[key]
					break
			if not self.is_collide(*self.direction):
				self.player.sprite.rect.move_ip(self.direction)

			# pacman eating-berry effect
			for berry in self.berries.sprites():
				if self.player.sprite.rect.colliderect(berry.rect):
					berry.kill()
					self.player.sprite.pac_score += 10

			# teleporting to the other side of the map
			if self.player.sprite.rect.right <= 0:
				self.player.sprite.rect.x = WIDTH
			elif self.player.sprite.rect.left >= WIDTH:
				self.player.sprite.rect.x = 0

		# pacman rendering
		self.player.update(self.screen)
		# self.player.draw(self.screen)		# temporarily removed
	