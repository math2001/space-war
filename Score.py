import pygame
import os
from pygame.locals import *
from couleur import *

pygame.init()

class Score:
	def __init__(self, font='d', size=50):
		if font == 'd':
			self.font = pygame.font.Font('font/indie-flower.ttf', size)
		else:
			self.font = pygame.font.Font(os.join.path('font', font), size)
		self.score = 0

	def add(self):
		self.score += 1

	def render(self):
		text = self.font.render('Score :' + str(self.score), 1, gray, pygame.Color(255, 255, 255, 255))
		rect = text.get_rect()
		return text, rect
