import pygame
from scripts.Global import *


def draw_bg():
    screen.fill(BG_COLOR)
    pygame.draw.line(screen, RED, (0, FLOOR), (screenWidth, FLOOR))


def draw(*x):
    for i in x:
        screen.blit(i.img, i.rect)


font = pygame.font.SysFont("JetBrainsMono", 30)


def draw_text(text, font, col, x, y):
    img = font.render(text, True, col)
    screen.blit(img, (x, y))
