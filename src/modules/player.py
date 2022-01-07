# modules
import pygame

from src.modules.mainScreen import *


class Player(pygame.sprite.Sprite):
    def __init__(self, playerType, x, y, scale, defaultSize=50, speed=5):
        pygame.sprite.Sprite.__init__(self)
        self.animation_list = []
        self.update_time = pygame.time.get_ticks()
        for i in range(4):
            img = pygame.image.load(
                "./src/images/sprites/{}/idle/{}.png".format(playerType, i)
            )
            scaledWidth = defaultSize*scale
            scaledHeight = scaledWidth * (img.get_height()/img.get_width())
            scaledWidth = int(scaledWidth)
            scaledHeight = int(scaledHeight)

            img = pygame.transform.scale(img, (scaledWidth, scaledHeight))

            self.animation_list.append(img)
        for i in range(4):
            img = pygame.image.load(
                "./src/images/sprites/{}/run/{}.png".format(playerType, i)
            )
            scaledWidth = defaultSize*scale
            scaledHeight = scaledWidth * (img.get_height()/img.get_width())
            scaledWidth = int(scaledWidth)
            scaledHeight = int(scaledHeight)

            img = pygame.transform.scale(img, (scaledWidth, scaledHeight))

            self.animation_list.append(img)
        self.frameIndex = 0
        self.image = self.animation_list[self.frameIndex]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

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

    def update_animation(self):
        ANIMATION_COOLDOWN = 100
        self.image = self.animation_list[self.frameIndex]
        if pygame.time.get_ticks()-self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frameIndex += 1
            if self.frameIndex >= len(self.animation_list):
                self.frameIndex = 0

    def draw(self):
        afterRotationImg = pygame.transform.flip(self.image, self.flip, False)
        screen.blit(afterRotationImg, self.rect)
