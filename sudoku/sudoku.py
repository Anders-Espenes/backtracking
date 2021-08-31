# Problem 1 Sudoku Backtracking solver
'''

A  Sudoku  puzzle  consists  of  9  3x3  squares  arranged  as  shown  on  the  next  page.    
Some  squares  are  initialized with numbers from 1 to 9 while others are left blank. 
The objective is to fill all squares with numbers from 1 to 9 such that each number occurs exactly once in each row, each column and each 3x3 square.
1.    Implement a backtracking solution.
2.    Count the number of visited and promising nodes in the search tree.
3.    Implement  some  deductive  strategies  (e.g.  x-wing,  swordfish,  forcing  chain,  etc)  to  reduce  the  search space. 
        How much do they contribute towards making the search for a solution faster?
'''

''' 
Backtracking methodology 
Backtracking is a modified depth-first search of a rooted tree
Root node is visited first, a visit to a node is followed immediately by visits to ALL child nodes
Solves problems a sequence of objects is chosen from a specified set so that the sequence satisfies some criterion.
Identify what is the sequence
Identify what is the set
Identify what is the criterion
    Identify promising nodes
    Identify non promising nodes
    Prune the tree, if a node is nonpromising backtrack as the children are not promising
    


Queens problem
Sequence is the number of n positions in which the queen is placed
The set is n^2 possible positions on the chessboard
The criterion is that no two queens can threaten each other

Sudoku:
    Sequence is the number of positions in which 
'''
# IMPORTS
from time import perf_counter_ns
# GLOBALS
SIZE = 9
EMPTY = 0

# Check axis for same value
def check_axis(board, row, column, value):
    for i in range (0, SIZE):
        if(value == board[i][column] or # Check if value is found on the row
           value== board[row][i]):   # Check if value is found on column
            return False
    return True

# Checks if 
def check_box(board, row, column, value):
    for i in range(0, 3):
        for j in range(0, 3):
            if(board[i + (row - row % 3)][j + (column - column % 3)] == value):
                return False
    return True


def find_zero(board):
    return next(((x, y) for x in range(SIZE) for y in range(SIZE) if board[x][y] == 0), False)

# Check if number is allowed
def promising(board, row, column, value):
    if(check_axis(board, row, column, value) and check_box(board, row, column, value)): # Check value along axis and box
        return True
    return False # No input is valid

def solve_sudoku(board):
    cell = find_zero(board)
    if(cell != False):
        for i in range (1, SIZE + 1):
            if(promising(board, cell[0], cell[1], i)):
                board[cell[0]][cell[1]] = i # Update board
                if(solve_sudoku(board)):
                    return board
                board[cell[0]][cell[1]] = 0 # Reset board
        return False
    return board

def print_board(board):
    for i in range(0, SIZE):
        print(board[i])

if __name__ == "__main__":
    # Sudoku problem to solve
    board = [[0 for x in range(SIZE)]for y in range(SIZE)]
    board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
             [5, 2, 0, 0, 0, 0, 0, 0, 0],
             [0, 8, 7, 0, 0, 0, 0, 3, 1],
             [0, 0, 3, 0, 1, 0, 0, 8, 0],
             [9, 0, 0, 8, 6, 3, 0, 0, 5],
             [0, 5, 0, 0, 9, 0, 6, 0, 0],
             [1, 3, 0, 0, 0, 0, 2, 5, 0],
             [0, 0, 0, 0, 0, 0, 0, 7, 4],
             [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    # Solution of the sudoku
    solution = [[0 for x in range(SIZE)]for y in range(SIZE)]
    solution = [[3, 1, 6, 5, 7, 8, 4, 9, 2],
                [5, 2, 9, 1, 3, 4, 7, 6, 8],
                [4, 8, 7, 6, 2, 9, 5, 3, 1],
                [2, 6, 3, 4, 1, 5, 9, 8, 7],
                [9, 7, 4, 8, 6, 3, 1, 2, 5],
                [8, 5, 1, 7, 9, 2, 6, 4, 3],
                [1, 3, 8, 9, 4, 7, 2, 5, 6],
                [6, 9, 2, 3, 5, 1, 8, 7, 4],
                [7, 4, 5, 2, 8, 6, 3, 1, 9]]
    # Start a timer
    start_time = perf_counter_ns()

    # Solve the sudoku
    board = solve_sudoku(board)
    if(board == solution):
        print_board(board)
    else:
        print_board(board)
        print("No Solution exists")
    time = perf_counter_ns() - start_time
    print("Time: ", time, "nano second")
