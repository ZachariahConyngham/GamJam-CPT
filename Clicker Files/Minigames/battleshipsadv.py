import time, copy
from random import randint
from math import floor

def batlshit():
	kaiTaunts = [[""],[""],[""]] #add something to this, 0 is you hit kai's ship, 1 is you didn't hit kai's ship, 2 is i sunk your ship, idk add more later

	def pwb(value, end=""): # to simplify printing - print_within_brackets
		print("[%s]" % (value), end=end)
		return

	def print_board(board): # general printing board such as debugging or tutorial
		print("   a  b  c  d  e  f  g  h  i  j ") # x-axis
		for row in range(10):
			print(row + 1, end = " " if row != 9 else "") # row number, if it is 10, don't print last space
			for column in range(10): # prints columns
				pwb(board[row][column]) # print tiles of the defined board
			print("") # print on new line

	def print_game_board(): # game board that is printed, change this to work with game
		print("          Your Board              |        Your Guessed Board")
		print("   a  b  c  d  e  f  g  h  i  j   |     a  b  c  d  e  f  g  h  i  j")
		for row in range(10):
			for boardid in range(0,2):
				if row != 9:
					print(row + 1, end=" ")
				else:
					print(row + 1, end="")
				if boardid == 0:
					for column in range(10):
						if kaiGuessBoard[row][column] != " ":
							if any(ship.startswith(board[row][column]) for ship in sunkShip):
								pwb("X")
							else:
								pwb(kaiGuessBoard[row][column])
						else:
							pwb(board[row][column])
				else:
					for k in range(10):
						pwb(guessBoard[i][k])
				if j == 0:
					print("  |  ", end="")
			print("")
	def generate_board(): # ai generate the board
		for piece in pieces:
			placed = False
			while placed == False:
				position = [randint(0,9), randint(0,9)]
				if kaiBoard[position[0]][position[1]] != " ":
					continue
				
				global possiblepositions
				possiblepositions = [[position[0], position[1] + piece[1] - 1], [position[0], position[1] - piece[1] + 1], [position[0] + piece[1] - 1, position[1]], [position[0] - piece[1] + 1, position[1]]]
				def invalid_coord():
					global possiblepositions
					possiblepositions[index] = ""
					return True

				print(position, piece)
				for index, coord in enumerate(possiblepositions):
					shiplength = 0
					if (any(number not in range(10) for number in coord)) and invalid_coord(): continue
					axis = floor(index / 2) ### 1,1 -- 1,0 1,2 0,1 2,1
					print(coord[1 - axis], position[1 - axis] + (-1 if index % 2 == 0 else 1), -1 if index % 2 == 0 else 1)
					for space in range(coord[1 - axis], position[1 - axis] + (-1 if index % 2 == 0 else 1), -1 if index % 2 == 0 else 1):
						shiplength += 1
						if axis == 0 and kaiBoard[coord[0]][space] != " ": break
						if axis == 1 and kaiBoard[space][coord[1]] != " ": break
					if shiplength != piece[1] and invalid_coord(): continue
				
				posspositions = [coord for coord in possiblepositions if bool(coord)]
				if not bool(posspositions): continue
				endcoord = posspositions[randint(0, len(posspositions) - 1)] # work on thisssssssssssssssssssssssssssssssssssssssssssss, simplify this please
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
		cleared = False
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
			for coord1 in atkcoordsall:
				if coord1 in atkcoords: continue
				atkcoords.append(coord1)
				print(atkcoords)
				if atkcoords[0][0] == atkcoords[1][0]: # if they are on the same row
					atkdirection = 0
				else: # if they are on the same column
					atkdirection = 1
				for coord2 in atkcoordsall:
					if coord2 in atkcoords: continue
					print(coord2)
					if coord2[atkdirection] == atkcoords[0][atkdirection]:
						atkcoords.append(coord2)
				limitbreak = [False, False] # 144 - 152: check whether the Xs have been blocked and not marked as sunk ship
				lwrlimit = int(min(atkcoords)[0 if atkdirection == 1 else 1]) - 1
				if lwrlimit < 0:
					limitbreak[0] = True
					lwrlimit = 0
				uprlimit = int(max(atkcoords)[0 if atkdirection == 1 else 1]) + 1
				if uprlimit > 9:
					limitbreak[1] = True
					uprlimit = 9
				print(lwrlimit, uprlimit)
				if tgtLen <= len(atkcoords): 
					atkcoords = []
					atkcoords.append(atkcoordsall[0])
					continue
				condition1 = bool(kaiGuessBoard[lwrlimit if atkdirection == 1 else int(atkcoords[0][0])][lwrlimit if atkdirection == 0 else int(atkcoords[0][1])] == "O" or limitbreak[0])
				condition2 = bool(kaiGuessBoard[uprlimit if atkdirection == 1 else int(atkcoords[0][0])][uprlimit if atkdirection == 0 else int(atkcoords[0][1])] == "O" or limitbreak[1])
				if condition1 and condition2:
					atkcoords = []
					atkcoords.append(atkcoordsall[0])
					continue
				else:
					break

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
					print(possibleCoords)
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
					print(possibleCoords)
					target = [max(possibleCoords[0], possibleCoords[1], key = len)[-1][0], atkcoords[0][1]]
			else:
				print(atkcoords)
				spaces = [[], [], [], []]
				print_board(kaiGuessBoard)
				for axis in range(2):
					for gradient in range(-1, 3, 2):
						for space in range(int(atkcoords[0][axis]), -1 if gradient == -1 else 10, gradient):
							print(axis, gradient, space)
							if axis == 0:
								print(space, atkcoords[0][1])
								if not (kaiGuessBoard[space][int(atkcoords[0][1])] == " " or kaiGuessBoard[space][int(atkcoords[0][1])] == "X" and (str(space) + atkcoords[0][1]) in atkcoords): break
							else:
								print(atkcoords[0][0], space)
								print(kaiGuessBoard[int(atkcoords[0][0])][space] == "X", (atkcoords[0][0] + str(space)) in atkcoords)
								if not (kaiGuessBoard[int(atkcoords[0][0])][space] == " " or kaiGuessBoard[int(atkcoords[0][0])][space] == "X" and (atkcoords[0][0] + str(space)) in atkcoords): break
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
			# Detect if cleared ship
			pieceList = []
			for length in userPieces:
				for ship in length:
					pieceList.append(ship)
			atkedPiece = [piece for piece in pieceList if piece[0] == board[int(atkcoords[0][0])][int(atkcoords[0][1])]]
			print(board[int(atkcoords[0][0])][int(atkcoords[0][1])])
			spaces = []
			print(atkcoords, possibleCoords, limit, target, atkedPiece, pieceList)
			print_board(board)
			for row in board:
				for i in range(0, len(row)):
					if row[i] == atkedPiece[0][0]: # Error: multiple ships adjacent are being hit, therefore it thinks it's one ship; if same amount of tiles are hit as the length of first hit tile, it clears it and thinks ship is dead
						spaces.append(str(board.index(row)) + str(i))
			print(spaces)
			if len(spaces) == len(atkcoords) + 1:
				cleared = True
				for coord in atkcoords:
					if board[int(coord[0])][int(coord[1])] != atkedPiece[0][0]:
						cleared = False
						break
				if board[int(target[0])][int(target[1])] != atkedPiece[0][0]:
					cleared = False
				if cleared:
					print("I sunk your %s! HAHAHAHA." % (atkedPiece[0]))
					userPieces[len(spaces) - 2].remove(atkedPiece[0])
					sunkShip.append(atkedPiece[0])
		else:
			lwstScore = [100, []]
			for row, rowvalue in enumerate(kaiGuessBoard): # count amount of spaces between target and end of the board
				for column, columnvalue in enumerate(rowvalue):
					if kaiGuessBoard[row][column] == "O": continue
					thisScore = 0
					spaces = [[],[],[],[]] # up, left, down, right
					for direction in range(4):
						if direction % 2 == 0:
							for space in range(row, 10 if direction == 0 else -1, 1 if direction == 0 else -1):
								print(row, column, direction, space)
								if kaiGuessBoard[space][column] not in [" ", "X"]:
									print("that")
									break
								if (str(space) + str(column)) not in spaces[direction]:
									spaces[direction].append(str(space) + str(column))
								print(spaces[direction], direction)
						else:
							for space in range(column, 10 if direction == 1 else -1, 1 if direction == 1 else -1):
								print(row, column, direction, space)
								if kaiGuessBoard[row][space] not in [" ", "X"]:
									print("that")
									break
								if (str(row) + str(space)) not in spaces[direction]:
									spaces[direction].append(str(row) + str(space))
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
			if cleared == True:
				if len(atkcoordsall) <= len(atkcoords):
					kaiSuccessAtk = False
				for coord in atkcoords:
					kaiGuessBoard[int(coord[0])][int(coord[1])] = "O"
				kaiGuessBoard[int(target[0])][int(target[1])] = "O"
				cleared = False
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
					print(sunkShip)
					print("--------Turn %s--------" % (floor(turn[0] / 2)))
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