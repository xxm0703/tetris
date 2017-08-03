import pygame
from board_game import Board

pygame.init()


class Graphic:
    colors = {'£': (255, 0, 0), '@': (0, 255, 0), '#': (0, 0, 255)}

    def __init__(self, board, resolution):
        self.board = board
        self.size = resolution
        self.width = board.XSZ * resolution
        self.high = board.YSZ * resolution
        self.screen = pygame.display.set_mode((self.width, self.high))

    def update(self):
        pygame.display.update()

    def draw(self):
        self.screen.fill((250, 250, 250))
        for x in range(self.board.XSZ):
            for y in range(self.board.YSZ):
                if self.board.fields[x][y] is not None:
                    pygame.display.update()
                    pygame.draw.rect(self.screen, Graphic.colors[self.board.fields[x][y].shape.ID],
                                     [x * self.size, y * self.size, self.size, self.size], 2)


if __name__ == '__main__':
    pass