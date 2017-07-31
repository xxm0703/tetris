from board_game import Board
import pygame

pygame.init()


class Engine:
    def __init__(self, FPS, board):
        self.board = board
        self.MPF = 1000 // FPS
        self.speed = None

    def game_loop(self):
        while True:  # Game Loop
            self.speed = self.MPF
            for x in range(4):
                self.get_event()
                pygame.time.Clock().tick(100)

            pygame.time.Clock().tick(self.MPF)
            self.board.drop()
            print(self.board)

    def get_event(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.board.rotate_block()
                elif event.key == pygame.K_DOWN:
                    self.speed = self.MPF / 2


if __name__ == '__main__':
    e = Engine(1, Board(10, 20))
    e.game_loop()
