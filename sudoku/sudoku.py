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

from time import perf_counter, perf_counter_ns


def solve_sudoku(board):
    # 1. Loop through every row or column
    # 2. For each cell try a number from 1 to 9
        # Check if each number is allowed, if not iterate and try the next one
    # 3. If number was valid go to next cell.
    #   If no number is valid backtrack the previous cell and iterate the number
    pass

def safe(board):
    # Check if number exists on the horizontal
    # Check if number exists on the vertical
    # Check if number exists in the 3x3 grid containing the cell
    pass
    

if __name__ == "__main__":
    board = [[0 for x in range(9)]for y in range(9)] # Note Grid is declared as a global variable here

    # Sudoku problem to solve
    board =[[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    # Start a timer
    start_time = perf_counter_ns()

    # Solve the sudoku
    if(solve_sudoku(board)):
        print(board)
    else:
        print("No Solution exists")
    time = perf_counter_ns() - start_time
    print("Time: ", time, "nano second")
    