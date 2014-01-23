import constants as c

class Pattern(list):
    def __init__(self, values = None):
        if values is None:
            values = [False] * c.Size * c.Size

        list.__init__(self, values)

    def set_board(self, board):
        for i, val in enumerate(self):
            if not val:
                board.set(i, 0)

        return board

    @staticmethod
    def random_difficulty():
        import random
        blocks = []

        blocks.append(lambda i: i % 2 == 0)
        blocks.append(lambda i: i % 2 == 0)
#        blocks.append(lambda i: random.choice(range(0, 4)) == 0)
#        blocks.append(lambda i: random.choice(range(0, 3)) == 1)
#        blocks.append(lambda i: i % 3 == 0 and (i/9) % 3 != 1 or 1 % 5 == 1)

        block = random.choice(blocks)

        arr = [None] * c.Size * c.Size
        for i, val in enumerate(arr):
            print(block(i))
            arr[i] = block(i)

        return Pattern(arr)
    
