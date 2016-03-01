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


	def play(self, son):
		self.sons[son].play()

	def play_music(self, name):
		pygame.mixer.music.load(os.path.join('son', name))
		pygame.mixer.music.play(-1)

	def stop_music(self, fadeout):
		pygame.mixer.music.fadeout(fadeout)
