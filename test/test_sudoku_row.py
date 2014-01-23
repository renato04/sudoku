import sys
sys.path.append('../')

import unittest
import sudoku_row


class SudokuRowTest(unittest.TestCase):

    def setUp(self):
        self.seq = sudoku_row.SudokuRow(9)
        for i, val in enumerate(self.seq):
            self.seq[i] = i + 1
        

    def test_should_not_allow_zero(self):
        self.seq[0]  = 0
        self.assertFalse(self.seq.is_valid())

    def test_should_not_allow_ten(self):
        self.seq[0]  = 10
        self.assertFalse(self.seq.is_valid())

    def test_should_not_allow_repeated_elements(self):
        self.seq[0]  = 1
        self.seq[1]  = 1
        self.assertFalse(self.seq.is_valid())

    def test_should_not_consider_repeated_elements_other_than_one_to_nine(self):
        self.seq[0]  = 0
        self.seq[0]  = 0
        self.assertFalse(self.seq.is_repeated())

    def test_row_should_be_valid(self):
        expected = True
        arr = [1,2,3,4,5,6,7,8,9]
        row = sudoku_row.SudokuRow(9,arr)

        received = row.is_valid()
        if(expected != received):
            raise Exception('Expected True. The receveid value was ' + str(received))          
