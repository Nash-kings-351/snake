import sys

import pygame

import time

from game_settings import Settings

from snake_class import Snake

from food_class import Food

import game_functions as Gf

from button import Button

from game_stats import GameStats

from scoreboard import Scoreboard

def run_game():
	#initializing game
	pygame.init()
	#creating an object so as to access variables values in class settings
	sn_settings=Settings()
	#drawing screen
	screen = pygame.display.set_mode((sn_settings.screen_width,sn_settings.screen_height))
	#creating an object snake so as to access variables values in class Snake
	snake = Snake(screen, sn_settings)
	#a list to store values of snake body to track it's movement
	snake_list = []
	##creating an object food so as to access variables values in class Food
	food =Food(screen, sn_settings)
	#adding screen caption
	pygame.display.set_caption("kings snake game")

	#to keep track of time while playing the game
	clock = pygame.time.Clock()
	# Make the Play button.
	play_button = Button(sn_settings, screen, "Play")
	#game statistics
	game_stats = GameStats(sn_settings)
	#game scores
	sb = Scoreboard(sn_settings, screen, game_stats)

	while True:
		#start main loop for the game
		if game_stats.game_active == True :
			#calling update in Snake class to automate snake movement
			snake.update(sn_settings)
		#watch for keyboard / mouse input
		Gf.check_event(screen, sn_settings, snake, game_stats,snake_list, play_button, sb)
		#displaying screen objects
		
		Gf.update(screen, sn_settings, snake_list, snake , food, play_button, game_stats, sb)
			#rate at which the screen is update
		clock.tick(sn_settings.snake_speed)

run_game()