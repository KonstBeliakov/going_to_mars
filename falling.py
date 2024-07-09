from random import randrange

import settings
from object import Object
from settings import *


class Falling(Object):
    def __init__(self, texture_filename, x=0, y=0, sizeX=100, sizeY=100):
        super().__init__(texture_filename, x=x, y=y, sizeX=sizeX, sizeY=sizeY)
        self.reset()

    def reset(self):
        self.x = randrange(0, SCREEN_WIDTH - self.sizeX)
        self.y = -self.sizeX - randrange(600)

    def update(self):
        super().update()
        self.speedY = settings.FALLING_SPEED
        if self.y > SCREEN_HEIGHT:
            self.reset()
