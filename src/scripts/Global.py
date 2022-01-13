# this script will only export
import pygame


clock = pygame.time.Clock()
FPS = 60

moving_left = False
moving_right = False
moving_up = False
moving_down = False
shoot = False
grenade = False
grenade_thrown = False

GRAVITY = 0.75
TILE_SIZE = 40
BG_COLOR = (144, 201, 100)
RED = (255, 0, 0)


def resize_image(imgurl, scale=3):
    bullet_img = pygame.image.load(
        imgurl)
    new_bullet_width = scale * bullet_img.get_width()
    new_bullet_height = (bullet_img.get_height() /
                         bullet_img.get_width()) * new_bullet_width
    new_bullet_width = int(new_bullet_width)
    new_bullet_height = int(new_bullet_height)
    bullet_img = pygame.transform.scale(
        bullet_img, (new_bullet_width, new_bullet_height))

    return bullet_img


bullet_img = resize_image("./src/images/objects/bullet.png")
grenade_img = resize_image("./src/images/objects/grenade.png")

pygame.init()

screenWidth = pygame.display.Info().current_w
screenHeight = pygame.display.Info().current_h
pygame.display.set_caption("Comtra")

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # fullscreen mode

# screenWidth = 800
# screenHeight = int(0.8 * screenWidth)
# screen = pygame.display.set_mode((screenWidth, screenHeight))  # windowed


FLOOR = 700
