import constants as c
import sudoku_row

class Board:

    def __init__(self, matrix = None):
        if matrix is None:
            matrix = [sudoku_row.SudokuRow(c.Size) for x in range(c.Size)]
        else:
            matrix = [sudoku_row.SudokuRow(c.Size, row) for row in matrix]
            
        self.matrix = matrix  

    def __getitem__(self, key):
        return self.matrix[key]

    def lines(self):
        return self.matrix

    def columns(self):
        return [sudoku_row.SudokuRow(c.Size, item) for item in zip(*self.matrix)]

    def all_values(self):
        return [cell for cellsList in self.matrix for cell in cellsList]

    def get(self, index):
        return self.all_values()[index]

    def set(self, index, value):
        from math import floor
        line = floor(index / c.Size)
        col = index % c.Size
        self.matrix[line][col] = value

    def get_peers(self, index):
        from math import floor
        line = floor(index / c.Size)
        col = index % c.Size
        square = floor(line / c.Sqrt) * c.Sqrt + floor(col / c.Sqrt)

        p = []
       
        for cell in self.lines()[int(line)]:
            p.append(cell)

        for cell in self.columns()[col]:
            p.append(cell)

        for cell in self.squares()[int(square)]:
            p.append(cell)            

        p = [item for item in set(p) if item in range(1, c.Size + 1)]

        p.sort()

        return p

    def swap_lines(self, a, b):
        lines[a], lines[b] = lines[b], lines[a]

    def fill_valid(self):
        for i, val in enumarate(range(0, c.Size)):
            for j, val in enumarate(range(0, c.Size)):
                self.matrix[i][j] = (i + j) % c.Size + 1

        self.swap_lines(1,3)
        self.swap_lines(2,6)
        self.swap_lines(5,7)

    def is_valid(self):
        for line in self.lines():
            if not line.is_valid():
                return False
        
        for colunm in self.columns():
            if not colunm.is_valid():
                return False

        for square in self.squares():
            if not square.is_valid():
                return False

        return True

    def is_possible(self):
        for line in self.lines():
            if line.is_repeated():
                return False
            
        for colunm in self.columns():
            if colunm.is_repeated():
                return False

        for square in self.squares():
            if square.is_repeated():
                return False

        return True

    def squares(self):
        squares = []
        from math import floor
        for i, val in enumerate(range(0, c.Size)):
            l = floor(i/c.Sqrt) * c.Sqrt
            m = (i % c.Sqrt) * c.Sqrt
                   
            squares.append(sudoku_row.SudokuRow(c.Size,
                                                self.matrix[int(l)][m:m+3] +
                                                self.matrix[int(l) + 1][m:m+3] +
                                                self.matrix[int(l) + 2][m:m+3]))
        
        return squares

    def show(self):
        [print(line) for line in self.lines()]
