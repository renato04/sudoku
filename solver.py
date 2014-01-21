import board
import time as t
import constants as c

class Solver:

    fixed = 'f'
    selected = 's'
    exhausted = 'e'
    new = 'n'

    def __init__(self):
        self.by_step = False
        self.limit = 40000

    def solve(self, board):
        if board.is_valid():
            return board

        self.initialize_vars(board)
        self.goal = lambda solver : solver.done or solver.board.is_valid()

        start = t.time()
        if not board.is_possible():
            self.done = True

        self.step()
        end = t.time()

        print('Sudoku board solved in ' + str(end - start))

        if self.done:
            return board_impossible()
        else:
            return board

    def count_solutions(self, board, maximum = 100):
        if board.is_valid():
            return 1

        print("before")
        board.show()
        self.initialize_vars(board)
        self.goal = lambda solver : solver.done or solver.solutions >= maximum

        start = t.time()
        if not board.is_possible():
            self.done = True

        self.step()
        end = t.time()

        print('Sudoku board solved in ' + str(end - start))
        self.clean_board()
        return self.solutions

    def step(self, steps = 1):
        while not self.reached_goal():
            self.total_steps += 1
            if self.reached_limit():
                break

            self.decide_square()
            if self.is_done_steps(steps):
                return steps

    def initialize_vars(self, board):
        self.board = board
        self.index = -1
        self.done = False
        self.option_tree = self.generate_options()
        self.step_count = 0
        self.total_steps = 0
        self.solutions = 0

        self.next_empty_square()

    def reached_goal(self):
        return self.goal(self)

    def decide_square(self):
        option = self.get_option()

        if option is None:
            self.backtrack()
        else:
            self.set_square(option)
            check_solution()

            if self.board.is_possible():
                next_square()
            else:
                exhaust_option(self.index)

    def backtrack(self):
        last_index = self.index

        if self.previous_editable_square():
            self.exhaust_option(last_index)
            self.empty_square_last_index()
        else:
            self.no_more_options()

    def next_square(self):
        if next_empty_square():
            set_options()

    def set_square(self, value):
        if self.option_tree[self.index] == Solver.fixed:
            return
        self.option_tree[self.index][value -1] = Solver.selected

    def empty_square(self, index):
        if self.option_tree[index] == Solver.fixed:
            return
        self.board.set(index,0)

    def exhaust_option(self, index):
        if self.option_tree[index] == Solver.fixed:
            return
        self.option_tree[self.index][value -1] = Solver.exhausted

    def board_impossible(self):
        print("This sudoku has no solution")

    def generate_options(self):
        a = [0] * c.Squares
        print("generate_options")
        self.board.show()
        for i, val in enumerate(a):
            print("self.board.get(i)")
            print(self.board.get(i))
            if self.board.get(i) in c.Numbers:
                val = Solver.Fixed
            else:
                val = [Solver.new] * c.Size
        return a

    def get_option(self):
        options = self.option_tree[self.index]
        if not type(options) is list:
            return None

        valid_options = []
        for i, val in options:
            if val == Solver.new:
                valid_options.append(i +1)

        if not valid_options:
            return None

        from random import shuffle
        return shuffle(valid_options)[0]

    def set_options(self):
        options = self.option_tree[self.index]

        for i, val in options:
            options[i] = Solver.new
            if (i + 1) in self.board.get_peers(self.index):
                options[i] = Solver.exhausted

    def print_option_state(self):
        for val in self.option_tree:
            print(val.count(Solver.exhausted))

    def check_solution(self):
        if self.board.is_valid():
            self.solutions += 1
            exhaust_solution()

    def reached_limit(self):
        if self.total_steps > self.limit:
            self.done = True
            raise ('Number of tries reached the limit!')
            return True

        return False

    def exhaust_solution(self):
        for opts in self.option_tree:
            if type(opts) is list:
                map(verify_selected, opts)

    def verify_selected(val):
        if val == Solver.selected:
            return Solver.exhausted
        else:
            return val

    def is_fixed(self, index):
        return self.option_tree[index] == Solver.fixed

    def is_done_steps(self, steps):
        if self.by_step:
            self.step_count += 1

            if self.step_count == steps:
                self.step_count = 0
                self.board.show_pretty()
                return True

        return False

    def next_empty_square(self):
        self.index += 1
        while self.is_fixed(self.index) and self.index < c.Squares - 1:
            self.index += 1

        found = (self.index < c.Squares and not self.is_fixed(self.index))

        if self.index > c.Squares - 1:
            self.index = c.Squares - 1

        return found

    def previous_editable_square(self):
        self.index -= 1
        while self.is_fixed(self.index):
            self.index -= 1

        return (self.index >= 0 and not self.is_fixed(self.index))

    def no_more_options(self):
        self.done = True
        print('exhausted in ' + str(self.total_steps) + ' tries')

    def clean_board(self):
        for i, v in enumerate(range(0, c.Squares - 1)):
            if not self.is_fixed(i):
                self.board.set(i,0)
