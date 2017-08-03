import collections
from random import randint
Point = collections.namedtuple('Point', ['x', 'y'])
Cell = collections.namedtuple('Cell', ['x', 'y'])


class Shape:
    def __init__(self, ID, cells):
        self.cells = cells
        self.ID = ID

    def rotate(self):
        rotated = tuple([Point(-y, x) for x, y in self.cells])
        return Shape(self.ID, rotated)

    def __str__(self):
        return list_to_str(self.cells)


class Block:
    def __init__(self, shape, origin):
        self.shape = shape
        self.cells = tuple([Point(x + origin.x, y + origin.y) for x, y in shape.cells])
        self.origin = origin

    def move(self, x, y):
        no = Point(self.origin.x + x, self.origin.y + y)
        return Block(self.shape, no)


class Board:
    shapes = [Shape('£', (Point(0, 0), Point(1, 0), Point(-1, 0), Point(1, 1))),
              Shape('@', (Point(0, 0), Point(1, 0), Point(2, 0), Point(-1, 0))),
              Shape('#', (Point(0, 0), Point(1, 0), Point(-1, 0), Point(-1, 1)))]

    def __init__(self, XSZ, YSZ):
        self.XSZ = XSZ
        self.YSZ = YSZ
        self.fields = [[None for _ in range(YSZ)] for _ in range(XSZ)]
        self.current = None
        assert self.fields[0] is not self.fields[1]
        self.change_current()
        self.place_block(self.current)

    def place_block(self, block):
        for x, y in block.cells:
            if 0 > x or x >= self.XSZ or y >= self.YSZ or self.fields[x][y] is not None:
                return False
        for x, y in block.cells:
            self.fields[x][y] = block
        return True

    def remove_block(self, block):
        for x, y in block.cells:
            #            assert self.fields[x][y] is block
            self.fields[x][y] = None

    def rotate_block(self):
        bs = self.current.shape.rotate()
        helper_block = Block(bs, self.current.origin)
        self.remove_block(self.current)
        if not self.place_block(helper_block):
            self.place_block(self.current)
        else:
            self.current = helper_block

    def move_block(self, direct):
        hb = self.current.move(direct, 0)
        self.remove_block(self.current)
        if not self.place_block(hb):
            self.place_block(self.current)
        else:
            self.current = hb

    def clear_line(self):
        #TODO
        for y in range(self.YSZ):
            for x in range(self.XSZ):
                if self.fields[x][y] is None:
                    break
            else:
                for x in range(self.XSZ):
                    self.fields[x][y] = None
                for k in range(y - 1, -1, -1):
                    for j in range(self.XSZ):
                        self.fields[j][k + 1] = self.fields[j][k]
                        self.fields[j][k] = None

    def change_current(self):
        self.current = Block(Board.shapes[randint(0, 2)], Point(5, 0))

    def drop(self):
        hb = self.current.move(0, 1)
        self.remove_block(self.current)
        if not self.place_block(hb):
            self.place_block(self.current)
            self.change_current()
            self.clear_line()
        else:
            self.current = hb

    def __str__(self):
        return self.str_zoom(2)

    def str_zoom(self, zoom):
        res = ''
        for y in range(self.YSZ):
            s = '\n%2d\t|' % y
            for x in range(self.XSZ):
                s += zoom * (' ' if self.fields[x][y] is None else "%1s" % self.fields[x][y].shape.ID[0]) + '|'
            res += zoom * s
        return res


def list_to_str(l):
    s = '['
    for x in l:
        s += str(x) + ', '
    s += ']'
    return s


if __name__ == '__main__':
    board = Board(10, 20)
    # s1 = Shape('%', (Point(0, 0), Point(1, 0), Point(0, 1)))
    # s2 = Shape('#', (Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0), Point(4, 0), Point(5, 0), Point(6, 0)))
    # a = Block(s2, Point(0, 3))
    # b = Block(s1, Point(5, 0))
    # c = Block(s1, Point(8, 3))
    # board.place_block(a)
    # board.place_block(b)
    # board.place_block(c)
    print(board)
    board.drop()
    #    board.rotate_block()
    board.clear_line()
    # board.remove_block(b)
    print(board)
    board.rotate_block()
    board.drop()
    print(board)
