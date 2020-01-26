import sys

import pygame

from game_settings import Settings

from snake_class import Snake

import game_functions as Gf

def run_game():
	#initializing game
	pygame.init()

	sn_settings=Settings()
	#drawing screen
	screen = pygame.display.set_mode((sn_settings.screen_width,sn_settings.screen_height))
	#snake
	snake =Snake(screen, sn_settings)
	#adding screen caption
	pygame.display.set_caption("kings snake game")
	#start main loop for the game
	while True:
		#watch for keyboard / mouse input
		Gf.check_event()
		#displaying screen objects
		Gf.update(screen, sn_settings, snake)



run_game()