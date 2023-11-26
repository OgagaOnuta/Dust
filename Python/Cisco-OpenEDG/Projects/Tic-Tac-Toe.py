'''
Create a TIC-TAC-TOE Game
'''

from random import randrange

# Create board
board = [["" for y in range(3)] for x in range(3)]

# Initialize row element
field = 1

# Initialize computer and user's move
comp_move = "X"
user_move = "O"

# Populate fields
for row in range(len(board)):
	for col in range(len(board[row])):
		board[row][col] = field
		field += 1

# Computer's first move
board[1][1] = comp_move


def display_board(board):
	# The function accepts one parameter containing the board's current status
	# and prints it out to the console.
	border = "+-------+-------+-------+"
	cell = "|       |       |       |"
	print("{0}\n{1}".format(border, cell))
	print("|   {}   |   {}   |   {}   |".format(board[0][0], 
											 	board[0][1], 
											 	board[0][2]))
	print("{1}\n{0}\n{1}".format(border, cell))
	print("|   {}   |   {}   |   {}   |".format(board[1][0], 
											 	board[1][1], 
											 	board[1][2]))
	print("{1}\n{0}\n{1}".format(border, cell))
	print("|   {}   |   {}   |   {}   |".format(board[2][0], 
											 	board[2][1], 
											 	board[2][2]))
	print("{1}\n{0}".format(border, cell))


def enter_move(board):
	# The function accepts the board's current status, asks the user about their move,
	# checks the input, and updates the board according to the user's decision.

	try:
		# Get user entry
		user_entry = int(input("Enter your move: "))
						# Check user entry
		if ((user_entry <= 0) or (user_entry >= 10)
			or (type(user_entry) is not int)):
			print("\nENTER FIELD NOT OCCUPIED\n")

		# Update board
		for row in range(len(board)):
			for col in range(len(board[row])):
				if (board[row][col] == user_entry):
					board[row][col] = user_move
					return (True)
	except (ValueError):
		print("\nENTER NUMBER BETWEEN 1 AND 9\n")
		return (False)


def make_list_of_free_fields(board):
	# The function browses the board and builds a list of all the free squares;
	# the list consists of tuples, while each tuple is a pair of row and column numbers.

	# Make free fields a global variable
	global free_fields

	# Create empty list to hold free fields
	free_fields = []

	for row in range(len(board)):
		for col in range(len(board[row])):
			if (type(board[row][col]) is int):
				field_tuple = (row, col)
				free_fields.append(field_tuple)


def victory_for(board, sign):
	# The function analyses the board's status in order to check if
	# the player using 'O's or 'X's has won the game
	if ((board[0][0] == sign) and (board[0][1] == sign)
	 	and (board[0][2] == sign)):
		return (True)
	elif ((board[1][0] == sign) and (board[1][1] == sign)
		and (board[1][2] == sign)):
		return (True)
	elif ((board[2][0] == sign) and (board[2][1] == sign)
	   	and	(board[2][2] == sign)):
		return (True)
	elif ((board[0][0] == sign) and (board[1][0] == sign)
	   	and (board[2][0] == sign)):
		return (True)
	elif ((board[0][1] == sign) and (board[1][1] == sign)
	   	and (board[2][1] == sign)):
		return (True)
	elif ((board[0][2] == sign) and (board[1][2] == sign)
	   	and (board[2][2] == sign)):
		return (True)
	elif ((board[0][0] == sign) and (board[1][1] == sign)
	   	and (board[2][2] == sign)):
		return (True)
	elif ((board[0][2] == sign) and (board[1][1] == sign)
	   	and (board[2][0] == sign)):
		return (True)
	else:
		return (False)


def draw_move(board):
	# The function draws the computer's move and updates the board

	while (True):
		# Draw computer move
		comp_entry = randrange(1, 9)
		empty = False

		# Check if field is empty
		for row in board:
			if (comp_entry in row):
				empty = True
				break

		if (empty == True):
			# Update board
			for row in range(len(board)):
				for col in range(len(board[row])):
					if (board[row][col] == comp_entry):
						board[row][col] = comp_move

			break


while (True):
	display_board(board)
	if (enter_move(board)):
		display_board(board)
		draw_move(board)
	if (victory_for(board, "O")):
		print("You won!")
		break
	elif (victory_for(board, "X")):
		print("Computer wins!")
		break
	else:
		make_list_of_free_fields(board)
		if (len(free_fields) <= 1):
			print("IT'S A TIE")
			break
