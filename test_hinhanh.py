import pygame
import os
import random
from pygame.locals import *
# <-- Avatar --> #



pygame.init()
DISPLAY= pygame.display.set_mode((600,300))
DISPLAY.fill((255,255,255))
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
	DISPLAY.blit(Avatar[random.randint(0,7)],(0,0))
	pygame.display.flip()