import pygame
from pygame.locals import *
from couleur import *
from Screen import Screen
from Ship import Ship

pygame.init()

screen = pygame.display.set_mode((0, 0), FULLSCREEN)
pygame.display.set_caption('Space War - ALPHA')
pygame.display.set_icon(pygame.image.load('img/ship-1-mini.png').convert_alpha())

listShip = [Ship()]

cont = 1
while cont:
	screen.fill(white)
	for ev in pygame.event.get():
		if ev.type == QUIT or (ev.type == KEYDOWN and ev.key == K_ESCAPE): cont = 0

	for ship in listShip:
		ship.checker()
		ship.render()

	pygame.display.flip()
pygame.quit()