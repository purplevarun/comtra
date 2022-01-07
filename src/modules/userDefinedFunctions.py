import pygame
from src.modules.gameVariables import *
from src.modules.mainScreen import *
# user defined functions

FLOOR = 700


def draw_bg():
    screen.fill(BG_COLOR)
    pygame.draw.line(screen, RED, (0, FLOOR), (screenWidth, FLOOR))


def draw(*x):
    for i in x:
        screen.blit(i.img, i.rect)
