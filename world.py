import pygame

from pac import Pac
from settings import WIDTH, HEIGHT, CHAR_SIZE, MAP
from cell import Cell

class World:
	def __init__(self, screen):
		self.screen = screen

		# self.player = pygame.sprite.GroupSingle()	# temporarily removed
		self.ghosts = pygame.sprite.Group()
		# self.display = Display(self.screen)

		self.game_over = False
		self.player_score = 0
		self.game_level = 1

		self._generate_world()


	# create and add player to the screen
	def _generate_world(self):
		player_pos = ((WIDTH // 2) - (CHAR_SIZE // 2), (HEIGHT // 2) - (CHAR_SIZE // 2))
		# self.player.add(Pac(player_pos, CHAR_SIZE))	# temporarily removed
		
		# renders obstacle from the MAP table
		self.cells = []
		for y_index, col in enumerate(MAP):
			cell_size = ((WIDTH // len(col)), (HEIGHT // len(MAP)))
			for x_index, char in enumerate(col):
				if char == "1":
					self.cells.append(Cell(x_index, y_index, cell_size))
				elif char == " ":
					self.cells.append(Cell(x_index, y_index, cell_size, is_open = True))


	# display nav
	def add_additionals(self):
		pass


	def player_move(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_a] and not self.game_over or keys[pygame.K_LEFT] and not self.game_over:
			if self.player.sprite.rect.left > 0:
				self.player.sprite.move_left()
		if keys[pygame.K_d] and not self.game_over or keys[pygame.K_RIGHT] and not self.game_over:
			if self.player.sprite.rect.right < WIDTH:
				self.player.sprite.move_right()
		if keys[pygame.K_w] and not self.game_over or keys[pygame.K_UP] and not self.game_over:
			if self.player.sprite.rect.top > 0:
				self.player.sprite.move_up()		
		if keys[pygame.K_s] and not self.game_over or keys[pygame.K_DOWN] and not self.game_over:
			if self.player.sprite.rect.bottom < HEIGHT:
				self.player.sprite.move_bottom()


	def update(self):
		# player ship rendering
		# self.player.update(self.screen)	# temporarily removed
		# self.player.draw(self.screen)		# temporarily removed
		[cell.draw(self.screen) for cell in self.cells]