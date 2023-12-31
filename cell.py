import pygame

class Cell:
	def __init__(self, row, col, cell_size, is_open = False):
		self.row = row
		self.col = col
		self.cell_size = cell_size
		self.width = self.cell_size[0]
		self.height = self.cell_size[1]
		self.abs_x = row * self.width
		self.abs_y = col * self.height

		self.rect = pygame.Rect(
			self.abs_x,
			self.abs_y,
			self.width,
			self.height
		)

		self.is_open = is_open

		self.occupying_piece = None

	def draw(self, display):
		if self.is_open:
			pygame.draw.rect(display, (0,0,0), self.rect)
		else:
			pygame.draw.rect(display, (100,100,100), self.rect)