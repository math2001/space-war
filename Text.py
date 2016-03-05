import pygame
from pygame.locals import *
from couleur import *
from Screen import Screen

pygame.init()

class Text(Screen):
	def __init__(self):
		Screen.__init__(self)
		self.text = "Texte default"
		self.color = (0, 0, 0)
		self.aa = True
		self.font = pygame.font.Font("font/indie-flower.ttf", 75)
		self.surf = self.font.render(self.text, self.aa, self.color)
		self.rect = self.surf.get_rect()

	def _reload(self):
		self.surf = self.font.render(self.text, self.aa, self.color)

	def set_aa(self, aa):
		self.aa = aa
		self._reload()

	def set_text(self, text):
		self.text = text
		self._reload()

	def set_color(self, color):
		self.color = color
		# self.surf = self.font.render(self.text, self.aa, self.color)
		self._reload()

	def set_rect(self, rect):
		self.rect = rect

	def check_mouse(self, pos):
		return self.rect.collidepoint(pos)

	def render(self):
		self.screen.blit(self.surf, self.rect)