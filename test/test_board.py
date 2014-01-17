import sys
sys.path.append('../')

import unittest
import board


class BoardTest(unittest.TestCase):
    
    def setUp(self):
        self.seq = board.Board()

    def checkEqual(self, L1, L2):
        return len(L1) == len(L2) and sorted(L1) == sorted(L2)

    def should_create_a_matrix(self):
        self.assertIsInstance(type(self.seq), list)
        self.assertIsInstance(type(self.seq[0]), list)

    def test_should_build_correct_squares(self):
        for i, val in enumerate(range(0,9)):
            self.seq[int(i/3)][int(i%3)] = i + 1
            
        if not self.checkEqual(self.seq.squares()[0], [1,2,3,4,5,6,7,8,9]):
            raise Exception

        for i, val in enumerate(range(0,9)):
            self.seq[int(3 + i/3)][int(3 + i%3)] = i + 10

        if not self.checkEqual(self.seq.squares()[4], [10,11,12,13,14,15,16,17,18]):
            raise Exception
