import constants as c
import sudoku_row

class Board:

    def __init__(self):
        self.matrix = [sudoku_row.SudokuRow(c.c.Size) for x in range(c.c.Size)]

    def __getitem__(self, key):
        return self.matrix[key]

    def lines(self):
        return self.matrix

    def columns(self):
        return zip(*self.matrix)

    def all_values(self):
        return [cell for cell in row for row in matrix]

    def get(self, index):
        all_values[index]

    def set(self, index, value):
        line = index / c.Size
        col = index % c.Size
        self.matrix[line][col] = value

    def get_peers(self, index):
        line = index / c.Size
        col = index % c.Size
        square = line / Sqrt * Sqrt + col / Sqrt

        p = []
        [p.append(cell) for cell in self.lines[line]]
        [p.append(cell) for cell in self.columns[col]]
        [p.append(cell) for cell in self.squares[square]]

        p = [item for item in set(p) if item in range(1,c.Size)]
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
        for line in lines:
            if not line.is_valid():
                return False

        for colunm in colunms:
            if not colunm.is_valid():
                return False

        for square in squares:
            if not square.is_valid():
                return False

        return True

    def is_possible(self):
        for line in lines:
            if not line.is_repeated():
                return False

        for colunm in colunms:
            if not colunm.is_repeated():
                return False

        for square in squares:
            if not square.is_repeated():
                return False

        return True

    def squares(self):
        squares = []

        for i, val in range(0, c.Size):
            l = i/Sqrt * Sqrt
            m = (i % Sqrt) * Sqrt
            r = range(m + 2)

            squares.append(sudoku_row.SudokuRow(self.matrix[l][r] +
                                                self.matrix[l + 1][r] +
                                                self.matrix[l + 2][r]))
        return squares

    def show(self):
        [print(line) for line in lines]

        
                           
        
                        
                     
            
        
    
        
