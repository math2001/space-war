import pygame
from pygame.locals import *
from couleur import *

pygame.init()

class Tools1:
	def add_element_of_list(self, liste):
		res = 0
		for el in liste:
			res += el
		return res

	def add_rect(self, *rects):
		width = max([rect.width for rect in rects])

		height = 0
		height = [rect.height for rect in rects]

		return pygame.Rect(0, 0, width, self.add_element_of_list(height))

	def add_surf(self, *surf):
		""" Cette fonction ajoute les surf a la suite des autres, en 1 colone """

		width = max([rect.width for rect in rects])

		height = [rect.height for rect in rects]
		height = self.add_element_of_list(height)
		big_surf = pygame.Surface(width, height)

		return pygame.Rect(0, 0, width)


class Tools:
	def add_element_of_list(self, liste):
		res = 0
		for el in liste:
			res += el
		return res

	def is_pair(self, nb):
		return nb % 2 == 0

	def menu_text(self, srect, *rect):
		if type(rect[0]) == list:
			rect = rect[0]
		moitie = len(rect) / 2
		rect_middle = rect[moitie]
		rect_middle.center = srect.center
		for i in range(len(rect)):
			if i > moitie:
				rect[i].midtop = rect[i-1].midbottom
		for i in reversed(range(len(rect) / 2)):
			rect[i].midbottom = rect[i+1].midtop
		return rect


if __name__ == '__main__Modif':
	screen = pygame.display.set_mode((500, 500))
	font = pygame.font.Font("font/consolas.ttf", 50)
	text = [
		font.render("Lol 1", 1, white),
		font.render("Lol 2", 1, white),
		font.render("Lol 3", 1, white),
		font.render("Lol 4", 1, white),
		font.render("Lol 5", 1, white),
		font.render("Lol 6", 1, white),
		font.render("Lol 7", 1, white),
		font.render("Lol 8", 1, white),
	]
	t = Tools()
	rect = t.menu_text([txt.get_rect() for txt in text])
	for i in range(len(text)):
		screen.blit(
			text[i], 
			rect[i]
		)
	cont = True
	while cont:
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == KEYDOWN: cont = False