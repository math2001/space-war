# Vous 
TIME_TO_ADD_TOWER = 2




import random
import pygame
import time
from pygame.locals import *



from couleur import *
from Ship import Ship
from Tower import Tower
from Life import Life
from Time import Time
from Game import run_menu, run_mouse_menu, run_a_propos
from Son import Son
from Screenshot import Screenshot

pygame.init()

screen = pygame.display.set_mode((0, 0), FULLSCREEN)
pygame.time.wait(1000)
# screen = pygame.display.set_mode((500, 500))
srect  = screen.get_rect()
pygame.display.set_caption('Space War - BETA')
pygame.display.set_icon(pygame.image.load('img/ship-1-mini.png').convert_alpha())

def rnd():
	return random.randint(0, srect.width), random.randint(0, srect.height)

def game_over(ship):
	ship.save_score()

cont = True
son = Son()
screenshot = Screenshot()
while cont:
	pygame.mouse.set_visible(False)
	ship = Ship()
	towers = []

	life = Life()
	son.play_music('menu1.4.wav')

	text = run_mouse_menu(ship.get_best_score()).lower()

	game = False
	a_propos = False
	if "jouer" in text:
		game = True
	elif "quitter" in text:
		game = cont = False
	elif "propos" in text:
		a_propos = True


	son.stop_music(2000)
	son.play_music('ThunderZone.mp3')

	tmp = Time()


	# ------------------------------ #
	# ------------ Game ------------ #
	# ------------------------------ #
	while game:
		screen.fill(white)
		pygame.mouse.set_visible(False)

		# on ajoute des tour
		if tmp.get_time() == TIME_TO_ADD_TOWER:
			towers.append( Tower( rnd(), random.randint(1, 10) ))
			tmp.reset_time()

		for ev in pygame.event.get():
			if ev.type == QUIT or (ev.type == KEYDOWN and ev.key == K_ESCAPE): 
				son.stop_music(2000)
				game_over(ship)
				game = 0
			if ev.type == KEYDOWN and ev.unicode == "m":
				son.toogle_son()

		for tower in towers:
			tower.render()
			tower.fire(ship.get_center())
			# on test si la ball du ship n'a pas touche une tower
			if tower.collision(ship.get_ball_rect()) and ship.ball.is_fired:
				towers.remove(tower) # on le retire de la liste - towerS.rem...
				ship.stop_ball()
				ship.add_score()
				ship.add_life(int(tower.get_level() / 2))

			# on test si le ship n'a pas ete touche par un missile
			if ship.collision(tower.get_missile_rect()) and tower.missile.is_fire:
				tower.remove_missile()
				if not ship.explose():
					son.play("explosion")
					game_over(ship)
					son.stop_music(2000)
					game = 0


		ship.checker()
		ship.render()
		life.set_percentage(ship.get_life(), ship.get_max_life())
		life.set_center(ship.get_rect().midtop)
		life.render()

		pygame.display.flip()

		if pygame.key.get_pressed()[K_s]:
			screenshot.take()

	while a_propos:
		cont = True
		screen.fill(h333)

		if "coucou" == run_a_propos():
			a_propos = False

		pygame.display.flip()


pygame.quit()