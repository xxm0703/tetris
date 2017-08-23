from board_game import Board
from render import Graphic
import pygame, sys


pygame.init()


class Engine:
    def __init__(self, FPS, board, resolution):
        self.board = board
        self.MPF = 1000 // FPS
        self.speed = self.MPF
        self.render = Graphic(board, resolution)
        self.move = 0
        self.clock = pygame.time.Clock()

    def game_loop(self):
        while True:  # Game Loop
            for x in range(4):
                self.get_event()
                if self.move != 0:
                    self.board.move_block(self.move)
                self.render.draw()
                self.render.update()
                self.clock.tick(self.speed)
            # self.clock.tick(self.speed)
            try:
                self.board.drop()
            except Board.GameOver:
                print("Game Over!")
                pygame.quit()
                sys.exit()

    def get_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

                elif event.key == pygame.K_LEFT:
                    self.move = -1
                elif event.key == pygame.K_RIGHT:
                    self.move = 1

                if event.key == pygame.K_UP:
                    self.board.rotate_block()
                elif event.key == pygame.K_DOWN:
                    self.speed = self.MPF * 4

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self.speed = self.MPF
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    self.move = 0

if __name__ == '__main__':
    e = Engine(90, Board(10, 20), 20)
    e.game_loop()
