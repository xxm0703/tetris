import random

import pygame

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

    def Param(self, add_x=0, add_y=0):
        return [self.x+add_x, self.y+add_y]

class Basic(object):
    def __init__(self, surface, x, y, box_size):
        self.display = surface
        self.box_size = box_size
        self.x = x
        self.y = y
    def Rotate(self, List):
        List = [[x,y]]
        return
    def Param(self, x, y, add_x=0, add_y=0):
        return [x+add_x, y+add_y]
class O(Basic):
    def __init__(self, surface, x, y, box_size):
        Basic.__init__(self,surface,x,y,box_size)
        self.list_cords = [Basic.Param(self, self.x, self.y), Basic.Param(self, self.x, self.y, add_x=1),
                           Basic.Param(self, self.x, self.y, add_y=1), Basic.Param(self, self.x, self.y, add_x=1, add_y=1)]
    def Ret_list(self):
        return self.list_cords

    def Ret_y(self):
        return [self.y, self.y+1]


class S(Basic):
    def __init__(self, surface, x, y, box_size):
        Basic.__init__(self,surface,x,y,box_size)
        self.list_cords = [Basic.Param(self, self.x, self.y), Basic.Param(self, self.x, self.y, add_x=1),
                           Basic.Param(self, self.x, self.y, add_y=1), Basic.Param(self, self.x, self.y, add_x=-1, add_y=1)]
    def Ret_list(self):
        return self.list_cords

    def Ret_y(self):
        return [self.y, self.y+1]


class Z(Box):
    pass


class L(Box):
    pass


class J(Box):
    pass


class T(Box):
    pass
