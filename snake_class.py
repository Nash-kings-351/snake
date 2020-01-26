import pygame
class Snake():
	def __init__(self, screen, sn_settings):
		self.screen = screen
		self.sn_settings = sn_settings
		self.snake_rect_x = 200
		self.snake_rect_y = 150
		self.snake_width  = 10
		self.snake_height = 10

	def draw_snake(self):
		"""function to draw snake on the screen"""
		snake=[self.snake_rect_x, self.snake_rect_y, self.snake_height, self.snake_width]

		pygame.draw.rect(self.screen,self.sn_settings.snake_color,snake)