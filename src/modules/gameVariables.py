import pygame

clock = pygame.time.Clock()
FPS = 60

moving_left = False
moving_right = False
moving_up = False
moving_down = False
shoot = False

GRAVITY = 0.75
BG_COLOR = (144, 201, 100)
RED = (255, 0, 0)


bullet_img = pygame.image.load(
    "./src/images/objects/bullet.png")
scale = 1
new_bullet_width = scale * bullet_img.get_width()
new_bullet_height = (bullet_img.get_height() /
                     bullet_img.get_width()) * new_bullet_width
new_bullet_width = int(new_bullet_width)
new_bullet_height = int(new_bullet_height)
bullet_img = pygame.transform.scale(
    bullet_img, (new_bullet_width, new_bullet_height))
