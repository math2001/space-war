import random
import pygame
import time
from pygame.locals import *

from couleur import *
from Ship import Ship
from Tower import Tower
from Life import Life
from Time import Time
from Game import run_menu
from Son import Son

pygame.init()

screen = pygame.display.set_mode((0, 0), FULLSCREEN)
# screen = pygame.display.set_mode((500, 500))
srect  = screen.get_rect()
pygame.display.set_caption('Space War - BETA')
pygame.display.set_icon(pygame.image.load('img/ship-1-mini.png').convert_alpha())

def rnd():
	return random.randint(0, srect.width), random.randint(0, srect.height)


cont = True
while cont:
	 # on attend 50ms pour ne pas qu'on relance le jeu direct
	game = True
	# on affiche le menu
	run_menu()
	pygame.display.flip()
	pygame.event.clear()
	# on nettoie les evenement
	start = False
	while not start:
		for ev in pygame.event.get():
			if ev.type == QUIT or (ev.type == KEYDOWN and ev.key == K_ESCAPE): 
				game = cont = False
				start = True
			elif ev.type == KEYDOWN:
				start = True

	ship = Ship()
	towers = []

	life = Life()
	son = Son()
	tmp = Time()
	son.play_music('ThunderZone.mp3')

	while game:
		if tmp.get_time() == 2:
			towers.append( Tower( rnd(), random.randint(1, 10) ))
			tmp.reset_time()
		screen.fill(white)
		for ev in pygame.event.get():
			if ev.type == QUIT or (ev.type == KEYDOWN and ev.key == K_ESCAPE): game = 0



		for tower in towers:
			tower.render()
			# tower.fire(ship.get_center())
			# on test si la ball du ship n'a pas touche une tower
			if tower.collision(ship.get_ball_rect()) and ship.ball.is_fired:
				towers.remove(tower) # on le retire de la liste - towerS.rem...
				ship.stop_ball()
				ship.add_score()
				if ship.is_rotating():
					ship.add_life(5)

			# on test si le ship n'a pas ete touche par un missile
			if ship.collision(tower.get_missile_rect()) and tower.missile.is_fire:
				tower.remove_missile()
				if not ship.explose():
					son.play("explosion")
					# pygame.time.wait(1000)
					son.stop_music(2000)
					game = 0


		ship.checker()
		ship.render()
		life.set_percentage(ship.get_life(), ship.get_max_life())
		life.set_center(ship.get_rect().midtop)
		life.render()

		pygame.display.flip()
pygame.quit()