import pygame
from pygame.locals import *
from couleur import *
from Screen import Screen

pygame.init()

class Life(Screen):
	""" Cette class permet d afficher la vie restante """
	def __init__(self):
		Screen.__init__(self)
		self.image = pygame.Surface((110, 255))
		self.rect  = self.image.get_rect()

		self.image.fill(blanc)

	def set_percentage(self, current, maxi):
		self.percentage = float(float(current) / float(maxi)) * 100
		print(self.percentage)

	def set_center(self, center):
		self.rect.center = center

	def render(self):
		pygame.draw.rect(self.screen, gray, self.rect, 5)
		pygame.draw.line(
			self.screen,
			self.color,
			self.rect.left + 5,
			self.rect.left + 5 + self.percentage,
			10
		)