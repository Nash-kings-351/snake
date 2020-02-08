import pygame.font

from pygame.sprite import Group
class Scoreboard():
	"""A class to report scoring information."""
	def __init__(self, sn_settings, screen, game_stats):
		"""Initialize scorekeeping attributes."""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.sn_settings = sn_settings
		self.game_stats = game_stats

		# Font settings for scoring information.
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 30)

		# Prepare the initial score images.
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
	def prep_score(self):
		"""Turn the score into a rendered image."""
		rounded_score = int(round(self.game_stats.score, -1))
		score_str = "{:,}".format(rounded_score)
		#score_str = str(self.stats.score)
		self.score_image = self.font.render("score "+score_str, True, self.text_color, self.sn_settings.bg_color)
		# Display the score at the top right of the screen.
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 10
		self.score_rect.top = 0
	
	def prep_high_score(self):
		"""Turn the high score into a rendered image."""
		high_score = int(round(self.game_stats.high_score, -1))
		high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render("highest score "+high_score_str, True,
		self.text_color, self.sn_settings.bg_color)
		# Center the high score at the top of the screen.
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top
	def prep_level(self):
		"""Turn the level into a rendered image."""
		self.level_image = self.font.render("level "+str(self.game_stats.level), True,
		self.text_color, self.sn_settings.bg_color)
		# Position the level below the score.
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = 100
		self.level_rect.top = 0

	def show_score(self):
		"""Draw scores,highest score and level  to the screen."""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)