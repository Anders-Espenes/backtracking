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

from time import perf_counter_ns
SIZE = 9
EMPTY = 0
# Note Grid is declared as a global variable here
board = [[0 for x in range(SIZE)]for y in range(SIZE)]

# Sudoku problem to solve
board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
         [5, 2, 0, 0, 0, 0, 0, 0, 0],
         [0, 8, 7, 0, 0, 0, 0, 3, 1],
         [0, 0, 3, 0, 1, 0, 0, 8, 0],
         [9, 0, 0, 8, 6, 3, 0, 0, 5],
         [0, 5, 0, 0, 9, 0, 6, 0, 0],
         [1, 3, 0, 0, 0, 0, 2, 5, 0],
         [0, 0, 0, 0, 0, 0, 0, 7, 4],
         [0, 0, 5, 2, 0, 6, 3, 0, 0]]

# Check if board is finished
def check_board():
    for i in range(0, SIZE):
        for j in range(0, SIZE):
            if(board[i][j] == 0):
                return False
    return True

# Check axis for same value
def check_axis(row, column):
    for i in range (0, SIZE):
        if(board[row][column] == board[i][column] or # Check if value is found on the row
        board[row][column] == board[row][i]):   # Check if value is found on column
            return False
        else: return True

# Checks if 
def check_box(row, column):
    for i in range(0, 3):
        for j in range(0, 3):
            if(board[i + (row - row % 3)][j + (column - column % 3)] == 
            board[row][column]):
                return True
    return False
    

# Check if number is allowed
def promising(row, column):
    # TODO: This is true and exits the recursion
    # TODO: Change solution to preemtivly check
    if(board[row][column] == EMPTY): # Check if cell is empty
        for i in range(1, SIZE + 1): # Try for values 1-9
            if(check_axis(row, column) and check_box(row, column)): # Check value along axis and box
                board[row][column] = i # Update
                return True
    return False # No input is valid

def solve_sudoku(row, column):
    if(promising(row, column)): # Check if cell can recieve value
        if(check_board()):
            return True
        else:
            for i in range(0, SIZE): 
                for j in range(0, SIZE):
                    solve_sudoku(i, j)    

if __name__ == "__main__":
    # Start a timer
    start_time = perf_counter_ns()

    # Solve the sudoku
    if(solve_sudoku(0, 0)):
        print(board)
    else:
        print(board)
        print("No Solution exists")
    time = perf_counter_ns() - start_time
    print("Time: ", time, "nano second")
