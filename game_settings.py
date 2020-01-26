class Settings():
	"""class model to store game settings"""
	def __init__(self):
		#intializing static game settings
		#colors
		blue=(0,0,255)
		red=(255,0,0)
		#screen
		self.screen_width =1200
		self.screen_height=600
		self.bg_color=blue
		#snake
		self.snake_color=red
