import random
import pygame

from settings import *


class Asteroid:
    def __init__(self):
        self.x = random.randrange(0, SCREEN_WIDTH - ASTEROID_WIDTH)
        self.y = -ASTEROID_HEIGHT - random.randrange(300)
        self.speed = 2

    def move(self):
        self.y += self.speed

    def reset(self):
        self.y = -ASTEROID_HEIGHT
        self.x = random.randrange(0, SCREEN_WIDTH - ASTEROID_WIDTH)

    def draw(self, screen):
        pygame.draw.rect(screen, ASTEROID_COLOR, pygame.Rect(self.x, self.y, ASTEROID_WIDTH, ASTEROID_HEIGHT))

    def collides_with(self, ship_x, ship_y):
        return (self.y + ASTEROID_HEIGHT > ship_y) and (self.x < ship_x + SHIP_WIDTH) and (
                self.x + ASTEROID_WIDTH > ship_x)
