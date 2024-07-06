import pygame


class Object:
    def __init__(self, texture_filename, x=0, y=0, sizeX=100, sizeY=100):
        self.x = x
        self.y = y
        self.speedX = 0
        self.speedY = 0
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.texture = pygame.image.load(texture_filename).convert_alpha()
        self.texture = pygame.transform.scale(self.texture, (sizeX, sizeY))

    def update(self):
        self.x += self.speedX
        self.y += self.speedY

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def size(self):
        return self.sizeX, self.sizeY

    def pos(self):
        return self.x, self.y

    def draw(self, screen):
        screen.blit(self.texture, (self.x, self.y))

    def collides_with(self, object):
        return (self.x + self.sizeX > object.x) and (object.x + object.sizeX > self.x) and \
            (self.y + self.sizeY > object.y) and (object.y + object.sizeY > self.y)
