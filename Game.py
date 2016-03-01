import pygame
from pygame.locals import *
from couleur import *
from Screen import Screen

pygame.init()

def run_menu():
	screen = pygame.display.get_surface()
	srect  = screen.get_rect()

	font = pygame.font.Font('font/indie-flower.ttf', 50)

	text1 = font.render("Une touche pour jouer", 1, gray)
	text2 = font.render("Ou ECHAP pour quitter", 1, gray)

	rect1 = text1.get_rect(center=srect.center)
	rect2 = text2.get_rect(center=srect.center)

	rect1.bottom = rect2.top

	screen.fill((51, 51, 51))
	screen.blit(text1, rect1)
	screen.blit(text2, rect2)
