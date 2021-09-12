# Problem 1 SudokuPuzzle Backtracking solver
from copy import deepcopy

class SudokuPuzzle:
	def __init__(self):
		self.visited = 0
		self.promisingCounter = 0
		self.SIZE = 9
		self.EMPTY = 0

	# Check axis for same value
	def check_axis(self, board, row, column, value):
		for i in range(0, self.SIZE):
			# Check if value is found on the row than checks for num on column
			if value == board[i][column] or value == board[row][i]:
				return False
		return True

	# Checks if
	def check_box(self, board, row, column, value):
		for i in range(0, 3):
			for j in range(0, 3):
				if board[i + (row - row % 3)][j + (column - column % 3)] == value:
					return False
		return True

	def find_empty(self, board):
		return next(((x, y) for x in range(self.SIZE) for y in range(self.SIZE) if board[x][y] == 0), False)

	# Finds all promising values
	def Find_all_promising(self, board, row, column):
		self.promisingCounter += 1
		possibleValues = []
		for i in range(1, self.SIZE + 1):
			# Check value along axis and box
			if self.check_axis(board, row, column, i) and self.check_box(board, row, column, i):
				possibleValues.append(i)
		return possibleValues

	def promising(self, board, row, column, value):
		self.promisingCounter += 1
		if self.check_axis(board, row, column, value) and self.check_box(board, row, column, value):
				return True
		return False

	# Generate board containing all possible values on empty squares
	def populate(self, board):
		# This is how a filed in board of possible values look
		# [[]          , [1, 9]    , []          , []                , [2, 7]   , []          , []       , [2, 9]   , [2, 7, 9]    ]
		# [[]          , []        , [1, 4, 9]   , [1, 3, 4, 6, 7, 9], [3, 4, 7], [1, 4, 7, 9], [7, 8, 9], [6, 9]   , [6, 7, 8, 9] ]
		# [[4]         , []        , []          , [4, 6, 9]         , [2, 4]   , [2, 4, 9]   , [5, 9]   , []       , []           ]
		# [[2, 4, 6, 7], [4, 6, 7] , []          , [4, 7]            , []       , [2, 4, 5, 7], [7, 9]   , []       , [2, 7, 9]    ]
		# [[]          , [1, 4, 7] , [1, 2, 4]   , []                , []       , []          , [1, 7]   , [1, 2, 4], []           ]
		# [[2, 4, 7, 8], []        , [1, 2, 4, 8], [4, 7]            , []       , [2, 4, 7]   , []       , [1, 2, 4], [2, 3, 7]    ]
		# [[]          , []        , [4, 8, 9]   , [4, 7, 9]         , [4, 7, 8], [4, 7, 9]   , []       , []       , [6, 8, 9]    ]
		# [[2, 6, 8]   , [6, 9]    , [2, 8, 9]   , [1, 3, 9]         , [3, 5, 8], [1, 5, 9]   , [1, 8, 9], []       , []           ]
		# [[4, 7, 8]   , [4, 7, 9] , []          , []                , [4, 7, 8], []          , []       , [1, 9]   , [8, 9]       ]
		possible_values = [[[], [], [], [], [], [], [], [], []],
						  [[], [], [], [], [], [], [], [], []],
						  [[], [], [], [], [], [], [], [], []],
						  [[], [], [], [], [], [], [], [], []],
						  [[], [], [], [], [], [], [], [], []],
						  [[], [], [], [], [], [], [], [], []],
						  [[], [], [], [], [], [], [], [], []],
						  [[], [], [], [], [], [], [], [], []],
						  [[], [], [], [], [], [], [], [], []]]
		zero_squares = [(x, y) for x in range(9) for y in range(9) if board[x][y] == 0]
		for x, y in zero_squares:
			possible_values[x][y] = self.Find_all_promising(board, x, y)
		return possible_values

		# test = [[[], [1, 9], [], [], [2, 7], [], [], [2, 9], [2, 7, 9]],
		# 		[[], [], [1, 4, 9], [1, 3, 4, 6, 7, 9], [3, 4, 7], [1, 4, 7, 9], [7, 8, 9], [6, 9], [6, 7, 8, 9]],
		# 		[[4], [], [], [4, 6, 9], [2, 4], [2, 4, 9], [5, 9], [], []],
		# 		[[2, 4, 6, 7], [4, 6, 7], [], [4, 7], [], [2, 4, 5, 7], [7, 9], [], [2, 7, 9]],
		# 		[[], [1, 4, 7], [1, 2, 4], [3], [], [], [1, 7], [1, 2, 4], []],
		# 		[[2, 4, 7, 8], [], [1, 2, 4, 8], [4, 7], [], [2, 4, 7], [], [1, 2, 4], [2, 3, 7]],
		# 		[[], [], [4, 8, 9], [4, 7, 9], [4, 7, 8], [4, 7, 9], [], [], [6, 8, 9]],
		# 		[[2, 6, 8], [6, 9], [2, 8, 9], [1, 3, 9], [3, 5, 8], [1, 5, 9], [1, 8, 9], [], []],
		# 		[[4, 7, 8], [4, 7, 9], [], [], [4, 7, 8], [], [], [1, 9], [8, 9]]]
		# return test

	def backtrack_solver(self, board, pos_values):
		def next_value(cell):
			for i in cell:
				yield i

		self.visited += 1
		cell = self.find_empty(board)

		if cell:
			for value in next_value(pos_values[cell[0]][cell[1]]):
				if self.promising(board, cell[0], cell[1], value):
					board[cell[0]][cell[1]] = value
					if self.backtrack_solver(board, pos_values):
						return board
					board[cell[0]][cell[1]] = 0

			return False
		return board

	def solve_sudoku(self, init_board, use_x_wing = False, use_single = False):
		def transpose(l1):
			return [[row[i] for row in l1] for i in range(len(l1[0]))]

		self.promisingCounter = 0
		self.visited = 0

		possible_values = self.populate(init_board)
		if use_single:
			self.naked_single(init_board, possible_values)

		if use_x_wing:
			self.x_wing(possible_values)

			trans = transpose(possible_values)
			self.x_wing(trans)
			possible_values = transpose(trans)

		if use_single:
			self.naked_single(init_board, possible_values)

		self.backtrack_solver(init_board, possible_values)
		self.print_board(init_board)

	def naked_single(self, board, possible_values):
		for y, row in enumerate(possible_values):
			for x, cell in enumerate(row):
				if len(cell) == 1:
					board[y][x] = cell[0]

	# Look for possible values that only pair 2 times along the row two times that share colums
	# removes possible values along the columns
	def x_wing(self, possible_values):
		def find_index(l, val):
			indexes = []
			for i, x in enumerate(l):
				if val in x:
					indexes.append((i, x.index(val)))

			return indexes
		def remove_value_col(pos_vals, value, col, row1, row2):
			for i in range(0, self.SIZE):
				if (not (i == row1 or i == row2)) and (value in pos_vals[i][col]):
					# print(f"removing {value}, col {col}, row1 {row1}, row2 {row2}")
					pos_vals[i][col].remove(value)

		for y, row in enumerate(possible_values):
			for i in range(1, self.SIZE + 1):
				val = find_index(row, i)
				if len(val) == 2:
					for row2 in range(y + 1, self.SIZE):
						val2 = find_index(possible_values[row2], i)
						if len(val2) == 2:
							if val[0][0] == val2[0][0] and val[1][0] == val2[1][0]:
								remove_value_col(possible_values, i, val[0][0], y, row2)
								remove_value_col(possible_values, i, val[1][0], y, row2)

	def print_board(self, board):
		solution = [[3, 1, 6, 5, 7, 8, 4, 9, 2],
					[5, 2, 9, 1, 3, 4, 7, 6, 8],
					[4, 8, 7, 6, 2, 9, 5, 3, 1],
					[2, 6, 3, 4, 1, 5, 9, 8, 7],
					[9, 7, 4, 8, 6, 3, 1, 2, 5],
					[8, 5, 1, 7, 9, 2, 6, 4, 3],
					[1, 3, 8, 9, 4, 7, 2, 5, 6],
					[6, 9, 2, 3, 5, 1, 8, 7, 4],
					[7, 4, 5, 2, 8, 6, 3, 1, 9]]
		print(board == solution)

		for i in range(0, self.SIZE):
			print(board[i])
		print("Visited: ", self.visited)
		print("Promising: ", self.promisingCounter)
		print("")


