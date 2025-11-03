import time
import random
import copy

def print_board(board):
	print("   a  b  c  d  e  f  g  h  i  j ")
	for i in range(10):
		if i != 9:
			print(i + 1, end=" ")
		else:
			print(i + 1, end="")
		for j in range(10):
			print("[" + board[i][j] + "]", end="")
		print("")

def print_game_board():
	print("          Your Board              |        Your Guessed Board")
	print("   a  b  c  d  e  f  g  h  i  j   |     a  b  c  d  e  f  g  h  i  j")
	for i in range(10):
		for j in range(0,2):
			if i != 9:
				print(i + 1, end=" ")
			else:
				print(i + 1, end="")
			if j == 0:
				for k in range(10):
					print("[" + board[i][k] + "]", end="")
			else:
				for k in range(10):
					print("[" + guessBoard[i][k] + "]", end="")
			if j == 0:
				print("  |  ", end="")
		print("")

def generate_board():
	for piece in remainingpieces:
		placed = False
		while placed == False:
			position = [random.randint(0,9), random.randint(0,9)]
			if kaiBoard[position[1]][position[0]] != " ":
				continue
			possiblepositions = [[position[0], position[1] + piece[1] - 1], [position[0], position[1] - piece[1] + 1], [position[0] + piece[1] - 1, position[1]], [position[0] - piece[1] + 1, position[1]]]
			for coord in possiblepositions:
				shiplength = 0
				if (coord[0] not in range(0, 10)) or (coord[1] not in range(0, 10)):
					possiblepositions[possiblepositions.index(coord)] = ""
					continue
				if position[0] == coord[0]:
					if position[1] > coord[1]:
						for i in range(coord[1], position[1] + 1):
							shiplength += 1
							if kaiBoard[i][coord[0]] != " ":
								break
						if shiplength != piece[1]:
							possiblepositions[possiblepositions.index(coord)] = ""
							continue
					else:
						for i in range(coord[1], position[1] - 1, -1):
							shiplength += 1
							if kaiBoard[i][coord[0]] != " ":
								break
						if shiplength != piece[1]:
							possiblepositions[possiblepositions.index(coord)] = ""
							continue
				else:
					if position[0] > coord[0]:
						for i in range(coord[0], position[0] + 1):
							shiplength += 1
							if kaiBoard[coord[1]][i] != " ":
								break
						if shiplength != piece[1]:
							possiblepositions[possiblepositions.index(coord)] = ""
							continue
					else:
						for i in range(coord[0], position[0] - 1, -1):
							shiplength += 1
							if kaiBoard[coord[1]][i] != " ":
								break
						if shiplength != piece[1]:
							possiblepositions[possiblepositions.index(coord)] = ""
							continue
			posspositions = []
			for coord in possiblepositions:
				if not bool(coord):
					continue
				posspositions.append(coord)
			if len(posspositions) == 0:
				continue
			endcoord = posspositions[random.randint(0, len(posspositions)) - 1]
			if position[0] == endcoord[0]:
				if position[1] > endcoord[1]:
					for i in range(endcoord[1], position[1] + 1):
						kaiBoard[i][position[0]] = piece[0][0]
				else:
					for i in range(position[1], endcoord[1] + 1):
						kaiBoard[i][position[0]] = piece[0][0]
			else:
				if position[0] > endcoord[0]:
					for i in range(endcoord[0], position[0] + 1):
						kaiBoard[position[1]][i] = piece[0][0]
				else:
					for i in range(position[0], endcoord[0] + 1):
						kaiBoard[position[1]][i] = piece[0][0]
			placed = True




print("")

