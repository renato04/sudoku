import board
import solver
from pattern import Pattern
import time as t
import constants as c

class Generator:


    def generate(self, mode = c.random_difficulty,
                 difficulty = c.easy):
        b = None
        s = solver.Solver()
        count = 0

        start = t.time()

        while b == None or count != 1:
 
            if mode == c.random_difficulty:
                b = self.random(difficulty)
            elif mode == c.pattern_difficulty:
                b = self.pattern(difficulty)
            elif mode == c.board_difficulty:
                b = self.board(difficulty)

            count = s.count_solutions(b, 2)

        end = t.time()

        print('Sudoku board generated in ' + str(end - start))
        return b

    def random(self, difficulty):
        board = self.get_board()
        p = Pattern.random_difficulty()
        print(p)
        return p.set_board(board)

    def get_board(self):
        return solver.Solver().solve(board.Board())
        
        
