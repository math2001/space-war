import pygame
import os
import pickle
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
		self.path = "data/score.txt"

	def add(self):
		self.score += 1

	def save_best_score(self):
		if os.path.isfile(self.path):
			with open(self.path, 'r') as f:
				content = pickle.Unpickler(f).load()
			current_best_score = int(content)
			if self.score > current_best_score:
				with open(self.path, 'w') as f:
					pickle.Pickler(f).dump(self.score)
		else:
			with open(self.path, 'w') as f:
				pickle.Pickler(f).dump(self.score)

	def get_best_score(self):
		try:
			with open(self.path, "r") as f:
				content = pickle.Unpickler(f).load()
		except IOError:
			content = None
		return content

	def get_score(self):
		return self.score

	def render(self):
		text = self.font.render('Score :' + str(self.score), 1, gray)
		rect = text.get_rect()
		return text, rect
