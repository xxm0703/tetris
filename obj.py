import pygame
pygame.init()
BLACK = (0,0,0)
class Box(object):
    def __init__(self, surface, x, y, box_size):
        self.display = surface
        self.x = x
        self.y = y
        self.box_size = box_size
    def Draw(self):
        return pygame.draw.rect(self.display,BLACK,[self.x*10,self.y*10,self.box_size,self.box_size])

    def Param(self):
        return self.y
        return self.x
class O(Box):
    pass
class I(Box):
    pass
class S(Box):
    pass
class Z(Box):
    pass
class L(Box):
    pass
class J(Box):
    pass
class T(Box):
    pass