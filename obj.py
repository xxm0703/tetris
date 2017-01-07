import pygame
import random

pygame.init()
R = random.randint(0, 255)
G = random.randint(0, 255)
B = random.randint(0, 255)
COLOR = (R, G, B)
print(COLOR)


class Box(object):
    def __init__(self, surface, x, y, box_size):
        self.display = surface
        self.box_size = box_size
        self.x = x
        self.y = y

    def Draw(self):
        return pygame.draw.rect(self.display, COLOR, [self.x * 10, self.y * 10, self.box_size, self.box_size], 3)

    def Struct(self):
        pass

    def Param(self, add_x=0, add_y=0):
        return [self.x+add_x, self.y+add_y]


class O(object):
    def __init__(self, surface, x, y, box_size):
        self.display = surface
        self.box_size = box_size
        self.x = x
        self.y = y
        self.list_cords = [O.Param(self, self.x, self.y), O.Param(self, self.x, self.y, add_x=1),
                           O.Param(self, self.x, self.y, add_y=1), O.Param(self, self.x, self.y, add_x=1, add_y=1)]

    def Struct(self):
        for cord in self.list_cords:
            Box(self.display,cord[0],cord[1],self.box_size).Draw()

    def Param(self, x, y, add_x=0, add_y=0):
        return [x+add_x, y+add_y]

    def Ret_list(self):
        return self.list_cords

    def Ret_y(self):
        return [self.y, self.y+1]


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
