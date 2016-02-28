import pygame
from pygame.locals import *
from couleur import *
from Screen import Screen
from Ball import Ball

pygame.init()

class Tower(Screen):
	def __init__(self):
		Screen.__init__(self)
		self.image    = pygame.image.load('img/tower.png').convert_alpha()
		self.rect     = self.image.get_rect()
		self.original = self.image.copy()

		self.current_angle = 0

		self.listBall = []
		for i in range(2):
			self.listBall.append(Ball())
			self.listBall[i].follow(self.rect.center)

	def _spin(self, angle):
		self.current_angle += angle
		prev_rect_center = self.rect.center
		self.image = pygame.transform.rotate(self.current_angle)
		self.rect  = self.image.get_rect(center=prev_rect_center)

	def fire(self, ship_pos):
		for ball in self.listBall:
			if not ball.is_fire():
				ball.fire_to(ship_pos)