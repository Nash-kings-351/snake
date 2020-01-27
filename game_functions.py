import sys

import pygame

from random import randint

def check_event(screen, sn_settings, snake,food):
	"""a function to check keyboard or mouse event"""
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				snake_director(event, screen, sn_settings, snake)


def update(screen, sn_settings, snake, food):
	"""a function to display screen object on screen"""
	screen.fill(sn_settings.bg_color)
	#snake_director(event, screen, sn_settings, snake)
	#setting snake demensions
	snake_demension = [sn_settings.snake_rect_x, sn_settings.snake_rect_y, sn_settings.snake_height, sn_settings.snake_width]
	#drawing snake
	snake.draw_snake(snake_demension)
	#drawing food randomly
	food.draw_food(sn_settings.food_x_position, sn_settings.food_y_position)

	
	#pygame.draw.rect(screen,sn_settings.snake_color,[200,150,10,10])
	#show the most recently drawn screen visible 
	pygame.display.update()
	automate_snake_movement(sn_settings)
	checking_food_snake_collision(sn_settings,food)

def automate_snake_movement(sn_settings):

	#bug to fix later 
	if (sn_settings.snake_rect_x < 0):
		sn_settings.snake_rect_x = sn_settings.max_right
	if (sn_settings.snake_rect_x > sn_settings.max_right):
		sn_settings.snake_rect_x = 0
	if (sn_settings.snake_rect_y < 0):
		sn_settings.snake_rect_y = sn_settings.max_buttom
	if (sn_settings.snake_rect_y > sn_settings.max_buttom):
		sn_settings.snake_rect_y = 0
	#change left or right 
	sn_settings.snake_rect_x += sn_settings.change_x
	#change down or up
	sn_settings.snake_rect_y += sn_settings.change_y	

def snake_director(event, screen, sn_settings, snake):
	"""function to change direction of the snake to aim fo food"""
	if event.key == pygame.K_DOWN:
		sn_settings.change_y = (1* sn_settings.snake_speed)
		sn_settings.change_x = 0
	elif event.key == pygame.K_LEFT:
		sn_settings.change_y = 0
		sn_settings.change_x = (-1 * sn_settings.snake_speed)
	elif event.key == pygame.K_UP:
		sn_settings.change_y = (-1 * sn_settings.snake_speed)
		sn_settings.change_x = 0
	elif event.key == pygame.K_RIGHT:
		sn_settings.change_y = 0
		sn_settings.change_x = (1 * sn_settings.snake_speed)
def food_position_generator(sn_settings, food):
	#generates random postion of food on the screen
	sn_settings.food_x_position = randint(0 ,sn_settings.screen_width)
	sn_settings.food_y_position = randint(0 ,sn_settings.screen_height)
def checking_food_snake_collision(sn_settings,food):
	#checks whether a snake has hit the food if there is a hit food_position_generator is called
	if sn_settings.snake_rect_x == sn_settings.food_x_position and sn_settings.snake_rect_y == sn_settings.food_y_position:
		#calling food radom generator
		food_position_generator(sn_settings, food)



	



	
	
	


