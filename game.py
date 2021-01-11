# -*- coding: utf-8 -*-
from var import *
import functions
import pygame
import time
pygame.init()
pygame.display.set_caption("Snake 🐍")
gameDisplay = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
pygame.display.set_icon(snakeIcon)
functions.startBackground()
pygame.display.update()
game = True
clock.tick(FPS)
functions.game_intro()