'''
Creating a chessboard and assigning pieces
'''

# Initializing an empty field on the board
EMPTY = " "

# Creating the board, rows are ranks, columns are files
board = [[EMPTY for files in range(8)] for ranks in range(8)]

# Printing the chessboard
for row in board:
	print(row)

# Assigning pieces at their specified positions
KING = "K"
QUEEN = "Q"
ROOK = "R"
BISHOP = "B"
KNIGHT = "N"
PAWN = "P"

board[0][4] = KING
board[7][4] = KING

board[0][3] = QUEEN
board[7][3] = QUEEN

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

board[0][2] = BISHOP
board[0][5] = BISHOP
board[7][2] = BISHOP
board[7][5] = BISHOP

board[0][1] = KNIGHT
board[0][6] = KNIGHT
board[7][1] = KNIGHT
board[7][6] = KNIGHT

board[1][0] = PAWN
board[1][1] = PAWN
board[1][2] = PAWN
board[1][3] = PAWN
board[1][4] = PAWN
board[1][5] = PAWN
board[1][6] = PAWN
board[1][7] = PAWN
board[6][0] = PAWN
board[6][1] = PAWN
board[6][2] = PAWN
board[6][3] = PAWN
board[6][4] = PAWN
board[6][5] = PAWN
board[6][6] = PAWN
board[6][7] = PAWN

print()
for row in board:
	print(row)
