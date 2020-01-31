import pygame

from pygame.sprite import Sprite

class Snake(Sprite):
	def __init__(self, screen, sn_settings):

		super(Snake, self).__init__()
		
		self.screen = screen
		self.sn_settings = sn_settings
		

	def update(self, sn_settings):
		#to automate snake movement
		#change left or right 
		sn_settings.snake_rect_x += sn_settings.change_x
		#change down or up
		sn_settings.snake_rect_y += sn_settings.change_y

	def draw_snake(self,sn_settings, snake_list):
		"""function to draw snake on the screen"""
		for x in snake_list:
			pygame.draw.rect(self.screen, sn_settings.snake_color, [x[0], x[1], sn_settings.snake_height, sn_settings.snake_width])