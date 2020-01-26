import sys
import pygame

def check_event(screen, sn_settings, snake):
	"""a function to check keyboard or mouse event"""
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				snake_director(event, screen, sn_settings, snake)


def update(screen, sn_settings, snake):
	"""a function to display screen object on screen"""
	screen.fill(sn_settings.bg_color)
	#snake_director(event, screen, sn_settings, snake)
	#setting snake demensions
	snake_demension = [sn_settings.snake_rect_x, sn_settings.snake_rect_y, sn_settings.snake_height, sn_settings.snake_width]
	#drawing snake
	snake.draw_snake(snake_demension)
	#pygame.draw.rect(screen,sn_settings.snake_color,[200,150,10,10])
	#show the most recently drawn screen visible 
	pygame.display.update()
	automate_snake_movement(sn_settings)

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

	
	
	


