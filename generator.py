import board
import solver
from pattern import Pattern
import time as t

class Generator:
    random_difficulty = 'r'
    pattern_difficulty = 'p'
    board_difficulty = 'b'
    easy = 'e'

    def generate(self, mode = random_difficulty,
                 difficulty = easy):
        b = None
        s = solver.Solver()
        count = 0

        start = t.time()

        while b == None or count != 1:
 
            if mode == self.random_difficulty:
                b = self.random(difficulty)
            elif mode == self.pattern_difficulty:
                b = self.pattern(difficulty)
            elif mode == self.board_difficulty:
                b = self.board(difficulty)

            count = s.count_solutions(b, 2)

        end = t.time()

        print('Sudoku board generated in ' + str(end - start))

    def random(self, difficulty):
        board = self.get_board()
        p = Pattern.random_difficulty()
        print(p)
        return p.set_board(board)

    def get_board(self):
        return solver.Solver().solve(board.Board())
        
        
