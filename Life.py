import pygame
from pygame.locals import *
from couleur import *
from Screen import Screen

pygame.init()

class Life(Screen):
	""" Cette class permet d afficher la vie restante """
	def __init__(self):
		Screen.__init__(self)
		self.image = pygame.Surface((60, 11))
		self.rect  = self.image.get_rect()

		self.color = pygame.Color(0, 0, 0)
		self.color_percent = [0, 0, 0]
		self.image.fill(blanc)

	def percent_to_color(self, percent_color):
		for i, percent in enumerate(percent_color):
			if percent_color[i] > 100:
				percent_color[i] = 100
			if percent_color[i] < 0:
				percent_color[i] = 0
			percent_color[i] = int(percent_color[i] * (float(255) / float(100)))
		return percent_color

	def set_percentage(self, current, maxi):
		self.percentage = float(float(current) / float(maxi)) * 100
		self.color_percent[2] = 0
		self.color_percent[1] = int(self.percentage)
		self.color_percent[0] = 100 - int(self.percentage)
		self.color = self.percent_to_color(self.color_percent)


	def set_center(self, center):
		self.rect.center = center
		self.rect.top -= 5

	def render(self):
		# contour
		pygame.draw.rect(self.screen, gray, self.rect, 1)
		# jauge
		pygame.draw.line(
			self.screen,
			self.color,
			(self.rect.left + 4, self.rect.top + 5),
			(self.rect.left + 4 + self.percentage / 2, self.rect.top + 5),
			5
		)