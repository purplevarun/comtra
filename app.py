import pygame
from src.scripts.Global import *
from src.scripts.functions import *
from src.scripts.main import *

gameRunning = True
while gameRunning:  # inf game loop

    # background reset
    draw_bg()

    # bullet
    bullet_group.update()
    bullet_group.draw(screen)

    # fps
    clock.tick(FPS)

    if player.Alive:
        # update actions (idle, running, jumping)
        if shoot:
            player.shoot()
            player.update_action(3)  # 3 - shooting
        elif player.in_air:
            player.update_action(2)  # 2 - jumping
        elif moving_left or moving_right:
            player.update_action(1)  # 1 - running
        else:
            player.update_action(0)  # 0 - idle

    # update frames
    player.update()
    enemy.update()

    # load sprite
    player.draw()
    enemy.draw()

    # move sprite
    player.move(moving_left, moving_right)

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
            if (key == pygame.K_w or key == pygame.K_UP) and player.Alive:
                player.jump = True

            if key == pygame.K_SPACE:
                shoot = True

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

            if key == pygame.K_SPACE:
                shoot = False

    pygame.display.update()

pygame.quit()
