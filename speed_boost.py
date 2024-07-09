from falling import Falling


class SpeedBoost(Falling):
    def __init__(self):
        size = 30
        super().__init__(f"textures/speed_boost.png", sizeX=size, sizeY=size)
        self.speedY = 2

