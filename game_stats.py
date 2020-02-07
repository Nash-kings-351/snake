class GameStats():
	"""Track statistics for Alien Invasion."""
	def __init__(self, sn_settings):
		"""Initialize statistics."""
		self.sn_settings = sn_settings
		self.reset_stats()
		# High score should never be reset.
		#self.high_score = 0
		# Start snake Invasion in an inactive state.
		self.game_active = False
		self.file_name="high_score.txt"
		self.get_high_score()
	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.score = 0
		#self.level = 1
	def get_high_score(self):
		with open(self.file_name,'r+') as file_object:
			self.high_score=0
			for line in file_object:
				self.high_score=int(line.strip())

	def write_high_score(self,high):

		with open(self.file_name,'w') as file_object1:
			file_object1.write(str(high))

