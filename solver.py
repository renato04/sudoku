import board
import timeit as time
import constants as c

class Solver:

    Solver.fixed = 'f'
    Solver.selected = 's'
    Solver.exhasuted = 'e'
    Solver.new = 'n'

    def __init__(self):
        self.by_step = False
        self.limit = 40000

    def solve(self, board):
        if board.is_valid():
            return board

        initialize_vars(board)
        self.goal = lambda solver : solver.exhausted or solver.board.is_valid()

        start = time.time()
        if not board.is_possible():
            self.exhausted = True

        step()
        end = time.time()

        print('Sudoku board solved in ' + str(end - start))

        if self.exhausted:
            return board_impossible()
        else
            return board

    def count_solutions(self, board, maximum = 100):
        if board.is_valid():
            return 1

        initialize_vars(board)
        self.goal = lambda solver : solver.exhausted or solver.solutions >= maximum

        start = time.time()
        if not board.is_possible():
            self.exhausted = True

        step()
        end = time.time()

        print('Sudoku board solved in ' + str(end - start))
        clean_board()
        return self.solutions

    def step(self, steps = 1):

        while not reached_goal():
            self.total_steps += 1

            if reached_limit()
                break

            decide_square()

            if done_steps()
                return steps

    def initializa_vars(self, board):
        self.board = board
        self.index = -1
        self.exhausted = false
        self.option_tree = generate_options()
        self.step_count = 0
        self.total_steps = 0
        self.solutions = 0

        next_empty_square()

    def reached_goal(self):
        return self.goal(self)

    def decide_square(self):
        option = self.get_option()

        if option is not None:
            backtrack()
        elif:
            set_square(option)
            check_solution()

            if self.board.is_possible():
                next_square()
            else:
                exhaust_option(self.index)

    def backtrack(self):
        last_index = self.index

        if previous_editable_square():
            exhaust_option(last_index)
            empty_square_last_index()
        else:
            no_more_options()

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
        for i, val in enumerate(a):
            if self.board.get(i) in c.Numbers:
                return Solver.Fixed
            else:
                return [Solver.new] * c.Size

    def get_option(self):
        options = self.option_tree[self.index]
        if not type(options) is list
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
        if self.total_steps > self.limit
            self.exhausted = True
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
        self.option_tree[index] == Solver.fixed

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

        found = (self.index < c.Squares and not is_fixed(self.index))

        if self.index > c.Squares - 1:
            self.index = c.Squares - 1

        return found

    def previous_editable_square(self):
        self.index -= 1
        while self.is_fixed(self.index)
            self.index -= 1

        return (self.index >= 0 and not self.is_fixed(self.index))

    def no_more_options(self):
        self.exhausted = True
        print('exhausted in' + str(self.total_steps) + ' tries')

    def clean_board(self):
        for i, v in c.Squares:
            if not self.is_fixed(i):
                self.board.set(i,0)
        
        
                
        
    

    
        
        
        
    
