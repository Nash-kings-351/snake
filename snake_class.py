import pygame

class Snake():
	def __init__(self, screen, sn_settings):

		self.screen = screen
		self.sn_settings = sn_settings
		

	def update(self, sn_settings):
		"""a function to automate snake movement"""
			#bug to fix later 
		if (sn_settings.snake_rect_x < 0):
			sn_settings.snake_rect_x += sn_settings.max_right
		if (sn_settings.snake_rect_x > sn_settings.max_right):
			sn_settings.snake_rect_x -= sn_settings.max_right
		if (sn_settings.snake_rect_y < 0):
			sn_settings.snake_rect_y += sn_settings.max_buttom
		if (sn_settings.snake_rect_y > sn_settings.max_buttom):
			sn_settings.snake_rect_y -= sn_settings.max_buttom
		#move  left or right 
		sn_settings.snake_rect_x += sn_settings.change_x
		#move down or up
		sn_settings.snake_rect_y += sn_settings.change_y

	def draw_snake(self,sn_settings, snake_list):
		"""function to draw snake on the screen"""
		for x in snake_list:
			pygame.draw.rect(self.screen, sn_settings.snake_color, [x[0], x[1], sn_settings.snake_height, sn_settings.snake_width])