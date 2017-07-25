import collections

Point = collections.namedtuple('Point', ['x', 'y'])
Cell = collections.namedtuple('Cell', ['x', 'y'])


class Board:
    def __init__(self, XSZ, YSZ):
        self.XSZ = XSZ
        self.YSZ = YSZ
        self.fields = [[None for _ in range(YSZ)] for _ in range(XSZ)]
        assert self.fields[0] is not self.fields[1]

    def place_block(self, block):
        for x, y in block.cells:
            if self.fields[x][y] is not None or 0 > x or x >= self.XSZ:
                return False
        for x, y in block.cells:
            self.fields[x][y] = block
        return True

    def remove_block(self, block):
        for x, y in block.cells:
            assert self.fields[x][y] is block
            self.fields[x][y] = None

    def rotate_block(self, block):
        bs = block.shape
        bs.rotate()
        helper_block = Block(block.ID, bs, block.cells[0])
        self.remove_block(block)
        if not self.place_block(helper_block):
            self.place_block(block)
            return block
        else:
            return helper_block

    def __str__(self):
        return self.str_zoom(2)

    def str_zoom(self, zoom):
        res = ''
        for y in range(self.YSZ):
            str = '\n%2d\t|' % y
            for x in range(self.XSZ):
                str += zoom * (' ' if self.fields[x][y] is None else "%1s" % self.fields[x][y].ID[0]) + '|'
            res += zoom * str
        return res


class Shape:
    def __init__(self, cells):
        self.cells = cells

    def rotate(self):
        i = 0
        for x, y in self.cells:
            self.cells[i] = Point(-y, x)
            i += 1

    @staticmethod
    def get(cells):
        pass


class Block:
    def __init__(self, ID, shape, origin):
        self.ID = ID
        self.shape = shape
        self.cells = [Point(x + origin.x, y + origin.y) for x, y in shape.cells]


board = Board(10, 20)
s = Shape([Point(0, 0), Point(1, 0), Point(0, 1)])
b = Block('#', s, Point(5, 0))
c = Block('*', s, Point(0, 0))
board.place_block(b)
board.place_block(c)
print(board)
c = board.rotate_block(c)
board.remove_block(b)
print(board)
# c = board.rotate_block(c)
# print(board)
