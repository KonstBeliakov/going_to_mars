import random
import pygame

from settings import *


class Object:
    def __init__(self, texture_filename):
        self.x = random.randrange(0, SCREEN_WIDTH - ASTEROID_WIDTH)
        self.y = -ASTEROID_HEIGHT - random.randrange(600)
        self.speed = 2
        self.texture = pygame.image.load(texture_filename).convert_alpha()
        self.texture = pygame.transform.scale(self.texture, (ASTEROID_WIDTH, ASTEROID_HEIGHT))

    def move(self):
        self.y += self.speed

    def reset(self):
        self.y = -ASTEROID_HEIGHT
        self.x = random.randrange(0, SCREEN_WIDTH - ASTEROID_WIDTH)

    def draw(self, screen):
        screen.blit(self.texture, (self.x, self.y))  # draw the asteroid texture

    def collides_with(self, ship_x, ship_y):
        return (self.y + ASTEROID_HEIGHT > ship_y) and (self.x < ship_x + SHIP_WIDTH) and (
                self.x + ASTEROID_WIDTH > ship_x)
