import sys

import pygame

import time

from game_settings import Settings

from snake_class import Snake

from food_class import Food

import game_functions as Gf

def run_game():
	#initializing game
	pygame.init()
	#creating an object so as to access variables values in class settings
	sn_settings=Settings()
	#drawing screen
	screen = pygame.display.set_mode((sn_settings.screen_width,sn_settings.screen_height))
	#creating an object snake so as to access variables values in class Snake
	snake = Snake(screen, sn_settings)
	#a list to store values of snake body to teck it movement
	snake_list = []
	##creating an object food so as to access variables values in class Food
	food =Food(screen, sn_settings)
	#adding screen caption
	pygame.display.set_caption("kings snake game")

	#to keep track of time while playing the game
	clock = pygame.time.Clock()

	#start main loop for the game
	while True:
		#watch for keyboard / mouse input
		Gf.check_event(screen, sn_settings, snake)
		#displaying screen objects
		#calling update in Snake class to automate snake movement
		snake.update(sn_settings)
		Gf.update(screen, sn_settings, snake_list, snake , food)
		#rate at which the screen is update
		clock.tick(sn_settings.snake_speed)

run_game()