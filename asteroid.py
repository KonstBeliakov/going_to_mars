from random import randrange

from falling import Falling


class Asteroid(Falling):
    def __init__(self):
        size = randrange(20, 70)
        super().__init__(f"textures/asteroid{randrange(3)}.png", sizeX=size, sizeY=size)
        self.speedY = 2
