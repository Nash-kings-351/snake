import pygame
class Snake():
	def __init__(self, screen, sn_settings):
		self.screen = screen
		self.sn_settings = sn_settings

	def draw_snake(self, snake_demension):
		"""function to draw snake on the screen"""
		self.snake_demension = snake_demension
		pygame.draw.rect(self.screen, self.sn_settings.snake_color, self.snake_demension)