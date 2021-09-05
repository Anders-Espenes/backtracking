# Problem 2 Knight movement backtracking solver
import random
from typing import List
from heapq import heappush, heappop


class KnightsBacktracking:
	def __init__(self, size: int):
		self.size: int = size
		self.nr_visited = 0
		self.nr_promising = 0

	def promising(self, x: int, y: int, board: List[List[int]]) -> bool:
		self.nr_promising += 1
		if 0 <= x < self.size and 0 <= y < self.size:  # To make sure we are not moving outside the board
			if board[x][y] == -1:  # Checks if cell is visited
				return True
		return False

	def knights_backtracking(self, board: List[List[int]], x: int, y: int, step: int = 1) -> bool:
		self.nr_visited += 1
		# When nr of steps is size * size all cells should be visited
		# We then have to return True here, since it will otherwise return
		# False and backtrack since there are no more legal moves left
		if step == self.size ** 2:
			self._print_result(board)
			return True

		# Loops though all the x, y pos a knight can legally do
		for (x_move, y_move) in zip([2, 1, -1, -2, -2, -1, 1, 2], [1, 2, 2, 1, -1, -2, -2, -1]):
			next_x = x + x_move
			next_y = y + y_move

			if self.promising(next_x, next_y, board):
				board[next_x][next_y] = step
				if self.knights_backtracking(board, next_x, next_y, step + 1):
					return True
				# This is the back tracking part. When a recursively called knights has no legal moves it will
				# return false and the move will be reversed, it will then try the next promising move
				board[next_x][next_y] = -1

		# Indicates that there are no legal moved from this position
		return False

	def _print_result(self, board: list[list[int]]):
		for x in board:
			print(x)
		print(f"\tnumber of promising nodes checked: {self.nr_promising}")
		print(f"\tnumber of visited nodes checked: {self.nr_visited}")


def start_knights_tour_backtracking(n: int):
	# Creates 2d list of 0's with the size n*n
	board = [[-1 for x in range(n)] for y in range(n)]

	# Defines a starting positions and marks it as visited with 0
	start_x = 0
	start_y = 0
	board[start_x][start_y] = 0

	knights = KnightsBacktracking(n)
	knights.knights_backtracking(board, start_x, start_y)


class KnightsHeuristic:
	def __init__(self, size: int):
		self.size: int = size
		self.nr_visited = 0
		self.nr_promising = 0
		self.x_moves = [2, 1, -1, -2, -2, -1, 1, 2]
		self.y_moves = [1, 2, 2, 1, -1, -2, -2, -1]
		self.n = 8  # Max number of legal moves a knight can make

	def promising(self, board: list[list[int]], x: int, y: int):
		self.nr_promising += 1
		if 0 <= x < self.size and 0 <= y < self.size:  # To make sure we are not moving outside the board
			if board[x][y] == -1:  # Checks if cell is visited
				return True
		return False

	def count_neighbors(self, board: list[list[int]], x: int, y: int):
		count = 1
		for (x_move, y_move) in zip(self.x_moves, self.y_moves):
			next_x = x + x_move
			next_y = y + y_move
			if self.promising(board, next_x, next_y):
				count += 1

		return count

	def knights_heuristic(self, board: List[List[int]], x: int, y: int, step: int = 1) -> bool:
		self.nr_visited += 1

		board[x][y] = step

		# When the last step is placed we know there is no reason to check neighbors, so we return early
		if step == self.size ** 2:
			self._print_result(board)
			return True

		priority_queue = []
		# Loops though all the x, y pos a knight can legally do
		for (x_move, y_move) in zip(self.x_moves, self.y_moves):
			next_x = x + x_move
			next_y = y + y_move
			if self.promising(board, next_x, next_y):
				# count the nr of promising nodes from this pos
				count = self.count_neighbors(board, next_x, next_y)
				if count > 0:
					heappush(priority_queue, (count, next_x, next_y))

		if len(priority_queue) > 0:
			# pops the first element in pq and uses that pos for next move
			(count, next_x, next_y) = heappop(priority_queue)
			if self.knights_heuristic(board, next_x, next_y, step + 1):
				return True


	def _print_result(self, board: list[list[int]]):
		for x in board:
			print(x)
		print(f"\tnumber of promising nodes checked: {self.nr_promising}")
		print(f"\tnumber of visited nodes checked: {self.nr_visited}")


def start_knights_tour_heuristic(n: int):
	# Creates 2d list of 0's with the size n*n
	board = [[-1 for x in range(n)] for y in range(n)]

	random.seed(234234)

	# Defines a starting positions and marks it as visited with 0
	start_x = random.randrange(0, n)
	start_y = random.randrange(0, n)

	knights = KnightsHeuristic(n)
	knights.knights_heuristic(board, start_x, start_y)



if __name__ == "__main__":
	# start_knights_tour_backtracking(8)
	start_knights_tour_heuristic(8)

