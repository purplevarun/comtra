# import python modules
import pygame

# import local modules
from src.classes import *

# user defined functions


def draw(*x):
    for i in x:
        screen.blit(i.img, i.rect)


# initialization

pygame.init()
screenWidth = 800
screenHeight = int(0.8 * screenWidth)
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Comtra")

moving_left = False
moving_right = False
moving_up = False
moving_down = False

clock = pygame.time.Clock()
FPS = 60

player = Player(200, 200, 5)
player2 = Player(400, 400, 4)

# game loop
gameRunning = True
while gameRunning:
    # inf game loop

    # fps
    clock.tick(FPS)

    # load sprite
    draw(player)

    # move sprite
    player.move(moving_left, moving_right, moving_up, moving_down)

    # actions
    for event in pygame.event.get():
        # close game
        if event.type == pygame.QUIT:
            gameRunning = False

        # key presses
        if event.type == pygame.KEYDOWN:
            key = event.key
            status = True
            # move left
            if key == pygame.K_a or key == pygame.K_LEFT:
                moving_left = status
            # move up
            if key == pygame.K_s or key == pygame.K_DOWN:
                moving_up = status
            # move right
            if key == pygame.K_d or key == pygame.K_RIGHT:
                moving_right = status
            # move down
            if key == pygame.K_w or key == pygame.K_UP:
                moving_down = status

        if event.type == pygame.KEYUP:
            key = event.key
            status = False
            # move left
            if key == pygame.K_a or key == pygame.K_LEFT:
                moving_left = status
            # move up
            if key == pygame.K_s or key == pygame.K_DOWN:
                moving_up = status
            # move right
            if key == pygame.K_d or key == pygame.K_RIGHT:
                moving_right = status
            # move down
            if key == pygame.K_w or key == pygame.K_UP:
                moving_down = status

    pygame.display.update()

pygame.quit()
