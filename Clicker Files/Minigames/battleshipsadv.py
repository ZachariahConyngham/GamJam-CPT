import time, copy
from random import randint
from math import floor

def batlshit():
	kaiTaunts = [[""],[""],[""]] #add something to this, 0 is you hit kai's ship, 1 is you didn't hit kai's ship, 2 is i sunk your ship, idk add more later

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
						if kaiGuessBoard[i][k] != " ":
							print("[" + kaiGuessBoard[i][k] + "]", end="")
						else:
							if bool([value for value in sunkShip if value[0] == board[i][k]]):
								print("[X]", end="")
							else:
								print("[" + board[i][k] + "]", end="")
				else:
					for k in range(10):
						print("[" + guessBoard[i][k] + "]", end="")
				if j == 0:
					print("  |  ", end="")
			print("")

	def generate_board():
		for piece in pieces:
			placed = False
			while placed == False:
				position = [randint(0,9), randint(0,9)]
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
				endcoord = posspositions[randint(0, len(posspositions)) - 1]
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

	def kaiGuess():
		global kaiSuccessAtk
		global sunkShips
		remainingLen = [value for value in userPieces if len(value) > 0]
		tgtLen = userPieces.index(max(remainingLen, key = userPieces.index)) + 2
		print(tgtLen)
		atkcoordsall = []
		atkcoords = []
		print(kaiSuccessAtk)
		if kaiSuccessAtk == True:
			for row in range(10):
				for column in range(10):
					if kaiGuessBoard[row][column] == "X":
						atkcoordsall.append(str(row) + str(column))
			atkcoords.append(atkcoordsall[0])
			for coord in atkcoordsall:
				if coord == atkcoords[0]:
					continue
				if coord[0] == atkcoords[0][0] or coord[1] == atkcoords[0][1]:
					if len(atkcoords) == 2:
						if atkcoords[0][0] == atkcoords[1][0]:
							atkdirection = 0
						else:
							atkdirection = 1
						if coord[atkdirection] == atkcoords[0][atkdirection]:
							atkcoords.append(coord)
					else:
						atkcoords.append(coord)
			print(atkcoordsall, atkcoords)
			possibleCoords = [[], []]
			limit = tgtLen - len(atkcoords)
			if len(atkcoords) > 1:
				if atkcoords[0][0] == atkcoords[1][0]: # if on the same row
					lwrlimit = int(min(atkcoords)[1]) - limit
					if lwrlimit < 0: lwrlimit = 0
					uprlimit = int(max(atkcoords)[1]) + limit
					if uprlimit > 9: uprlimit = 9
					for column in range(lwrlimit, int(min(atkcoords)[1])):
						if kaiGuessBoard[int(atkcoords[0][0])][column] != " ":
							continue
						else:
							possibleCoords[0].append(atkcoords[0][0] + str(column))
					for column in range(uprlimit, int(max(atkcoords)[1]), -1):
						if kaiGuessBoard[int(atkcoords[0][0])][column] != " ":
							continue
						else:
							possibleCoords[1].append(atkcoords[0][0] + str(column))
					target = str(atkcoords[0][0]) + str(max(possibleCoords[0], possibleCoords[1], key = len)[-1][1])
				else:
					lwrlimit = int(min(atkcoords)[0]) - limit
					if lwrlimit < 0: lwrlimit = 0
					uprlimit = int(max(atkcoords)[0]) + limit
					if uprlimit > 9: uprlimit = 9
					for row in range(lwrlimit, int(min(atkcoords)[0])):
						if kaiGuessBoard[row][int(atkcoords[0][1])] != " ":
							continue
						else:
							possibleCoords[0].append(str(row) + atkcoords[0][1])
					for row in range(uprlimit, int(max(atkcoords)[0]), -1):
						if kaiGuessBoard[row][int(atkcoords[0][1])] != " ":
							continue
						else:
							possibleCoords[1].append(str(row) + atkcoords[0][0])
					target = [max(possibleCoords[0], possibleCoords[1], key = len)[-1][0], atkcoords[0][1]]
				
				# Detect if cleared ship
				atkedLen = [value for index, value in enumerate(userPieces[len(atkcoords) - 1:])]
				pieceList = []
				for length in atkedLen:
					for ship in length:
						pieceList.append(ship)
				atkedPiece = [value for index, value in enumerate(pieceList) if value[0] == board[int(atkcoords[0][0])][int(atkcoords[0][1])]]
				print(board[int(atkcoords[0][0])][int(atkcoords[0][1])])
				spaces = []
				print(atkcoords, possibleCoords, limit, target, atkedLen, atkedPiece, pieceList)
				print(spaces, atkcoords)
				print_board(board)
				for row in board:
					for i in range(0, len(row)):
						if row[i] == atkedPiece[0][0]: # Error: multiple ships adjacent are being hit, therefore it thinks it's one ship; if same amount of tiles are hit as the length of first hit tile, it clears it and thinks ship is dead
							spaces.append(str(board.index(row)) + str(i))
				if len(spaces) == len(atkcoords) + 1:
					print("I sunk your %s! HAHAHAHA." % (atkedPiece[0]))
					userPieces[len(spaces) - 2].remove(atkedPiece[0])
					sunkShip.append(atkedPiece[0])
			else:
				print(atkcoords)
				spaces = [[], [], [], []]
				for axis in range(2):
					for gradient in range(-1, 3, 2):
						for space in range(int(atkcoords[0][axis]), -1 if gradient == -1 else 10, gradient):
							print(axis, gradient, space)
							if axis == 0:
								print(kaiGuessBoard[space][int(atkcoords[0][1])])
								if kaiGuessBoard[space][int(atkcoords[0][1])] not in [" ", "X"]: break
							else:
								if kaiGuessBoard[int(atkcoords[0][0])][space] not in [" ", "X"]: break
							spaces[(0 if gradient == -1 else 2) + axis].append(str(atkcoords[0][0] if axis == 1 else space) + str(atkcoords[0][1] if axis == 0 else space))
				len1 = len(spaces[0]) + len(spaces[2])
				len2 = len(spaces[1]) + len(spaces[3])
				print(spaces)
				if len1 == len2:
					direction = randint(0, 1)
					if len(spaces[direction]) == spaces[direction + 2]:
						target = spaces[randint(0, 1) * 2 + direction][1]
					else:
						target = max(spaces[direction], spaces[direction + 2], key = len)[1]
				else:
					if len1 > len2:
						if len(spaces[0]) == len(spaces[2]):
							target = spaces[randint(0, 1) * 2][1]
						else:
							target = max(spaces[0], spaces[2], key = len)[1]
					else:
						if len(spaces[1]) == len(spaces[3]):
							target = spaces[randint(0, 1) * 2 + 1][1]
						else:
							target = max(spaces[1], spaces[3], key = len)[1]
		else:
			lwstScore = [100, []]
			for row, rowvalue in enumerate(kaiGuessBoard): # count amount of spaces between target and end of the board
				for column, columnvalue in enumerate(rowvalue):
					if kaiGuessBoard[row][column] == "O": continue
					thisScore = 0
					spaces = [[],[],[],[]]
					for direction in range(4):
						if direction % 2 == 0:
							for space in range(row, -1 if direction == 0 else 10, 1 if direction == 2 else -1):
								print(row, column, direction, space)
								if kaiGuessBoard[space][column] not in [" ", "X"]:
									print("that")
									break
								if (str(row) + str(column)) not in spaces[direction]:
									spaces[direction].append(str(row) + str(column))
								print(spaces[direction], direction)
						else:
							for space in range(column, -1 if direction == 1 else 10, 1 if direction == 3 else -1):
								print(row, column, direction, space)
								if kaiGuessBoard[row][space] not in [" ", "X"]:
									print("that")
									break
								if (str(row) + str(column)) not in spaces[direction]:
									spaces[direction].append(str(row) + str(column))
								print(spaces[direction], direction)
						thisScore += ((len(spaces[direction]) % tgtLen)/(floor(len(spaces[direction]))/tgtLen + 1))
					for i in spaces:
						print(i)
					print(thisScore)
					print(kaiGuessBoard)
					thisScore += ((len(spaces[0]) + len(spaces[2]) % tgtLen)/(floor(len(spaces[0]) + len(spaces[2])/tgtLen) + 1))/2
					thisScore += ((len(spaces[1]) + len(spaces[3]) % tgtLen)/(floor(len(spaces[1]) + len(spaces[3])/tgtLen) + 1))/2
					print(thisScore)
					if thisScore == lwstScore[0]:
						lwstScore.append([row, column])
					if thisScore < lwstScore[0]:
						lwstScore[0] = thisScore
						lwstScore[1:] = []
						lwstScore.append([row, column])
					print(lwstScore, "this")
			target = lwstScore[randint(1, len(lwstScore) - 1)]
		print(target)
		if board[int(target[0])][int(target[1])] == " ":
			kaiGuessBoard[int(target[0])][int(target[1])] = "O"
		else:
			if bool([value for value in sunkShip if value[0] == atkedPiece[0][0]]):
				kaiSuccessAtk = False
				for coord in atkcoords:
					kaiGuessBoard[int(coord[0])][int(coord[1])] = "O"
				kaiGuessBoard[int(target[0])][int(target[1])] = "O"
			else:
				kaiSuccessAtk = True
				kaiGuessBoard[int(target[0])][int(target[1])] = "X"




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
				pieces = [["Aircraft Carrier", 5], ["Battleship", 4], ["Cruiser", 3], ["Submarine", 3], ["Destroyer", 2], ["Frigate", 2]]
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
					for piece in pieces:
						placed = False
						validationError = ["This is an invalid position. Please choose somewhere else.", "There is already a piece here. Please choose somewhere else.", "You can't place it here. Please choose somewhere else.", "A %s cannot fit in this region. Please choose somewhere else." % (piece[0])]
						while placed == False: # Start to place
							print_board(board)
							position = ["", ""]
							position[0] = input("Place the head of %s" % (piece[0]) + " (Length: %s)" % (piece[1]) + " (e.g. a1, d5): ")
							if not bool(position[0]) or not(len(position[0]) == 2 or len(position[0]) == 3 and position[0][1] + position[0][2] == "10"):
								print(validationError[0])
								continue
							if not position[0][1:].isdigit():
								print(validationError[0])
								continue
							if not (position[0][0] in columns and int(position[0][1:]) in range(1, 11)):
								print(validationError[0])
								continue
							position[1] = input("Place the end of %s" % (piece[0]) + "(e.g. a3, g5): ")
							if not bool(position[1]) or not(len(position[1]) == 2 or len(position[1]) == 3 and position[1][1] + position[1][2] == "10"):
								print(validationError[0])
								continue
							if not position[1][1:].isdigit():
								print(validationError[0])
								continue
							if not (position[1][0] in columns and int(position[1][1:]) in range(1, 11)):
								print(validationError[0])
								continue
							if not (position[0][0] == position[1][0] or position[0][1:] == position[1][1:]) or position[0] == position[1]:
								print(validationError[3])
								continue
							else: # Update board[]
								changedcoords = []
								shiplength = 0
								obstruction = False
								if position[0][0] == position[1][0]:
									if int(position[0][1:]) > int(position[1][1:]):
										for i in range(int(position[1][1:]), int(position[0][1:]) + 1):
											shiplength += 1
											if not (board[i - 1][columns.index(position[0][0])] == " "):
												print(validationError[1])
												obstruction = True
												break
											changedcoords.append(i)
									else:
										for i in range(int(position[0][1:]), int(position[1][1:]) + 1):
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
											if not (board[int(position[0][1:]) - 1][i] == " "):
												print(validationError[1])
												obstruction = True
												break
											changedcoords.append(columns[i])
									else:
										for i in range(columns.index(position[0][0]), columns.index(position[1][0]) + 1):
											shiplength += 1
											if not (board[int(position[0][1:]) - 1][i] == " "):
												print(validationError[1])
												obstruction = True
												break
											changedcoords.append(columns[i])
								if obstruction == True:
									continue
								if shiplength != piece[1]:
									print(shiplength, piece[1])
									print(validationError[3])
									continue
								if type(changedcoords[0]) == int:
									for row in changedcoords:
										board[row - 1][columns.index(position[0][0])] = piece[0][0]
								else:
									for column in changedcoords:
										board[int(position[0][1:]) - 1][columns.index(column)] = piece[0][0]
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
								print("I gave you two choices. It's not that hard.")
								time.sleep(1)

				generate_board()
				print("Great! You're ready,")
				time.sleep(0.2)
				print("Now we can start.")
				time.sleep(1)
				true_turn = 0
				turn = [0, "kai"]
				gamestate = "ongoing"

				# ai use variables only
				global kaiSuccessAtk
				global sunkShip
				sunkShip = []
				kaiSuccessAtk = False
				userPieces = [["Frigate", "Destroyer"], ["Submarine", "Cruiser"], ["Battleship"], ["Aircraft Carrier"]]


				while gamestate == "ongoing":
					print("--------Turn %s--------" % (turn[0]))
					print_game_board()
					if true_turn == 0:
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
						turn[1] = "user"
					elif turn == 0:
						if (randint(0, 1) == 0):
							turn[1] = "user"
						else:
							turn[1] = "kai"
					# Start of attack gameplay

					if turn[1] == "user":
						print("---Your Turn---")
						target = ""
						print_board(kaiBoard)
						while target == "":
							target = input("Where would you like to attack?(e.g. a1, d5) ")
							if not (len(target) == 2 or len(target) == 3 and target[1:] == "10") or not target[0].isalpha() or not target[1].isdigit():
								target = ""
								print("That is in the incorrect format.")
								continue
							if (target[0] not in columns) or (int(target[1:]) not in range(1, 11)):
								target = ""
								print("That's not a valid position.")
								continue
							if guessBoard[int(target[1:]) - 1][columns.index(target[0])] != " ":
								target = ""
								print("You have already hit that spot.")
								continue
						# player shot valid
						if kaiBoard[int(target[1:]) - 1][columns.index(target[0])] != " ": # if targeted coord is not empty
							guessBoard[int(target[1:]) - 1][columns.index(target[0])] = "X" # guessBoard update to 'hit'
							shotShip = kaiBoard[int(target[1:]) - 1][columns.index(target[0])] # identify hit ship
							spaces = [] # declare spaces list
							for row in kaiBoard: # for each row in kaiBoard
								for index, value in enumerate(row):
									if value == shotShip:
										spaces.append(str(kaiBoard.index(row)) + str(index))
							breakFor = False # declare breakFor bool
							for coord in spaces:
								print(coord)
								if guessBoard[int(coord[0])][int(coord[1])] != "X": # if the ship is not hit
									breakFor = True # breakFor
									break
							if breakFor == True:
								print("You have hit my ship! %s" % (kaiTaunts[0][randint(0, len(kaiTaunts[0]) - 1)]))
							else:
								print("You have sunk my %s!" % ([value for index, value in enumerate(pieces) if value[0][0] == shotShip][0][0]))
						else:
							guessBoard[int(target[1:]) - 1][columns.index(target[0])] = "O"
							print(kaiTaunts[1][randint(0, len(kaiTaunts[1]) - 1)])
					else:
						print("---His Turn---")
						kaiGuess()

					turn[0] += 1
					true_turn += 1
					match turn[1]:
						case "user":
							turn[1] = "kai"
						case "kai":
							turn[1] = "user"
						case _:
							print("?????")
					continue #end iteration


					


			case "advanced":
				pass
			case _:
				print("That's not a way of playing Battleships.")
				gamemode = ""

batlshit()