import sys

import pygame

import random

from pygame.sprite import Sprite

from snake_class import Snake

def check_event(screen, sn_settings, Snake_1,food):
	"""a function to check keyboard or mouse event"""
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				snake_director(event, screen, sn_settings, Snake_1)


def update(screen, sn_settings, snake_list, Snake_1, food):
	"""a function to display screen object on screen"""
	automate_snake_movement(sn_settings, snake_list)
	checking_food_snake_collision(screen, sn_settings,food, snake_list, Snake_1)
	screen.fill(sn_settings.bg_color)
	#snake_director(event, screen, sn_settings, snake)
	
	#drawing food randomly
	food.draw_food(sn_settings.food_x_position, sn_settings.food_y_position)

	increase_snake_size(screen, sn_settings,snake_list)
	# Redraw snake .
	Snake_1.draw_snake(sn_settings,snake_list)

	#pygame.draw.rect(screen,sn_settings.snake_color,[200,150,10,10])
	#show the most recently drawn screen visible 
	
	pygame.display.update()
	# Make the most recently drawn screen visible.
	#pygame.display.flip()
	automate_snake_movement(sn_settings, Snake_1)
	checking_food_snake_collision(screen, sn_settings,food, snake_list, Snake_1)
	


	

def automate_snake_movement(sn_settings, Snake_1):

	#bug to fix later 
	if (sn_settings.snake_rect_x < 0):
		sn_settings.snake_rect_x += sn_settings.max_right
	if (sn_settings.snake_rect_x > sn_settings.max_right):
		sn_settings.snake_rect_x -= sn_settings.max_right
	if (sn_settings.snake_rect_y < 0):
		sn_settings.snake_rect_y += sn_settings.max_buttom
	if (sn_settings.snake_rect_y > sn_settings.max_buttom):
		sn_settings.snake_rect_y -= sn_settings.max_buttom
	
def increase_snake_size(screen, sn_settings, snake_list):
	"""function to increase snake length"""
	snake_Head = []
	snake_Head.append(sn_settings.snake_rect_x)
	snake_Head.append(sn_settings.snake_rect_y)
	snake_list.append(snake_Head)
	if len(snake_list) > sn_settings.Length_of_snake:
		del snake_list[0]

	

def snake_director(event, screen, sn_settings, snake_list):
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
	else:
		sn_settings.change_y = (1* sn_settings.snake_height)
		sn_settings.change_x = 0
def food_position_generator(sn_settings, food):
	#generates random postion of food on the screen
	sn_settings.food_x_position = round(random.randrange(0, sn_settings.screen_width-sn_settings.snake_height) / 10.0) * 10.0
	sn_settings.food_y_position = round(random.randrange(0, sn_settings.screen_height-sn_settings.snake_width) / 10.0) * 10.0
	#sn_settings.food_x_position = randint(1 ,sn_settings.screen_width-sn_settings.snake_height)
	#sn_settings.food_y_position = randint(1 ,sn_settings.screen_height-sn_settings.snake_width)
def checking_food_snake_collision(screen ,sn_settings,food,snake_list, Snake_1):
	#checks whether a snake has hit the food if there is a hit food_position_generator is called
	#collisions = pygame.sprite.groupcollide(food, snake, True, True)

	if sn_settings.food_x_position  == sn_settings.snake_rect_x or sn_settings.food_y_position == sn_settings.snake_rect_y:
	#if collisions==1:
		#calling food radom generator
		food_position_generator(sn_settings, food)
		sn_settings.Length_of_snake +=1