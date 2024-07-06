import pygame

from object import Object
from settings import *


class Ship(Object):
    def __init__(self):
        super().__init__('textures/mask_default.png')

        self.speed = 20

        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT - 100

        self.width = SHIP_WIDTH
        self.height = SHIP_HEIGHT

        self.mask_happiness = 0

        self.texture_default = pygame.image.load('textures/mask_default.png').convert_alpha()
        self.texture_default = pygame.transform.scale(self.texture_default, (SHIP_WIDTH, SHIP_HEIGHT))

        self.texture_happy = pygame.image.load('textures/mask_happy.png').convert_alpha()
        self.texture_happy = pygame.transform.scale(self.texture_happy, (SHIP_WIDTH, SHIP_HEIGHT))

    def draw(self, screen):
        if self.mask_happiness > 0:
            screen.blit(self.texture_happy, (self.x, self.y))
        else:
            screen.blit(self.texture_default, (self.x, self.y))

    def update(self):
        super().update()
        self.mask_happiness -= 1

    def control(self, event):
        if event.key == pygame.K_LEFT:
            self.x -= self.speed
        if event.key == pygame.K_RIGHT:
            self.x += self.speed
