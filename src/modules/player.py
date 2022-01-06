# modules
import pygame

from src.modules.mainScreen import *


class Player(pygame.sprite.Sprite):
    def __init__(self, playerType, x, y, scale, defaultSize=50, speed=5):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(
            "./src/images/sprites/{}/0.png".format(playerType)
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

    def move(self, left, right, up, down):
        
        dx = 0
        dy = 0

        if left:
            dx = -self.speed

        if right:
            dx = self.speed

        if up:
            dy = self.speed

        if down:
            dy = -self.speed

        self.rect.x += dx
        self.rect.y += dy

    def draw(self):
        screen.blit(self.img, self.rect)
