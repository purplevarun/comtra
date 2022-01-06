# import python modules
import pygame

# import local modules
from src.classes import *

# initialization
pygame.init()
screenWidth = 800
screenHeight = int(0.8 * screenWidth)
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Comtra")

player = Player(200, 200, 5)

# game loop
gameRunning = True
while gameRunning:
    # inf game loop

    screen.blit(player.img, player.rect)

    # actions
    for event in pygame.event.get():
        # close game
        if event.type == pygame.QUIT:
            gameRunning = False

    pygame.display.update()

pygame.quit()
