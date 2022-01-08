# modules
import pygame
from src.modules.userDefinedFunctions import *
from src.modules.gameVariables import *
from src.modules.mainScreen import *


class Player(pygame.sprite.Sprite):
    def __init__(self, playerType, x, y, scale, defaultSize=50, speed=5):
        pygame.sprite.Sprite.__init__(self)
        self.Alive = True
        self.playerType = playerType
        self.scale = scale
        self.defaultSize = defaultSize
        self.jump = False
        self.in_air = True
        self.vel_y = 0
        self.animation_list = []
        self.update_time = pygame.time.get_ticks()
        self.action = 0  # 0 for idle, 1 for run

        self.add_images('idle')
        self.add_images('run')
        self.add_images('jump')

        self.frameIndex = 0
        self.image = self.animation_list[self.action][self.frameIndex]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.speed = speed
        self.flip = False

    def add_images(self, type):
        temp_list = []
        for i in range(2):
            img = pygame.image.load(
                "./src/images/sprites/{}/{}/{}.png".format(
                    self.playerType, type, i)
            )
            scaledWidth = self.defaultSize*self.scale
            scaledHeight = scaledWidth * (img.get_height()/img.get_width())
            scaledWidth = int(scaledWidth)
            scaledHeight = int(scaledHeight)

            img = pygame.transform.scale(img, (scaledWidth, scaledHeight))

            temp_list.append(img)
        self.animation_list.append(temp_list)

    def move(self, left, right):

        dx = 0
        dy = 0

        if left:
            dx = -self.speed
            self.flip = True
        if right:
            dx = self.speed
            self.flip = False
        if self.jump and (not self.in_air):
            self.vel_y = -11
            self.jump = False
            self.in_air = True

        # gravity
        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y
        dy += self.vel_y

        # floor collision
        if self.rect.bottom + dy > FLOOR:
            dy = FLOOR - self.rect.bottom
            self.in_air = False

        self.rect.x += dx
        self.rect.y += dy

    def update_animation(self):
        ANIMATION_COOLDOWN = 100
        self.image = self.animation_list[self.action][self.frameIndex]
        if pygame.time.get_ticks()-self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frameIndex += 1
            if self.frameIndex >= len(self.animation_list[self.action]):
                self.frameIndex = 0

    def update_action(self, new_action):
        if self.action == new_action:
            return

        self.action = new_action
        self.frameIndex = 0
        self.update_time = pygame.time.get_ticks()

    def draw(self):
        afterRotationImg = pygame.transform.flip(self.image, self.flip, False)
        screen.blit(afterRotationImg, self.rect)
