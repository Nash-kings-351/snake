class Settings():
	"""class model to store game settings"""
	def __init__(self):
		#intializing static game settings
		#colors
		blue = (0,0,255)
		red = (255,0,0)
		green=(0,255,0)
		#screen
		self.screen_width = 1200
		self.screen_height= 600
		self.bg_color = blue
		#maxmum right and bottom screen point 
		self.max_right = self.screen_width
		self.max_buttom = self.screen_height
		#snake
		self.snake_color = red
		self.snake_speed =1
		self.snake_rect_x = 600
		self.snake_rect_y = 300
		self.snake_width  = 15
		self.snake_height = 15
		#snake default moving up
		self.change_y = (-1* self.snake_speed)
		self.change_x =0

		#food configs
		self.food_radius = 10
		self.food_color = green
		self.food_x_position = 600
		self.food_y_position = 300

