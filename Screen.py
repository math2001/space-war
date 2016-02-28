import pygame
from pygame.locals import *
from couleur import *

pygame.init()

class Screen:
	def __init__(self):
		self.screen = pygame.display.get_surface()
		self.sSize  = self.screen.get_size()
		self.srect  = self.screen.get_rect()