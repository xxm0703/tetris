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
    def __init__(self, x, y, L):
        self.x = x
        self.y = y
        self.list_cords = L

    def Ret_x(self):
        return [x for x, y in self.list_cords]

    def Ret_y(self):
        return [y for x,y in self.list_cords]

    def Rotate(self):
        self.list_cords = [[-y, x] for x,y in self.list_cords]

    def Param(self, x, y, add_x=0, add_y=0):
        return [x+add_x, y+add_y]

    def Ret_list(self):
        return self.list_cords

class O(Basic):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        Basic.__init__(self,self.x,self.y,[Basic.Param(self, self.x, self.y), Basic.Param(self, self.x, self.y, add_x=1),
                           Basic.Param(self, self.x, self.y, add_y=1), Basic.Param(self, self.x, self.y, add_x=1, add_y=1)])

class I(Basic):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        Basic.__init__(self,self.x,self.y,[Basic.Param(self, self.x, self.y), Basic.Param(self, self.x, self.y, add_x=-1),
                           Basic.Param(self, self.x, self.y, add_x=1), Basic.Param(self, self.x, self.y, add_x=-2)])

class S(Basic):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        Basic.__init__(self,self.x,self.y,[Basic.Param(self, self.x, self.y), Basic.Param(self, self.x, self.y, add_x=1),
                           Basic.Param(self, self.x, self.y, add_y=1), Basic.Param(self, self.x, self.y, add_x=-1, add_y=1)])

class Z(Basic):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        Basic.__init__(self,self.x,self.y,[Basic.Param(self, self.x, self.y), Basic.Param(self, self.x, self.y, add_x=-1),
                           Basic.Param(self, self.x, self.y, add_y=1), Basic.Param(self, self.x, self.y, add_x=1, add_y=1)])


class L(Basic):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        Basic.__init__(self,self.x,self.y,[Basic.Param(self, self.x, self.y), Basic.Param(self, self.x, self.y, add_x=1),
                           Basic.Param(self, self.x, self.y, add_x=-1), Basic.Param(self, self.x, self.y, add_x=-1, add_y=1)])


class J(Basic):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        Basic.__init__(self,self.x,self.y,[Basic.Param(self, self.x, self.y), Basic.Param(self, self.x, self.y, add_x=-1),
                           Basic.Param(self, self.x, self.y, add_x=1), Basic.Param(self, self.x, self.y, add_x=1, add_y=1)])


class T(Basic):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        Basic.__init__(self,self.x,self.y,[Basic.Param(self, self.x, self.y), Basic.Param(self, self.x, self.y, add_x=1),
                           Basic.Param(self, self.x, self.y, add_x=-1), Basic.Param(self, self.x, self.y, add_y=1)])
