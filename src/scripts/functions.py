import pygame
from src.scripts.Global import *


def draw_bg():
    screen.fill(BG_COLOR)
    pygame.draw.line(screen, RED, (0, FLOOR), (screenWidth, FLOOR))


def draw(*x):
    for i in x:
        screen.blit(i.img, i.rect)
