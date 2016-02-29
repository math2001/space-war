import random
import pygame
from pygame.locals import *
from couleur import *
from Ship import Ship
from Tower import Tower
from Life import Life

pygame.init()

screen = pygame.display.set_mode((0, 0))
srect  = screen.get_rect()
pygame.display.set_caption('Space War - BETA')
pygame.display.set_icon(pygame.image.load('img/ship-1-mini.png').convert_alpha())

def rnd():
	return random.randint(0, srect.width), random.randint(0, srect.height)
ship = Ship()
towers = [
	Tower( rnd(), 5 ),
	Tower( rnd(), 8 )
]

life = Life()

cont = False
while cont:
	screen.fill(white)
	for ev in pygame.event.get():
		if ev.type == QUIT or (ev.type == KEYDOWN and ev.key == K_ESCAPE): cont = 0

	ship.checker()
	ship.render()

	for tower in towers:
		tower.render()
		tower.fire(ship.get_center())
		# on test si la ball du ship n'a pas touche une tower
		if tower.collision(ship.get_ball_rect()):
			towers.remove(tower)
			ship.stop_ball()

		if ship.collision(tower.get_missile_rect()):
			if not ship.explose():
				cont = 0

	pygame.display.flip()
pygame.quit()