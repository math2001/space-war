# -*- encoding: utf-8 -*-
import re
import os
import pygame
from pygame.locals import *
from couleur import *
from Screen import Screen
from Tools import Tools

from Text import Text


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
		"Meilleur Score: " + score,
	]
	for i in range(len(text)):
		text[i] = font.render(text[i], 1, gray)

	rect = tools.menu_text(srect, [txt.get_rect() for txt in text])
	screen.fill(h333)
	for i in range(len(text)):
		screen.blit(text[i], rect[i])

def run_mouse_menu(score):
	cursor = pygame.image.load('img/cursor.png').convert_alpha()

	if score is None:
		score = "Pas de meilleur score"
	score = str(score)
	screen = pygame.display.get_surface()
	srect  = screen.get_rect()

	font = pygame.font.Font('font/indie-flower.ttf', 75)


	text = [
		"Jouer !",
		"Quitter",
		"Meilleur score: " + score,
		"A propos"
	]
	
	for i in range(len(text)):
		t = text[i]
		text[i] = Text()
		text[i].set_text(t)
		text[i].set_color(gray)
		text[i].set_rect(text[i].surf.get_rect())


	rect = tools.menu_text(srect, [txt.rect for txt in text])
	for i in range(len(rect)):
		text[i].set_rect(rect[i])

	cont = False
	pos_cursor = pygame.mouse.get_pos()
	while not cont:
		for ev in pygame.event.get():
			if ev.type == MOUSEMOTION:
				pos_cursor = ev.pos
				for txt in text:
					if txt.check_mouse(ev.pos):
						txt.set_color(white)
					else:
						txt.set_color(grey)
			if ev.type == MOUSEBUTTONDOWN:
				for txt in text:
					if txt.check_mouse(ev.pos):
						return txt.text

		screen.fill(h333)
		for i in range(len(text)):
			text[i].render()
		screen.blit(cursor, pos_cursor)
		pygame.display.flip()

def run_a_propos():
	screen = pygame.display.get_surface()
	srect  = screen.get_rect()
	font   = pygame.font.Font('font/indie-flower.ttf', 30)

	titre = "A propos de Space War"
	texte = "Hi,/r/rCe jeu a ete devellope en Python, avec la bibliotheque Pygame./r Je voulais au debut faire un *player VS player* avec du reseau, mais vu la galere que ca a ete, j'ai un peu abandonne :(/rJe ne savais donc plus comment continuer mon jeu. Et puis j'ai eu l'idee des tours. Donc ce n'etait plus un combat entre joueur, mais un jeux contre l'ordi !/r/r/r/r<center>En construction..."
	texte = re.sub(r'(([a-zA-Z]+[ ,\.] *){10})', r'\1/r' , texte)
	texte_split = re.split('/r', texte)
	top = 100
	for ligne in texte_split:
		if "<center>" in ligne:
			center = True
		else:
			center = False
		ligne = font.render(ligne, True, white)

		rect = ligne.get_rect(x=50, top=top) if not center else ligne.get_rect(center=srect.center)
		top += rect.height
		screen.blit(ligne, rect)

	for e in pygame.event.get():
		if e.type == MOUSEBUTTONDOWN:
			return "coucou"
