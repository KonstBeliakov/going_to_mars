from falling import Falling
from settings import *


class Asteroid(Falling):
    def __init__(self):
        super().__init__("textures/asteroid.png", sizeX=ASTEROID_WIDTH, sizeY=ASTEROID_HEIGHT)
        self.speedY = 2
