# Problem 2 Knight movement backtracking solver
from typing import List

# Global vars for counting the number of visited node and promising nodes checked
nr_promising = 0
nr_visited = 0


def promising(x: int, y: int, board: List[List[int]], size: int) -> bool:
	global nr_promising
	nr_promising += 1
	if 0 <= x < size and 0 <= y < size:  # To make sure we are not moving outside the board
		if board[x][y] == -1:  			 # Checks if cell is visited
			return True
	return False


def knights(board: List[List[int]], x: int, y: int, size: int, step: int = 1) -> bool:
	global nr_visited
	nr_visited += 1
	# When nr of steps is size * size all cells should be visited
	# We then have to return True here, since it will otherwise return
	# False and backtrack since there are no more legal moves left
	if step == size**2:
		return True

	# Loops though all the x, y pos a knight can do from a cell
	for (x_move, y_move) in zip([2, 1, -1, -2, -2, -1, 1, 2], [1, 2, 2, 1, -1, -2, -2, -1]):
		next_x = x + x_move
		next_y = y + y_move

		if promising(next_x, next_y, board, size):
			board[next_x][next_y] = step
			if knights(board, next_x, next_y, size, step + 1):
				return True
			# This is the back tracking part. When a recursively called knights has no legal moves it will
			# return false and the move will be reversed, it will then try the next promising move
			board[next_x][next_y] = -1

	# Indicates that there are no legal moved from this position
	return False


def main(n: int):
	# Creates 2d list of 0's with the size n*n
	board = [[-1 for x in range(n)] for y in range(n)]

	start_x = 0
	start_y = 0

	#
	board[start_x][start_y] = 0

	if knights(board, start_x, start_y, size=n):
		for x in board:
			print(x)
		print(f"number of promising nodes checked: {nr_promising}")
		print(f"number of visited nodes checked: {nr_visited}")


if __name__ == "__main__":
	main(5)
