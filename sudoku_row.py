class SudokuRow(list):
    def __init__(self, size = 0, values = None):
        if values is None:
            list.__init__(self, [0] * size)
        else:
            list.__init__(self, values)

           

    def is_repeated(self):
        for i, val in enumerate(self):
            if self.count(i + 1) > 1:
                return True
        return False

    def is_valid(self):
        if self.is_repeated():
            return False

        validos = range(1,10)
        for i, val in enumerate(self):
            if val not in validos:
                return False
        return True   
