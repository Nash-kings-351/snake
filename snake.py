import sys

import pygame

import time

from game_settings import Settings

from snake_class import Snake

from food_class import Food

import game_functions as Gf

from pygame.sprite import Group


def run_game():
	#initializing game
	pygame.init()

	sn_settings=Settings()
	#drawing screen
	screen = pygame.display.set_mode((sn_settings.screen_width,sn_settings.screen_height))
	#snake
	Snake_1 = Snake(screen, sn_settings)
	# Make a group to store snake segment in.
	snake_list = []
	#food
	food =Food(screen, sn_settings)
	#adding screen caption
	pygame.display.set_caption("kings snake game")

	clock = pygame.time.Clock()
	#start main loop for the game
	while True:
		#watch for keyboard / mouse input
		Gf.check_event(screen, sn_settings, Snake_1, food)
		#displaying screen objects
		#snake segment distance
		Snake_1.update(sn_settings)
		Gf.update(screen, sn_settings, snake_list, Snake_1 , food)
		clock.tick(sn_settings.snake_speed)

run_game()