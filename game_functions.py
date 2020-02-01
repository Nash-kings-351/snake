import sys

import pygame

import random

from pygame.sprite import Sprite

from snake_class import Snake

def check_event(screen, sn_settings, snake):
	"""a function to check keyboard or mouse event"""
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				snake_director(event, sn_settings)


def update(screen, sn_settings, snake_list, snake, food):
	"""a function to display screen object on screen"""
	
	screen.fill(sn_settings.bg_color)
	
	#drawing food randomly
	food.draw_food(sn_settings.food_x_position, sn_settings.food_y_position)
	
	#increasing snake length every time screen update
	increase_snake_size(sn_settings,snake_list)
	
	# Redraw snake .
	snake.draw_snake(sn_settings,snake_list)

	#show the most recently drawn screen visible 
	pygame.display.update()
	
	#checking for collision
	checking_food_snake_collision(sn_settings,food, snake_list)

def increase_snake_size(sn_settings, snake_list):
	"""function to increase snake length"""
	snake_Head = []
	snake_Head.append(sn_settings.snake_rect_x)
	snake_Head.append(sn_settings.snake_rect_y)
	snake_list.append(snake_Head)
	#Deletes the added segment if snake is longer than the length it should be at that point
	if len(snake_list) > sn_settings.Length_of_snake:
		del snake_list[0]

	

def snake_director(event, sn_settings):
	"""function to change direction of the snake to aim fo food"""
	if event.key == pygame.K_DOWN:
		sn_settings.change_y = (1 * sn_settings.snake_height)
		sn_settings.change_x = 0
	elif event.key == pygame.K_LEFT:
		sn_settings.change_y = 0
		sn_settings.change_x = (-1 * sn_settings.snake_height)
	elif event.key == pygame.K_UP:
		sn_settings.change_y = (-1 * sn_settings.snake_height)
		sn_settings.change_x = 0
	elif event.key == pygame.K_RIGHT:
		sn_settings.change_y = 0
		sn_settings.change_x = (1 * sn_settings.snake_height)

def food_position_generator(sn_settings, food):
	"""generates random postion of food on the screen"""
	# there is need to revisit and know this random and randint functions
	sn_settings.food_x_position = round(random.randrange(0, sn_settings.screen_width-sn_settings.snake_height) / 10.0) * 10.0
	sn_settings.food_y_position = round(random.randrange(0, sn_settings.screen_height-sn_settings.snake_width) / 10.0) * 10.0

def checking_food_snake_collision(sn_settings, food, snake_list):
   if sn_settings.food_x_position  == sn_settings.snake_rect_x and sn_settings.food_y_position == sn_settings.snake_rect_y:
		#calling food radom generator
		food_position_generator(sn_settings, food)
		#incrementing snake length once a snake eat food
		sn_settings.Length_of_snake +=1