# Problem 3 Magnets placement solver
# Print solution
def print_solution(board):
    print(f'Visited {visited}')
    print(f'Promising {promising}')
    for i in range(M):
        for j in range(N):
            print(board[i][j], end=' ')
        print()


# Counts total number of characters in the column
def count_ch_columns(board, ch, j):
    count = 0
    for i in range(M):
        if board[i][j] == ch:
            count = count + 1
    return count


# Counts total number of characters in the row
def count_ch_row(board, ch, i):
    count = 0
    for j in range(N):
        if board[i][j] == ch:
            count = count + 1
    return count


# Check if its safe to put the character in the cell
def is_safe(board, row, col, ch, top, left, bottom, right):
    # checks for adjacent cells
    if ((row - 1 >= 0 and board[row - 1][col] == ch) or
            (col + 1 < N and board[row][col + 1] == ch) or
            (row + 1 < M and board[row + 1][col] == ch) or
            (col - 1 >= 0 and board[row][col - 1] == ch)):
        return False

    rowCount = count_ch_row(board, ch, row)

    colCount = count_ch_columns(board, ch, col)

    # if character is +, check `top[]` and `left[]`
    if ch == '+':

        # check top
        if top[col] != -1 and colCount >= top[col]:
            return False

        # check left
        if left[row] != -1 and rowCount >= left[row]:
            return False

    # if the given character is `-`, check `bottom[]` and `right[]`
    if ch == '-':

        # check bottom
        if bottom[col] != -1 and colCount >= bottom[col]:
            return False

        # check left
        if right[row] != -1 and rowCount >= right[row]:
            return False

    return True


# Function to validate the configuration of the board
def validate_configuration(board, top, left, bottom, right, solutions):
    # check top
    for i in range(N):
        if top[i] != -1 and count_ch_columns(board, '+', i) != top[i]:
            return False

    # check left
    for j in range(M):
        if left[j] != -1 and count_ch_row(board, '+', j) != left[j]:
            return False

    # check bottom
    for i in range(N):
        if bottom[i] != -1 and count_ch_columns(board, '-', i) != bottom[i]:
            return False

    # check right
    for j in range(M):
        if right[j] != -1 and count_ch_row(board, '-', j) != right[j]:
            return False

    for solution in solutions:
        count = 0
        for i in range(M):
            for j in range(N):
                if solution[i][j] == board[i][j]:
                    count += 1
                    if count == M*N:
                        return False

    solutions.append(board)
    print_solution(board)
    return True


# Function to solve
def solve_puzzle(board, row, col, top, left, bottom, right, rules, solutions):
    global visited
    global promising
    promising += 1
    # checks if the last cell has been reached and try to validate
    if row >= M - 1 and col >= N - 1:
        validate_configuration(board, top, left, bottom, right, solutions)
        return

    # Checks if its the end of the row and jumps to the next one
    if col >= N:
        col = 0
        row = row + 1

    # if the current cell contains `R` or `B` recur for the next cell
    #
    if rules[row][col] == 'R' or rules[row][col] == 'B':

        if solve_puzzle(board, row, col + 1, top, left, bottom, right, rules, solutions):
            return True

    # if a horizontal slot contains `L` and `R`
    if rules[row][col] == 'L' and rules[row][col + 1] == 'R':

        # put (`+`, `-`) pair and recur
        if (is_safe(board, row, col, '+', top, left, bottom, right) and
                is_safe(board, row, col + 1, '-', top, left, bottom, right)):
            visited += 1
            board[row][col] = '+'
            board[row][col + 1] = '-'

            if solve_puzzle(board, row, col + 2, top, left, bottom, right, rules, solutions):
                return True

            # backtrack if it doesnt reach a solution
            board[row][col] = 'X'
            board[row][col + 1] = 'X'

        # put (`-`, `+`) pair and recur
        if (is_safe(board, row, col, '-', top, left, bottom, right) and
                is_safe(board, row, col + 1, '+', top, left, bottom, right)):
            visited += 1
            board[row][col] = '-'
            board[row][col + 1] = '+'

            if solve_puzzle(board, row, col + 2, top, left, bottom, right, rules, solutions):
                return True

            # backtrack if it doesnt reach a solution
            board[row][col] = 'X'
            board[row][col + 1] = 'X'

    # if a vertical slot contains `T` and `B`
    if rules[row][col] == 'T' and rules[row + 1][col] == 'B':

        # put (`+`, `-`) pair and recur
        if (is_safe(board, row, col, '+', top, left, bottom, right) and
                is_safe(board, row + 1, col, '-', top, left, bottom, right)):
            visited += 1
            board[row][col] = '+'
            board[row + 1][col] = '-'

            if solve_puzzle(board, row, col + 1, top, left, bottom, right, rules, solutions):
                return True

            # backtrack if it doesnt reach a solution
            board[row][col] = 'X'
            board[row + 1][col] = 'X'

        # put (`-`, `+`) pair and recur
        if (is_safe(board, row, col, '-', top, left, bottom, right) and
                is_safe(board, row + 1, col, '+', top, left, bottom, right)):
            visited += 1
            board[row][col] = '-'
            board[row + 1][col] = '+'

            if solve_puzzle(board, row, col + 1, top, left, bottom, right, rules, solutions):
                return True

            # backtrack if it doesnt reach a solution
            board[row][col] = 'X'
            board[row + 1][col] = 'X'

    # no solutions found for this cell, move on
    if solve_puzzle(board, row, col + 1, top, left, bottom, right, rules, solutions):
        return True

    # return if there are no possible solutions
    return


def magnet_puzzle(top, left, bottom, right, rules):
    # initialize all cells with `X`
    board = [['X' for x in range(N)] for y in range(M)]
    solutions = []

    # start at (0, 0)
    if not solve_puzzle(board, 0, 0, top, left, bottom, right, rules, solutions):
        print("No more possible solutions")
        return


visited = 0
promising = 0
top = [ 1, -1, -1, 2, 1, -1 ]
bottom = [ 2, -1, -1, 2, -1, 3 ]
left = [ 2, 3, -1, -1, -1 ]
right = [ -1, -1, -1, 1, -1 ]


rules = [["L","R","L","R","T","T" ],
        [ "L","R","L","R","B","B" ],
        [ "T","T","T","T","L","R" ],
        [ "B","B","B","B","T","T" ],
        [ "L","R","L","R","B","B" ]]

(M, N) = (len(rules), len(rules[0]))

magnet_puzzle(top, left, bottom, right, rules)