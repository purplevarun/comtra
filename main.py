# import python modules
import pygame

# import local modules
import src.classes

# initialization
pygame.init()
screenWidth = 800
screenHeight = int(0.8 * screenWidth)
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Comtra")


# game loop
gameRunning = True
while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False
