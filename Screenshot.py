import pygame
import time
import os
import pickle
from pygame.locals import *
from couleur import *
from Screen import Screen


pygame.init()

class Screenshot(Screen):
	def __init__(self):
		Screen.__init__(self)
		self.file = os.path.join('data', 'nb_screenshot.txt')

	def _generate_name(self):
		date = time.localtime()
		if os.path.isfile(self.file):
			with open(self.file, 'r') as f:
				content = pickle.Unpickler(f).load()
			return "screenshot-" + str(content)
		else:
			with open(self.file, 'w') as f:
				pickle.Pickler(f).dump("1")
			return "screenshot-1"

	def _increment(self):
		if os.path.isfile(self.file):
			with open(self.file, "r") as f:
				nb_screenshot = int(pickle.Unpickler(f).load())
			with open(self.file, 'w') as f:
				pickle.Pickler(f).dump(nb_screenshot + 1)

	def take(self):

		pygame.image.save(
			self.screen,
			"screenshot" + os.sep + self._generate_name() + ".png"
		)
		self._increment()
