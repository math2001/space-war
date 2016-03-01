import pygame
from pygame.locals import *
from couleur import *
from Screen import Screen
from Missile import Missile

pygame.init()

class Tower(Screen):
	def __init__(self, center=(0, 0), vitesse=10):
		Screen.__init__(self)
		self.image    = pygame.image.load('img/tower.png').convert_alpha()
		self.rect     = self.image.get_rect()
		self.original = self.image.copy()

		self.rect.center = center

		self.current_angle = 0

		self.missile = Missile(self.rect.center, vitesse)

	def _spin(self, angle):
		self.current_angle += angle
		prev_rect_center = self.rect.center
		self.image = pygame.transform.rotate(self.current_angle)
		self.rect  = self.image.get_rect(center=prev_rect_center)

	def fire(self, ship_pos):
		self.missile.fire(self.rect.x, self.rect.y, ship_pos[0], ship_pos[1])

	def get_pos(self):
		return self.rect.x, self.rect.y

	def get_center(self):
		return self.rect.center

	def get_rect(self):
		return self.rect

	def render(self):
		self.missile.move(self.rect)
		image, rect = self.missile.render()
		self.screen.blit(image, rect)
		self.screen.blit(self.image, self.rect)

	def collision(self, rect):
		return self.rect.colliderect(rect)

	def get_missile_rect(self):
		return self.missile.rect

	def remove_missile(self):
		self.missile.rect.center = self.rect.center