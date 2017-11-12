import pygame
from json import load

from board_game import Board
from render import Graphic

pygame.init()


class Engine:
    def __init__(self, fps, board, resolution):
        self.board = board
        self.speed = 1000 // fps  # MPF
        self.MPF = self.speed  # reset
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
            try:
                self.board.drop()
            except Board.GameOver:
                pygame.quit()
                exit("Game Over!")

    def get_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit("End Of Game")

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit("End Of Game")

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
    with open(".settings.conf", 'r') as f:
        settings = load(f)
    settings['speed'] = 110 - settings['speed']
    e = Engine(settings['speed'], Board(10, 20), settings['resolution'])
    e.game_loop()
