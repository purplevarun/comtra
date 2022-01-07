# import python modules
import pygame

# import local modules
from src.modules.player import *
from src.modules.userDefinedFunctions import *
from src.modules.gameVariables import *
from src.modules.mainScreen import *

# initialization


player = Player("player", 200, 400, 5)
player2 = Player("player", 400, 400, 4)

# game loop
gameRunning = True
while gameRunning:  # inf game loop

    # background reset
    draw_bg()

    # fps
    clock.tick(FPS)

    if player.Alive:
        # update actions (idle, running.. etc)
        if moving_left or moving_right:
            player.update_action(1)  # 1 - running
        else:
            player.update_action(0)  # 0 - idle

    # update frames
    player.update_animation()

    # load sprite
    player.draw()
    # player2.draw()

    # move sprite
    player.move(moving_left, moving_right, moving_up, moving_down)
    # player2.move(moving_left, moving_right, moving_up, moving_down)

    # actions
    for event in pygame.event.get():
        # close game
        if event.type == pygame.QUIT:
            gameRunning = False

        # key presses
        if event.type == pygame.KEYDOWN:
            key = event.key
            status = True

            # exit game
            if key == pygame.K_ESCAPE:
                gameRunning = False
            # move left
            if key == pygame.K_a or key == pygame.K_LEFT:
                moving_left = status
            # move right
            if key == pygame.K_d or key == pygame.K_RIGHT:
                moving_right = status
            # move up
            if (key == pygame.K_w or key == pygame.K_SPACE or key == pygame.K_UP) and player.Alive:
                player.jump = True

        if event.type == pygame.KEYUP:
            key = event.key
            status = False
            # move left
            if key == pygame.K_a or key == pygame.K_LEFT:
                moving_left = status
            # move right
            if key == pygame.K_d or key == pygame.K_RIGHT:
                moving_right = status
            # move up
            if key == pygame.K_s or key == pygame.K_DOWN:
                moving_up = status

    pygame.display.update()

pygame.quit()
