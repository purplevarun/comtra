import pygame
from src.modules.gameVariables import *
from src.modules.mainScreen import *


class Bullet (pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction

    def update(self):

        self.rect.x += self.direction * self.speed

        if self.rect.right < 0 or self.rect.left > screenWidth:
            self.kill()


bullet_group = pygame.sprite.Group()
