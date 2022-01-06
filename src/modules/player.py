# modules
import pygame

from src.modules.mainScreen import *


class Player(pygame.sprite.Sprite):
    def __init__(self, playerType, x, y, scale, defaultSize=50, speed=5):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(
            "./src/images/sprites/{}/idle.png".format(playerType)
        )
        scaledWidth = defaultSize*scale
        scaledHeight = scaledWidth * (img.get_height()/img.get_width())
        scaledWidth = int(scaledWidth)
        scaledHeight = int(scaledHeight)

        img = pygame.transform.scale(img, (scaledWidth, scaledHeight))

        rect = img.get_rect()
        rect.center = (x, y)

        self.img = img
        self.rect = rect
        self.speed = speed
        self.flip = False

    def move(self, left, right, up, down):

        dx = 0
        dy = 0

        if left:
            dx = -self.speed
            self.flip = True
        if right:
            dx = self.speed
            self.flip = False
        if up:
            dy = self.speed

        if down:
            dy = -self.speed

        self.rect.x += dx
        self.rect.y += dy

    def draw(self):
        afterRotationImg = pygame.transform.flip(self.img, self.flip, False)
        screen.blit(afterRotationImg, self.rect)
