import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, defaultSize=50):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("./src//freedinosprite/png/Idle (1).png")
        scaledWidth = defaultSize*scale
        scaledHeight = scaledWidth * (img.get_height()/img.get_width())
        scaledWidth = int(scaledWidth)
        scaledHeight = int(scaledHeight)

        img = pygame.transform.scale(img, (scaledWidth, scaledHeight))

        rect = img.get_rect()
        rect.center = (x, y)

        self.img = img
        self.rect = rect
