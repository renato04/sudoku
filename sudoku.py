import pattern
from generator import Generator
import constants as c
import time as t

class Sudoku:

    def __init__(self):
        self.difficulty = c.easy
        self.mode = c.random_difficulty
        self.board = Generator().generate(self.mode, self.difficulty)

        self.win = False
        self.t0 =  t.time()


    def set_number(self, line, col, value):
        self.board[line][col] = value
        if self.board.is_valid():
          self.win = true
          self.ellapsed = t.time() - self.t0

    def erase(self, line, col):
        self.board[line][col] = 0

    def is_fixed_cell(line, col):
        self.pattern[line * c.Size + col]
            
