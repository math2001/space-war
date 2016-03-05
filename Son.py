import pygame
import os
from pygame.locals import *
from couleur import *

pygame.init()

class Son:
	def __init__(self):
		self.sons = {
			"explosion": pygame.mixer.Sound('son/explosion.wav'),
			"tire"     : pygame.mixer.Sound('son/tire.ogg')
		}
		self.son_active = False

	def toogle_son(self):
		self.son_active = not self.son_active
		if not self.son_active:
			pygame.mixer.music.stop()
		else:
			pygame.mixer.music.play(-1)

	def play(self, son):
		if self.son_active:
			self.sons[son].play()

	def play_music(self, name):
		pygame.mixer.music.load(os.path.join('son', name))
		if self.son_active:
			pygame.mixer.music.play(-1)



	def stop_music(self, fadeout=2000):
		pygame.mixer.music.fadeout(fadeout) 
