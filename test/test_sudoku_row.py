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