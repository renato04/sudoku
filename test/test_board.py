import sys
sys.path.append('../')

import unittest
import board


class BoardTest(unittest.TestCase):
    
    def setUp(self):
        self.seq = board.Board()

    def should_create_a_matrix(self):
        self.assertIsInstance(type(self.seq), list)
        self.assertIsInstance(type(self.seq[0]), list)

    def test_should_build_correct_squares(self):
        for i, val in enumerate(range(0,9)):
            self.seq[int(i/3)][int(i%3)] = i + 1

         self.assertEqual(self.seq.squares()[0], [1,2,3,4,5,6,7,8,9])

        for i, val in enumerate(range(0,9)):
            self.seq[int(i/3)][int(i%3)] = i + 10

        self.assertEqual(self.seq.squares()[4], [10,11,12,13,14,15,16,17,18])        
        
