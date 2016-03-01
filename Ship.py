import pygame
from pygame.locals import *

from couleur import *
from Screen import Screen
from Ball import Ball
from Son import Son
from Score import Score

pygame.init()

class Ship(Screen):
	def __init__(self, name_image="ship-1.png"):
		Screen.__init__(self)
		self.keys = {
			"up"          : [K_UP],
			"down"        : [K_DOWN],
			"left"        : [K_LEFT],
			"right"       : [K_RIGHT],
			"rotate_left" : [K_a, K_q],
			"rotate_right": [K_d],
			"fire"        : [K_SPACE],

			# test
			"lose_life": [K_l] # c'est un L
		}

		self.image = pygame.image.load('img/' + name_image).convert_alpha()
		self.rect  = self.image.get_rect()

		self.rect.center = self.srect.center
		self.ball = Ball(default_center=self.rect.center)

		self.vitesse = 2
		self.vitesse_rotate = 2

		self.orginal = self.image.copy()
		self.current_angle = 0

		self.cheated = 0

		self.max_life = 50
		self.life = self.max_life

		self.score = Score()

	def _test_index(self, liste, index):
		""" 
			Cette fonction test si UN des element selectionne par les index sont vrai
			ex:
			liste = [0, 1, 0, 0, 0, 1]
			index = [1, 5] # test l index 1 et 5
		"""
		ok = 0
		for i in index:
			if liste[i]:
				ok = self.cheated if 0 else 1
		return ok

	def _move(self, x, y):

		self.rect.move_ip((x, y))
		self.ball.follow(self.rect.center)

	def _spin(self, angle):
		prev_rect_center = self.rect.center
		image = pygame.transform.rotate(self.orginal, self.current_angle + angle)
		self.rect = image.get_rect(center=prev_rect_center)
		self.current_angle += angle
		self.image = image

	def checker(self):
		self.is_rotate = False
		keystate = pygame.key.get_pressed()
		# bouger
		if self._test_index(keystate, self.keys["left"]):
			if self.rect.left > self.srect.left:
				self._move(-self.vitesse, 0)
		if self._test_index(keystate, self.keys["right"]):
			if self.rect.right < self.srect.right:
				self._move(self.vitesse, 0)
		if self._test_index(keystate, self.keys["up"]):
			if self.rect.top > self.srect.top:
				self._move(0, -self.vitesse)
		if self._test_index(keystate, self.keys["down"]):
			if self.rect.bottom < self.srect.bottom:
				self._move(0, self.vitesse)

		# tourner
		if self._test_index(keystate, self.keys["rotate_left"]):
			self._spin(self.vitesse_rotate)
			self.is_rotate = True
		if self._test_index(keystate, self.keys["rotate_right"]):
			self._spin(-self.vitesse_rotate)
			self.is_rotate = True

		# tirer
		if self._test_index(keystate, self.keys["fire"]):
			self.ball.fire(self.current_angle)

		# test
		if self._test_index(keystate, self.keys["lose_life"]):
			self.life -= 1


	def render(self):
		# on se sert de cette fonction pour faire bouger la balle
		# car elle est appele a chaque fois
		self.ball.move(self.srect, self.rect.center)

		# on affiche d abord la balle
		params = self.ball.render()
		self.screen.blit(params[0], params[1])
		# PUIS le vaisseau
		self.screen.blit(self.image, self.rect)
		score, rect = self.score.render()
		rect.midtop = self.srect.midtop
		self.screen.blit(score, rect)
		# comme ca, le vaisseau est au dessus
	
	def get_center(self):
		return self.rect.center

	def get_rect(self):
		return self.rect

	def get_ball_rect(self):
		return self.ball.rect

	def collision(self, rect):
		return self.rect.colliderect(rect)

	def stop_ball(self):
		self.ball.rect.center = self.rect.center
		self.ball.speed = [0, 0]
		self.ball.is_fired = False

	def explose(self):
		self.life -= 1
		if self.life < 0:
			return 0
		else:
			return 1

	def get_max_life(self):
		return self.max_life

	def get_life(self):
		return self.life

	def add_score(self):
		self.score.add()

	def is_rotating(self):
		return self.is_rotate

	def full_life(self):
		self.life = self.max_life

	def add_life(self, nb):
		self.life += nb
		if self.life > self.max_life:
			self.life = self.max_life