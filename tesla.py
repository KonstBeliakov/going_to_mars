from falling import Falling


class Tesla(Falling):
    def __init__(self):
        super().__init__('textures/tesla.png', sizeX=50, sizeY=50)
        self.speedY = 2