gamemode = ""
while gamemode == "":
	gamemode = input("Would you like to play classic or advanced Battleships? ")
	match gamemode:
		case "classic":
			board_template = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]
			kaiBoard = copy.deepcopy(board_template)
			guessBoard = copy.deepcopy(board_template)
			kaiGuessBoard = copy.deepcopy(board_template)
			remainingpieces = [["Aircraft Carrier", 5], ["Battleship", 4], ["Cruiser", 3], ["Submarine", 3], ["Destroyer", 2], ["Frigate", 2]]
			columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
			print("Here is the board:")
			time.sleep(0.5)
			print("   a  b  c  d  e  f  g  h  i  j ")
			for i in range(10):
				if i != 9:
					print(i + 1, end=" ")
				else:
					print(i + 1, end="")
				for j in range(10):
					print("[ ]", end="")
				print("")
			"""
			print("You own 6 ships:")
			time.sleep(1)
			print("The Aircraft Carrier - ", end="")
			time.sleep(1)
			print("It takes up 5 spaces on the board")
			time.sleep(1)
			print("The Battleship - ", end="")
			time.sleep(1)
			print("It takes up 4 spaces on the board")
			time.sleep(1)
			print("The Cruiser and Submarine - ", end="")
			time.sleep(1)
			print("They both take up 3 spaces on the board")
			time.sleep(1)
			print("And finally,")
			time.sleep(1)
			print("The Destroyer and Frigate - ", end="")
			time.sleep(1)
			print("They both take up 2 spaces on the board.")
			time.sleep(2)
			print("")
			print("I will have my own 6 ships.")
			time.sleep(1)
			print("We each place down our ships,")
			time.sleep(1)
			print("And after we have finished,")
			time.sleep(1)
			print("We try to sink each others!")
			time.sleep(2)
			"""
			print("Place your battleships down now!")
			time.sleep(0.2)
			ready = False
			while ready == False:
				board = copy.deepcopy(board_template)
				for piece in remainingpieces:
					placed = False
					validationError = ["This is an invalid position. Please choose somewhere else.", "There is already a piece here. Please choose somewhere else.", "You can't place it here. Please choose somewhere else.", "A %s cannot fit in this region. Please choose somewhere else." % (piece[0])]
					while placed == False: # Start to place
						print_board(board)
						position = ["", ""]
						position[0] = input("Place the head of %s" % (piece[0]) + "(e.g. a1, d5): ")
						if position[0] == "" or len(position[0]) != 2:
							print(validationError[0])
							continue
						if not position[0][1].isdigit():
							print(validationError[0])
							continue
						if not (position[0][0] in columns and int(position[0][1]) in range(1, 11)):
							print(validationError[0])
							continue
						position[1] = input("Place the end of %s" % (piece[0]) + "(e.g. a3, g5): ")
						if position[1] == "" or len(position[1]) != 2:
							print(validationError[0])
							continue
						if not position[1][1].isdigit():
							print(validationError[0])
							continue
						if not (position[1][0] in columns and int(position[1][1]) in range(1, 11)):
							print(validationError[0])
							continue
						if not (position[0][0] == position[1][0] or position[0][1] == position[1][1]) or position[0] == position[1]:
							print(validationError[3])
							continue
						else: # Update board[]
							changedcoords = []
							shiplength = 0
							obstruction = False
							if position[0][0] == position[1][0]:
								if position[0][1] > position[1][1]:
									for i in range(int(position[1][1]), int(position[0][1]) + 1):
										shiplength += 1
										if not (board[i - 1][columns.index(position[0][0])] == " "):
											print(validationError[1])
											obstruction = True
											break
										changedcoords.append(i)
								else:
									for i in range(int(position[0][1]), int(position[1][1]) + 1):
										shiplength += 1
										if not (board[i - 1][columns.index(position[1][0])] == " "):
											print(validationError[1])
											obstruction = True
											break
										changedcoords.append(i)
							else:
								if columns.index(position[0][0]) > columns.index(position[1][0]):
									for i in range(columns.index(position[1][0]), columns.index(position[0][0]) + 1):
										shiplength += 1
										if not (board[int(position[0][1]) - 1][i] == " "):
											print(validationError[1])
											obstruction = True
											break
										changedcoords.append(columns[i])
								else:
									for i in range(columns.index(position[0][0]), columns.index(position[1][0]) + 1):
										shiplength += 1
										if not (board[int(position[0][1]) - 1][i] == " "):
											print(validationError[1])
											obstruction = True
											break
										changedcoords.append(columns[i])
							if obstruction == True:
								continue
							if shiplength != piece[1]:
								print(validationError[3])
								continue
							if type(changedcoords[0]) == int:
								for row in changedcoords:
									board[row - 1][columns.index(position[0][0])] = piece[0][0]
							else:
								for column in changedcoords:
									board[int(position[0][1]) - 1][columns.index(column)] = piece[0][0]
						placed = True
				print_board(board)
				while True:
					readyinput = input("I have finished placing my ships. Have you?(y/n) ")
					match readyinput:
						case 'y':
							ready = True
							break
						case 'n':
							print("I'll give you a little big longer to place your ships.")
							break
						case '_':
							print("I gave you two choices. It's not that hard.")
							time.sleep(1)

			generate_board()
			print("Great! You're ready,")
			time.sleep(0.2)
			print("Now we can start.")
			time.sleep(1)
			turn = 0
			print("--------Turn %s--------" % (turn))
			print_game_board()
			
			print("This is the first turn.")
			print("As my guest,")
			print("I'll let you attack first.")
			print("Your goal is to attack coordinates that may contain my ships. ")
			print("If you can shoot all my ships out of the water,")
			print("You would win.")
			print("But.", end="")
			print(".", end="")
			print(".", end="")
			print("That's not happening.")

			print("---Your Turn---")
			target = input("Where would you like to attack?(e.g. a1, d5) ")

				


		case "advanced":
			pass
		case _:
			print("That's not a way of playing Battleships.")
			gamemode = ""