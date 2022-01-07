import pygame
from src.modules.gameVariables import *
from src.modules.mainScreen import *
# user defined functions


def draw_bg():
    screen.fill(BG_COLOR)
    pygame.draw.line(screen, RED, (0, 600), (screenWidth, 600))


def draw(*x):
    for i in x:
        screen.blit(i.img, i.rect)
