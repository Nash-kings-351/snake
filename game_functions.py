import sys
import pygame

def check_event():
	"""a function to check keyboard or mouse event"""
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()


def update(screen, sn_settings, snake):
	"""a function to display screen object on screen"""
	screen.fill(sn_settings.bg_color)
	snake.draw_snake()
	#pygame.draw.rect(screen,sn_settings.snake_color,[200,150,10,10])
	#show the most recently drawn screen visible 
	pygame.display.update()