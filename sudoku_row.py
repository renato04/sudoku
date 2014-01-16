class SudokuRow(list):
    def __init__(self, size):
        list.__init__(self, [0] * size)

    def is_repeated(self):
        for i, val in enumerate(self):
            if self.count(i + 1) > 1:
                return True
        return False

    def is_valid(self):
        if self.is_repeated():
            return False

        validos = range(1,9)
        for i, val in enumerate(self):
            if i not in validos:
                return False
        return True   
