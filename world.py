import pygame

from pac import Pac
from settings import WIDTH, HEIGHT, CHAR_SIZE, MAP
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


	# display nav
	def add_additionals(self):
		pass


	def _detect_collisions(self):
		# checks if player bullet hits the enemies (aliens)
		player_attack_collision = pygame.sprite.groupcollide(self.aliens, self.player.sprite.player_bullets, True, True)
		if player_attack_collision:
			self.player_score += 10

		# checks if the aliens' bullet hit the player
		for alien in self.aliens.sprites():	
			alien_attack_collision = pygame.sprite.groupcollide(alien.bullets, self.player, True, False)
			if alien_attack_collision:
				self.player.sprite.life -= 1
				break

		# checks if the aliens hit the player
		alien_to_player_collision = pygame.sprite.groupcollide(self.aliens, self.player, True, False)
		if alien_to_player_collision:
			self.player.sprite.life -= 1


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

		# player ship rendering
		self.player.update(self.screen)
		# self.player.draw(self.screen)		# temporarily removed
	