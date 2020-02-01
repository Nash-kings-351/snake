import sys

import pygame
class Food():
	"""a class to describe the food to be eaten by snake"""
	def __init__(self,screen,sn_settings):
		"""initializing food properties"""
		self.screen = screen
		self.sn_settings = sn_settings

	def draw_food(self, food_x_position, food_y_position):
		"""a funtion to draw a square food"""
		#position of food 
		self.center =[food_x_position, food_y_position]
		pygame.draw.rect(self.screen, self.sn_settings.food_color, [food_x_position, food_y_position ,self.sn_settings.food_length, self.sn_settings.food_length])
