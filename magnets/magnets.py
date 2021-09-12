# Write Python3 code here
# Defines the rules of the board
top = [1, -1, -1, 2, 1, -1]
bottom = [2, -1, -1, 2, -1, 3]
left = [2, 3, -1, -1, -1]
right = [-1, -1, -1, 1, -1]

board = [["L", "R", "L", "R", "T", "T"],
         ["L", "R", "L", "R", "B", "B"],
         ["T", "T", "T", "T", "L", "R"],
         ["B", "B", "B", "B", "T", "T"],
         ["L", "R", "L", "R", "B", "B"]]

(M, N) = (len(board), len(board[0]))
visited = 0
promising = 0


# Counts total number of characters in the column
def count_character_columns(board, ch, j):
    count = 0
    for i in range(M):
        if board[i][j] == ch:
            count = count + 1
    return count


# Counts total number of characters in the row
def count_character_row(board, ch, i):
    count = 0
    for j in range(N):
        if board[i][j] == ch:
            count = count + 1
    return count


# Checks that there are no minuses of plusses in the spaces next to the magnet that can be placed.
def horizontal_check(board, row, col, pat):
    if col - 1 >= 0 and board[row][col - 1] == pat[0]:
        return False
    elif row - 1 >= 0 and board[row - 1][col] == pat[0]:
        return False
    elif row - 1 >= 0 and board[row - 1][col + 1] == pat[1]:
        return False
    elif col + 2 < len(board[0]) and board[row][col + 2] == pat[1]:
        return False

    return True


# Checks that there are no minuses of plusses in the spaces next to the magnet that can be placed.
def vertical_check(board, row, col, pat):
    if col - 1 >= 0 and board[row][col - 1] == pat[0]:
        return False
    elif row - 1 >= 0 and board[row - 1][col] == pat[0]:
        return False
    elif col + 1 < len(board[0]) and board[row][col + 1] == pat[0]:
        return False

    return True


def check_rules(board):
    # check top
    for i in range(N):
        if top[i] != -1 and count_character_columns(board, '+', i) != top[i]:
            return False

    # check left
    for j in range(M):
        if left[j] != -1 and count_character_row(board, '+', j) != left[j]:
            return False

    # check bottom
    for i in range(N):
        if bottom[i] != -1 and count_character_columns(board, '-', i) != bottom[i]:
            return False

    # check right
    for j in range(M):
        if right[j] != -1 and count_character_row(board, '-', j) != right[j]:
            return False

    return True


def solve_magnets(board, row, col, promising, visited):
    if row >= M - 1 and col >= N - 1:

        # Check that solution is valid
        if check_rules(board):
            print(f'Promising: {promising}')
            print(f'Visited: {visited}')
            for i in range(M):
                for j in range(N):
                    print(board[i][j], end=' ')
                print()

    elif col >= N:

        solve_magnets(board, row + 1, 0, promising, visited)

    # If not solved or invalid position
    else:
        # If board har value 'L' then its a horizontal piece.
        if board[row][col] == "L":

            visited += 1
            # Check horizontal '+-' placement
            if horizontal_check(board, row, col, "+-"):
                board[row][col] = "+"
                board[row][col + 1] = "-"

                promising += 1
                solve_magnets(board, row, col + 2, promising, visited)

                board[row][col] = "L"
                board[row][col + 1] = "R"

            # Check horizontal '-+' placement
            if horizontal_check(board, row, col, "-+"):
                board[row][col] = "-"
                board[row][col + 1] = "+"

                promising += 1
                solve_magnets(board, row, col + 2, promising, visited)

                board[row][col] = "L"
                board[row][col + 1] = "R"

            # Check horizontal 'xx' placement
            if True or horizontal_check(board, row, col, "xx"):
                board[row][col] = "x"
                board[row][col + 1] = "x"

                promising += 1
                solve_magnets(board, row, col + 2, promising, visited)

                board[row][col] = "L"
                board[row][col + 1] = "R"

        # If board har value 'T' then its a vertical piece.
        elif board[row][col] == "T":
            visited += 1

            # Check vertical '+-' placement
            if vertical_check(board, row, col, "+-"):
                board[row][col] = "+"
                board[row + 1][col] = "-"

                promising += 1
                solve_magnets(board, row, col + 1, promising, visited)

                board[row][col] = "T"
                board[row + 1][col] = "B"

            # Check vertical '-+' placement
            if vertical_check(board, row, col, "-+"):
                board[row][col] = "-"
                board[row + 1][col] = "+"

                promising += 1
                solve_magnets(board, row, col + 1, promising, visited)

                board[row][col] = "T"
                board[row + 1][col] = "B"

            # Check vertical 'xx' placement

            if True or vertical_check(board, row, col, "xx"):
                board[row][col] = "x"
                board[row + 1][col] = "x"

                promising += 1
                solve_magnets(board, row, col + 1, promising, visited)

                board[row][col] = "T"
                board[row + 1][col] = "B"

        else:
            solve_magnets(board, row, col + 1, promising, visited)


# Solve puzzle
solve_magnets(board, 0, 0, visited, promising)
