import sys
sys.path.append('../')

import generator
import unittest

class GeneratorTest(unittest.TestCase):
    def setUp(self):
        self.seq = generator.Generator()

    def test_should_generate_valid_board(self):
        expected = True
        board = self.seq.generate()
        board.show()
        received = board.is_valid()

        if(expected != received):
            raise Exception('Expected True. The receveid value was ' + str(received))

        
