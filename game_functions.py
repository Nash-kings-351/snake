import sys

import pygame

import random

from pygame.sprite import Sprite

from snake_class import Snake

def check_event(screen, sn_settings, snake, game_stats, snake_list, play_button, sb):
	"""a function to check keyboard or mouse event"""

	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(sn_settings, screen, game_stats, snake_list, play_button, sb, mouse_x, mouse_y)
		if event.type == pygame.QUIT:
			Quit_game(sn_settings, game_stats)
		if event.type == pygame.KEYDOWN:
			snake_director(event, sn_settings, game_stats)


def update(screen, sn_settings, snake_list, snake, food, play_button, game_stats, sb):
	"""a function to display screen object on screen"""
	

	screen.fill(sn_settings.bg_color)
	#draw play button when game is inactive
	if game_stats.game_active == False :
		play_button.draw_button()
	elif game_stats.game_active == True:
		#drawing food randomly
		food.draw_food(sn_settings.food_x_position, sn_settings.food_y_position)
		
		#increasing snake length every time screen update
		increase_snake_size(sn_settings,snake_list, game_stats)
		
		# Redraw snake .
		snake.draw_snake(sn_settings,snake_list)
		#displaying score on screen
		sb.show_score()
		#checking for collision
		checking_food_snake_collision(sn_settings,food, snake_list, game_stats, sb)
	
	#show the most recently drawn screen visible 
	pygame.display.update()
	
	

def increase_snake_size(sn_settings, snake_list, game_stats):
	"""function to increase snake length"""
	snake_Head = []
	snake_Head.append(sn_settings.snake_rect_x)
	snake_Head.append(sn_settings.snake_rect_y)
	snake_list.append(snake_Head)
	#Deletes the added segment if snake is longer than the length it should be at that point
	if len(snake_list) > game_stats.Length_of_snake:
		del snake_list[0]

	

def snake_director(event, sn_settings, game_stats):
	"""function to change direction of the snake to aim fo food"""
	if event.key == pygame.K_DOWN and sn_settings.change_y >= 0:
		sn_settings.change_y = (1 * sn_settings.snake_height)
		sn_settings.change_x = 0
	elif event.key == pygame.K_LEFT and sn_settings.change_x <= 0:
		sn_settings.change_y = 0
		sn_settings.change_x = (-1 * sn_settings.snake_height)
	elif event.key == pygame.K_UP and sn_settings.change_y <= 0:
		sn_settings.change_y = (-1 * sn_settings.snake_height)
		sn_settings.change_x = 0
	elif event.key == pygame.K_RIGHT and sn_settings.change_x >= 0:
		sn_settings.change_y = 0
		sn_settings.change_x = (1 * sn_settings.snake_height)
	elif (event.key == pygame.K_DOWN and sn_settings.change_y < 0) or (event.key == pygame.K_LEFT and sn_settings.change_x > 0) or (event.key == pygame.K_UP and sn_settings.change_y > 0) or (event.key == pygame.K_RIGHT and sn_settings.change_x < 0) :
		# UnHide the mouse cursor.
		pygame.mouse.set_visible(True)
		game_stats.game_active = False
def food_position_generator(sn_settings, food):
	"""generates random postion of food on the screen"""
	# there is need to revisit and know this random and randint functions
	sn_settings.food_x_position = round(random.randrange(0, sn_settings.screen_width-sn_settings.snake_height) / 10.0) * 10.0
	sn_settings.food_y_position = round(random.randrange(30, sn_settings.screen_height-sn_settings.snake_width) / 10.0) * 10.0

def checking_food_snake_collision(sn_settings, food, snake_list, game_stats, sb):
   if (sn_settings.food_x_position  == sn_settings.snake_rect_x) and (sn_settings.food_y_position == sn_settings.snake_rect_y):
	   #calling food radom generator
	   food_position_generator(sn_settings, food)
	   #checking for high score
	   check_high_score(game_stats, sb)
	   #display intance score
	   sb.prep_score()
	   sb.prep_level()
	   #incrementing snake length once a snake eat food
	   game_stats.Length_of_snake += 1
	   game_stats.score += 10
	   game_stats.level = int(game_stats.score /10 + 1)
	   sn_settings.snake_speed *= game_stats.level * 0.2
	   game_stats.write_high_score(game_stats.high_score)
def check_play_button(sn_settings, screen, game_stats, snake_list, play_button, sb, mouse_x, mouse_y):
	"""Start a new game when the player clicks Play."""
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not game_stats.game_active:
		# Reset the game settings.
		sn_settings.dynamic_game_settings()
		# Hide the mouse cursor.
		pygame.mouse.set_visible(False)
		#Deleting the previous snake
		del snake_list[0:game_stats.Length_of_snake]
		# Reset the game statistics.

		sn_settings.change_y = (-1 * sn_settings.snake_height)
		sn_settings.change_x = 0


		game_stats.reset_stats()
		game_stats.game_active = True

		# Reset the scoreboard images.
		sb.prep_score()
		sb.prep_high_score()
		sb.prep_level()

def Quit_game(sn_settings, game_stats):
	"""function to quit the game"""
	game_stats.write_high_score(game_stats.high_score)
	sys.exit()
def check_high_score(game_stats, sb):
	"""Check to see if there's a new high score."""
	if game_stats.score > game_stats.high_score:
		game_stats.high_score = game_stats.score
		sb.prep_high_score()