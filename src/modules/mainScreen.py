import pygame

pygame.init()
screenWidth = 800
screenHeight = int(0.8 * screenWidth)
pygame.display.set_caption("Comtra")
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # fullscreen mode
# screen = pygame.display.set_mode((screenWidth, screenHeight)) # windowed
