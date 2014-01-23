import sys
sys.path.append('../')

import unittest
import board


class BoardTest(unittest.TestCase):
    
    def setUp(self):
        self.seq = board.Board()

    def checkEqual(self, L1, L2):
        return len(L1) == len(L2) and sorted(L1) == sorted(L2)

    def test_should_build_correct_squares(self):
        for i, val in enumerate(range(0,9)):
            self.seq[int(i/3)][int(i%3)] = i + 1
            
        if not self.checkEqual(self.seq.squares()[0], [1,2,3,4,5,6,7,8,9]):
            raise Exception

        for i, val in enumerate(range(0,9)):
            self.seq[int(3 + i/3)][int(3 + i%3)] = i + 10

        if not self.checkEqual(self.seq.squares()[4], [10,11,12,13,14,15,16,17,18]):
            raise Exception

    def test_should_build_correct_peers_list(self):
        for i, val in enumerate(range(0,9)):
            self.seq[0][i] = 4
            self.seq[i][0] = 5
            self.seq[int(i/3)][i%3] = 3

        if not self.checkEqual(self.seq.get_peers(0), [3,4,5]):
            raise Exception

        b2 = board.Board()
        b2[1][5] = 9
        b2[4][8] = 8
        b2[3][3] = 1
        b2[6][3] = 2

        if not self.checkEqual(b2.get_peers(41), [1,8,9]):
            raise Exception

    def test_should_be_possible(self):
        expected = True
        
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

        received = b.is_possible()

        if(expected != received):
            raise Exception('Expected True. The receveid value was False')

    def test_first_position_should_be_five(self):
        expected = 5
        
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

        received = b.get(0)

        if(expected != received):
            raise Exception('Expected True. The receveid value was ' + str(received))

    def test_39th_position_should_be_five_after_set_value(self):
        expected = 5
        
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

        b.set(39, expected)

        if(b.all_values()[39] != expected):
            raise Exception('Expected True. The receveid value was ' + str(received))

    def test_full_board_should_be_valid(self):
        expected = True
        
        arr = [
          [5, 9, 1,   8, 4, 7,   6, 2, 3],   
          [4, 2, 3,   6, 9, 1,   7, 5, 8],
          [8, 6, 7,   2, 3, 5,   1, 4, 9],   

          [1, 8, 4,   3, 5, 9,   2, 7, 6],  
          [2, 3, 9,   4, 7, 6,   5, 8, 1],  
          [6, 7, 5,   1, 2, 8,   3, 9, 4], 

          [9, 5, 8,   7, 6, 3,   4, 1, 2],  
          [3, 1, 2,   5, 8, 4,   9, 6, 7], 
          [7, 4, 6,   9, 1, 2,   8, 3, 5]]

        b = board.Board(arr)

        received = b.is_valid()

        if(expected != received):
            raise Exception('Expected True. The receveid value was ' + str(received))

    def test_incomplete_board_should_be_not_valid(self):
        expected = False
        
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

        received = b.is_valid()

        if(expected != received):
            raise Exception('Expected True. The receveid value was ' + str(received))        
    
        

        
        

        
