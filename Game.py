import pygame
from pygame.locals import *
from couleur import *
from Screen import Screen
from Tools import Tools

pygame.init()



tools = Tools()


def run_menu(score):
	if score is None:
		score = "Pas de meilleur du score"
	score = str(score)
	screen = pygame.display.get_surface()
	srect  = screen.get_rect()

	font = pygame.font.Font('font/indie-flower.ttf', 50)

	text = [
		"Un touche pour jouer",
		"Ou ECHAP pour quitter",
		"Meilleur Score: " + score
	]
	for i in range(len(text)):
		text[i] = font.render(text[i], 1, gray)

	rect = tools.menu_text(srect, [txt.get_rect() for txt in text])
	screen.fill(h333)
	for i in range(len(text)):
		screen.blit(text[i], rect[i])