import pygame
from pygame.locals import *
from couleur import *
from Screen import Screen
import math

pygame.init()

class Missile(Screen):
	def __init__(self, center=(0, 0), vitesse=10):
		Screen.__init__(self)
		self.image = pygame.image.load('img/bullet-1.png').convert_alpha()
		self.rect  = self.image.get_rect(center=center)

		self.speed = [0, 0]
		self.vitesse = vitesse

		self.is_fire = False

	def move(self, tower_rect):
		self.rect.move_ip(self.speed)
		if self._is_out():
			self.is_fire = False
			self.rect.center = tower_rect.center

	def _calculeSpeed(self, xtower, ytower, xcible, ycible):

		x = float(xcible - xtower)
		y = float(ycible - ytower)

		angle = math.degrees(math.atan2( x, y ) )


		cos = math.cos(math.radians(angle))
		sin = math.sin(math.radians(angle))	
		y = math.floor(cos * self.vitesse)
		x = math.floor(sin * self.vitesse)
		return ((x, y), angle)

	def _is_out(self):
		return not self.srect.colliderect(self.rect)

	def fire(self, xtower, ytower, xcible, yxible):
		if not self.is_fire:
			self.speed, angle = self._calculeSpeed(xtower, ytower, xcible, yxible)
			self.is_fire = True
			return angle

	def render(self):
		return self.image, self.rect