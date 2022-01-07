# import python modules
import pygame

# import local modules
from src.modules.player import *
from src.modules.mainScreen import *
# user defined functions


def draw_bg():
    BG_COLOR = (144, 201, 100)
    screen.fill(BG_COLOR)


def draw(*x):
    for i in x:
        screen.blit(i.img, i.rect)


def moving():
    if moving_left or moving_right or moving_up or moving_down:
        return True
    return False


# initialization


moving_left = False
moving_right = False
moving_up = False
moving_down = False

clock = pygame.time.Clock()
FPS = 60

player = Player("player", 200, 200, 2)
player2 = Player("player", 400, 400, 4)

# game loop
gameRunning = True
while gameRunning:
    # inf game loop

    # background reset
    draw_bg()

    # fps
    clock.tick(FPS)

    # update actions (idle, running.. etc)
    if moving():
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
