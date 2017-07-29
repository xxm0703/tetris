from board_game import Board
import pygame

class Engine:
    def __init__(self, FPS, board):
        self.board = board
        self.MPF = 1000 // FPS

    def game_loop(self):
        while True:
            self.get_event()
