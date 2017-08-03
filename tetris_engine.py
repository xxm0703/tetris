from board_game import Board
from render import Graphic
import pygame, os

pygame.init()


class Engine:
    def __init__(self, FPS, board, resolution):
        self.board = board
        self.MPF = 10 // FPS
        self.speed = self.MPF
        self.render = Graphic(board, resolution)

    def game_loop(self):
        while True:  # Game Loop
            for x in range(4):
                self.get_event()
                self.render.draw()
                self.render.update()
                pygame.time.Clock().tick(self.speed)
            pygame.time.Clock().tick(self.speed)
            self.board.drop()

    def get_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.board.rotate_block()
                elif event.key == pygame.K_DOWN:
                    self.speed = self.MPF * 4

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self.speed = self.MPF


if __name__ == '__main__':
    e = Engine(1, Board(10, 20), 10)
    e.game_loop()
