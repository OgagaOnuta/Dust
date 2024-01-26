'''
Sudoku (checks if the Sudoku is valid)

TEST DATA:
Yes - 2 9 5 7 4 3 8 6 1
	  4 3 1 8 6 5 9 2 7
	  8 7 6 1 9 2 5 4 3
	  3 8 7 4 5 9 2 1 6
	  6 1 2 3 8 7 4 9 5
	  5 4 9 2 1 6 7 3 8
	  7 6 3 5 2 4 1 8 9
	  9 2 8 6 7 1 3 5 4
	  1 5 4 9 3 8 6 7 2

No - 1 9 5 7 4 3 8 6 2
	 4 3 1 8 6 5 9 2 7
	 8 7 6 1 9 2 5 4 3
	 3 8 7 4 5 9 2 1 6
	 6 1 2 3 8 7 4 9 5
	 5 4 9 2 1 6 7 3 8
	 7 6 3 5 2 4 1 8 9
	 9 2 8 6 7 1 3 5 4
	 2 5 4 9 3 8 6 7 1
'''

# Create a 9x9 grid
sudoku = [["" for x in range(9)] for y in range(9)]

for row in sudoku:
	row.clear()
	numbers_in_cell = input("Enter numbers in row separated by spaces: ").split()
	for number in numbers_in_cell:
		row.append(number)

print()
for row in sudoku:
	print(row)


# Create checker function
def checker(chklist):
	# Sort list
	chklisted = sorted(chklist)
	length = len(chklisted)

	# Iterate through sorted list comparing adjacent elements
	for i in range(length - 1):
		# If elements are the same, return TRUE
		if (chklisted[i] == chklisted[i + 1]):
			return (True)


# Create valid function
def valid(puzzle):
	verdict = True

	# Iterate through each row, and implement checker function
	print()
	for row in puzzle:
		print("row", row)
		if (checker(row) == True):
			verdict = False

	# Iterate through each column, and implement checker function
	print()
	column = []
	for col in range(9):
		for row in puzzle:
			column.append(row[col])
		
		print("column", column)
		if (checker(column) == True):
			verdict = False

		column.clear()
			
	# Iterate through each 3x3 grid, and implement checker function

	# Sudoku Matrix (row_column)
	# [00, 01, 02, 03, 04, 05, 06, 07, 08]
	# [10, 11, 12, 13, 14, 15, 16, 17, 18]
	# [20, 21, 22, 23, 24, 25, 26, 27, 28]
	# [30, 31, 32, 33, 34, 35, 36, 37, 38]
	# [40, 41, 42, 43, 44, 45, 46, 47, 48]
	# [50, 51, 52, 53, 54, 55, 56, 57, 58]
	# [60, 61, 62, 63, 64, 65, 66, 67, 68]
	# [70, 71, 72, 73, 74, 75, 76, 77, 78]
	# [80, 81, 82, 83, 84, 85, 86, 87, 88]

	print()
	grid = []
	for row in range(0, 9, 3):
		for col in range(0, 9, 3):
			grid.append(puzzle[row][col])
			grid.append(puzzle[row][col + 1])
			grid.append(puzzle[row][col + 2])
			grid.append(puzzle[row + 1][col])
			grid.append(puzzle[row + 1][col + 1])
			grid.append(puzzle[row + 1][col + 2])
			grid.append(puzzle[row + 2][col])
			grid.append(puzzle[row + 2][col + 1])
			grid.append(puzzle[row + 2][col + 2])

			print("grid: ", grid)
			if (checker(grid) == True):
				verdict = False

			grid.clear()

	# print()
	# grid, row = [], 0
	# while (row < 9):
	# 	col = 0
	# 	while (col < 9):
	# 		grid.append(puzzle[row][col])
	# 		grid.append(puzzle[row][col + 1])
	# 		grid.append(puzzle[row][col + 2])
	# 		grid.append(puzzle[row + 1][col])
	# 		grid.append(puzzle[row + 1][col + 1])
	# 		grid.append(puzzle[row + 1][col + 2])
	# 		grid.append(puzzle[row + 2][col])
	# 		grid.append(puzzle[row + 2][col + 1])
	# 		grid.append(puzzle[row + 2][col + 2])

	# 		print("grid: ", grid)
	# 		if (checker(grid) == True):
	# 			verdict = False

	# 		grid.clear()
	# 		col += 3

	# 	row += 3

	print()
	# Check verdict
	if (verdict == True):
		return ("Yes")
	else:
		return ("No")


print(valid(sudoku))
