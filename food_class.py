import sys

import pygame
class Food():
	"""a class to describe the food to be eaten by snake"""
	def __init__(self,screen,sn_settings):
		"""initializing food properties"""
		self.screen = screen
		self.sn_settings = sn_settings

	def draw_food(self, food_x_position, food_y_position):
		"""a circular food"""
		#position of food 
		self.center =[food_x_position, food_y_position]
		#if width == 0 is a fill, if width <0 nothing drawn, if width >0 increases width
		width = 0
		pygame.draw.circle(self.screen, self.sn_settings.food_color, self.center ,self.sn_settings.food_radius, 0)
