import pygame
from pygame.locals import *
import math # je ne pensais pas que ca m arriverai... :D
from couleur import *

pygame.init()

class Ball:
	
	"""Cette classe n'est pas appeler depuis le main, mais depuis la class Ship """

	def __init__(self, default_center=(0, 0), image_name="ball-1.png"):
		self.image = pygame.image.load('img/' + image_name).convert_alpha()
		self.rect  = self.image.get_rect(center=default_center)

		self.speed = [0, 0]
		self.vitesse = 8
		self.is_fired = 0

	def _is_out(self, screen_rect, center_ship):
		if not self.rect.colliderect(screen_rect):
			self.speed = [0, 0]
			self.rect.center = center_ship
			self.is_fired = 0

	def follow(self, pos):
		if self.speed[0] + self.speed[1] == 0: # la balle n est pas tire
			self.rect.center = pos

	def is_fire(self):
		return self.is_fired

	def fire(self, angle):
		""" 
			Cette methode est utilise par la class `Ship`, 
			car elle ne connait que son angle, et pas sa destination
			`angle` est en degres 
			cos -> y
			sin -> x
		"""
		if not self.is_fired:
			cos = math.cos(math.radians(angle))
			sin = math.sin(math.radians(angle))	
			y = math.floor(cos * self.vitesse)
			x = math.floor(sin * self.vitesse)

			self.speed = [-x, -y]
			self.is_fired = 1

	def fire_to_del(self, destination):
		""" `destination` est un tuple : (x, y) """
		if not self.is_fired:
			# calcule des x a rajouter en fonction de la vitesse
			x_rajouter = self.rect.x - destination[0]
			self.speed = [x_rajouter, 0]


	def move(self, screen_rect, center_ship):
		self.rect.move_ip(self.speed)
		self._is_out(screen_rect, center_ship)


	def render(self):
		return self.image, self.rect

