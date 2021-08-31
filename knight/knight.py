# Problem 2 Knight movement backtracking solver
from typing import List


def print_board(list_y) -> None:
	for list_x in list_y:
		print(list_x)


def promising(board: List[List[int]], x: int, y: int, size: int) -> bool:
	if 0 <= x < size and 0 <= y < size:  # To make sure we are not moving outside the board
		if board[y][x] == 0:  # Checks if cell is visited
			return True
	return False


def knights(board: List[List[int]], x: int, y: int, size: int, step: int):
	# When nr of steps is size * size all cells should be visited
	if step == size * size:
		return True

	# all the x, y pos a knight can do from a cell
	x_moves = [2, 1, -1, -2, -2, -1, 1, 2]
	y_moves = [1, 2, 2, 1, -1, -2, -2, -1]

	for i in range(0, 8):
		next_x = x + x_moves[i]
		next_y = y + y_moves[i]

		if promising(board, next_x, next_y, size):
			board[y][x] = step
			if knights(board, next_x, next_y, size, step + 1):
				return True
			board[y][x] = 0

	# Indicates that there are no legal moved from this position
	return False


def main(n: int):
	# Creates 2d list of 0's with the size n*n
	board = [[x * 0 for x in range(n)] for _ in range(n)]

	if knights(board, 1, 1, n, 1):
		print_board(board)


if __name__ == "__main__":
	main(5)
