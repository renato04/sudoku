import sys
sys.path.append('../')

import unittest
import solver
import board
import generator

class SolverTest(unittest.TestCase):
    def setUp(self):
        self.seq = solver.Solver()

    def should_find_out_when_there_is_no_solution(self):
        b = generator.Generator().generate()
        b.show()
        b[0][0] = 1
        b[0][1] = 1
        b[0][2] = 0

        a = self.seq.solve(b)

        if a != None:
            raise Exception

    def test_should_solve_empty_board(self):
        a = self.seq.solve(board.Board())

        if a == None:
            raise Exception
    
    def test_should_correctly_count_the_solutions_2(self):
        arr = [
          [5, 9, 1,   8, 4, 7,   6, 2, 3],   
          [4, 2, 3,   6, 9, 1,   7, 5, 8],
          [8, 6, 7,   2, 3, 5,   1, 4, 9],   

          [1, 8, 4,   3, 5, 9,   2, 7, 6],  
          [2, 3, 9,   0, 7, 6,   5, 8, 0],  
          [6, 7, 5,   0, 2, 8,   3, 9, 0], 

          [9, 5, 8,   7, 6, 3,   4, 1, 2],  
          [3, 1, 2,   5, 8, 4,   9, 6, 7], 
          [7, 4, 6,   9, 1, 2,   8, 3, 5]]

        b = board.Board(arr)
        solutions = self.seq.count_solutions(b)

        if solutions != 2:
            raise Exception('Solutions should be 2. The returned value was '
                            + str(solutions))

    def test_should_correctly_count_the_solutions_1(self):
        arr = [
          [5, 9, 1,   8, 4, 7,   6, 2, 3],   
          [4, 2, 3,   6, 9, 1,   7, 5, 8],
          [8, 6, 7,   2, 3, 5,   1, 4, 9],   

          [1, 8, 4,   3, 5, 9,   2, 7, 6],  
          [2, 3, 9,   0, 7, 6,   5, 8, 0],  
          [6, 7, 5,   1, 2, 8,   3, 9, 0], 

          [9, 5, 8,   7, 6, 3,   4, 1, 2],  
          [3, 1, 2,   5, 8, 4,   9, 6, 7], 
          [7, 4, 6,   9, 1, 2,   8, 3, 5]]

        b = board.Board(arr)
        solutions = self.seq.count_solutions(b)

        if solutions != 1:
            raise Exception('Solutions should be 1. The returned value was '
                            + str(solutions))        
