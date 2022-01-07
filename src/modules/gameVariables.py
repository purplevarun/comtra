import pygame

clock = pygame.time.Clock()
FPS = 60

moving_left = False
moving_right = False
moving_up = False
moving_down = False


def moving_horizontally():
    if moving_left or moving_right:
        return True
    return False


GRAVITY = 0.75
BG_COLOR = (144, 201, 100)
RED = (255, 0, 0)