def sudoku():
	# SudokuPuzzle problem to solve
	# sudoku_board = [[0 for x in range(9)]for y in range(9)]
	sudoku_board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
					[5, 2, 0, 0, 0, 0, 0, 0, 0],
					[0, 8, 7, 0, 0, 0, 0, 3, 1],
					[0, 0, 3, 0, 1, 0, 0, 8, 0],
					[9, 0, 0, 8, 6, 3, 0, 0, 5],
					[0, 5, 0, 0, 9, 0, 6, 0, 0],
					[1, 3, 0, 0, 0, 0, 2, 5, 0],
					[0, 0, 0, 0, 0, 0, 0, 7, 4],
					[0, 0, 5, 2, 0, 6, 3, 0, 0]]

	sudoku_board2 = [[0, 0, 4, 3, 0, 2, 6, 5, 9],
					 [0, 0, 0, 6, 4, 7, 0, 0, 0],
					 [0, 0, 0, 0, 0, 5, 0, 0, 4],
					 [0, 2, 0, 0, 3, 0, 8, 4, 7],
					 [0, 0, 3, 4, 0, 8, 2, 9, 6],
					 [9, 4, 8, 2, 7, 6, 5, 1, 3],
					 [1, 3, 0, 0, 0, 4, 0, 0, 5],
					 [4, 0, 0, 0, 0, 3, 0, 6, 0],
					 [2, 0, 5, 7, 0, 0, 4, 3, 0]]

	# Solve the sudoku
	sudokuGame = SudokuPuzzle()
	sudokuGame.solve_sudoku(deepcopy(sudoku_board), False, False)
	sudokuGame.solve_sudoku(deepcopy(sudoku_board), False, True)
	sudokuGame.solve_sudoku(deepcopy(sudoku_board), True, False)
	sudokuGame.solve_sudoku(deepcopy(sudoku_board), True, True)


if __name__ == "__main__":
	sudoku()
