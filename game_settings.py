class Settings():
	"""class model to store game settings"""
	def __init__(self):
		#intializing static game settings
		#colors
		self.blue = (0,0,255)
		self.red = (255,0,0)
		self.green=(0,255,0)
		#screen
		self.screen_width = 1200
		self.screen_height= 600
		self.bg_color = self.blue
		#maxmum right and bottom screen point minus one to avoid snake disapearing along the screen edge 
		self.max_right = self.screen_width - 10
		self.max_buttom = self.screen_height - 10
		#to set snake speed which is the rate which screen updates it self
		self.snake_speed = 40
		#self.dynamic_game_settings()
	def dynamic_game_settings(self):
		"""function to intialize dynamic game values"""
		#snake
		self.snake_color = self.red
		self.snake_rect_x = 600
		self.snake_rect_y = 300
		self.snake_width  = 10
		self.snake_height = 10
		#snake default moving up
		self.change_y = 0
		self.change_x =0
		#food configs
		self.food_length = 10
		self.food_color = self.green
		self.food_x_position = 600
		self.food_y_position = 300
		

