# Problem 1 Sudoku Backtracking solver

# GLOBALS
SIZE = 9
EMPTY = 0

visited = 0
promisingCounter = 0

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
    global visited
    visited += 1
    cell = find_zero(board)
    if(cell != False):
        for i in range (1, SIZE + 1):
            global promisingCounter
            promisingCounter += 1
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

    # Solve the sudoku
    board = solve_sudoku(board)
    if(board == solution):
        print_board(board)
    else:
        print_board(board)
        print("No Solution exists")

    print("Visited: ", visited)
    print("Promising: ", promisingCounter)
