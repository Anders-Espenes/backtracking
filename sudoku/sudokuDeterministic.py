# Problem 1 SudokuPuzzle Backtracking solver


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

	def solve_sudoku(self, init_board):
		def backtrack_solver(board):
			self.visited += 1
			cell = self.find_empty(board)
			if cell:
				for i in range(1, self.SIZE + 1):
					self.promisingCounter += 1
					if self.promising(board, cell[0], cell[1], i):
						board[cell[0]][cell[1]] = i  # Update board
						if backtrack_solver(board):
							return board
						board[cell[0]][cell[1]] = 0  # Reset board
				return False
			return board

		# TODO: Solve naked single
		# TODO: Solve X-wing
		# backtrack_solver(init_board, self.populate(init_board))
		backtrack_solver(init_board)
		self.print_board(init_board)

	# Look for possible values that only pair 2 times along the row two times that share colums
	# removes possible values along the columns
	# https://www.youtube.com/watch?v=ZiFPgU4aqGE
	def x_wing_row(self,board, possible_values):
		# Dette er trash, ikke se veldig nøye på det
		for y, col in enumerate(possible_values):
			for x, square in enumerate(col):
				if len(square) > 0:
					for val in square:
						second_val = [0, 0]
						for i in range(x + 1, self.SIZE):
							if val in possible_values[i][y]:
								if second_val == [0, 0]:
									second_val = [i, y]
								else:
									continue
						if second_val != [0, 0]:
							pass


	def print_board(self, board):
		for i in range(0, self.SIZE):
			print(board[i])

		print("Visited: ", self.visited)
		print("Promising: ", self.promisingCounter)


def sudoku():
	# SudokuPuzzle problem to solve
	# sudoku = [[0 for x in range(SIZE)]for y in range(SIZE)]
	sudoku_board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
					[5, 2, 0, 0, 0, 0, 0, 0, 0],
					[0, 8, 7, 0, 0, 0, 0, 3, 1],
					[0, 0, 3, 0, 1, 0, 0, 8, 0],
					[9, 0, 0, 8, 6, 3, 0, 0, 5],
					[0, 5, 0, 0, 9, 0, 6, 0, 0],
					[1, 3, 0, 0, 0, 0, 2, 5, 0],
					[0, 0, 0, 0, 0, 0, 0, 7, 4],
					[0, 0, 5, 2, 0, 6, 3, 0, 0]]


	# Solution of the sudoku
	# solution = [[0 for x in range(SIZE)]for y in range(SIZE)]
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
	sudoku = SudokuPuzzle()

	# possibleValues = sudoku.populate(sudoku_board)
	# sudoku.print_board(possibleValues)

	# sudoku.solve_sudoku(sudoku_board)

	sudoku.x_wing_row(sudoku_board, sudoku.populate(sudoku_board))



if __name__ == "__main__":
	pass
	sudoku()
	# test = [[[1, 1], [2, 2], [3, 3]]]
	# solution = [[[3, 1, 6, 5, 7, 8, 4, 9, 2], [12], [], [], [], [], [], [], [], []]]
	# for x in test:
	# 	print(x[0])
