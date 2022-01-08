import pygame
from src.scripts.Global import *
from src.scripts.functions import *


class Player(pygame.sprite.Sprite):
    def __init__(self, playerType, x, y, scale, defaultSize=50, speed=5, ammo=20):
        pygame.sprite.Sprite.__init__(self)
        self.Alive = True
        self.playerType = playerType
        self.scale = scale
        self.defaultSize = defaultSize
        self.ammo = ammo
        self.start_ammo = ammo
        self.jump = False
        self.in_air = True
        self.vel_y = 0
        self.animation_list = []
        self.update_time = pygame.time.get_ticks()
        self.action = 0  # 0 for idle, 1 for run

        self.add_images('idle')
        self.add_images('run')
        self.add_images('jump')
        self.add_images('shoot')

        self.frameIndex = 0
        self.image = self.animation_list[self.action][self.frameIndex]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.speed = speed
        self.shoot_cooldown = 0
        self.flip = False
        self.direction = 1

    def update(self):
        self.update_animation()

        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def shoot(self):
        if self.shoot_cooldown == 0 and self.ammo > 0:
            self.shoot_cooldown = 20
            self.ammo -= 1
            bullet = Bullet(self.rect.centerx + self.direction*0.6 *
                            self.rect.size[0], self.rect.centery, self.direction)
            bullet_group.add(bullet)

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
            self.direction = -1
        if right:
            dx = self.speed
            self.flip = False
            self.direction = 1

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

        if pygame.sprite.spritecollide(player, bullet_group, False):
            if player.alive:
                self.kill()

        if pygame.sprite.spritecollide(enemy, bullet_group, False):
            if enemy.alive:
                self.kill()


player = Player("player", x=200, y=400, scale=5)
enemy = Player("player", x=400, y=400, scale=4)


bullet_group = pygame.sprite.Group()