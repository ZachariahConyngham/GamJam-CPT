import time, os
import copy
#import functions as func
from random import randint, choice
from math import floor

def clear():  # Clears the terminal
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")

def batlshit(shift):
	clear()
	kaiTaunts = [[""],[""],[""],[""],[""]] #add something to this, 0 is you hit kai's ship, 1 is you didn't hit kai's ship, 2 is i sunk your ship, 3 is kai wins, 4 is kai loses idk add more later

	def clearline():
		print("\033[" + str(shift + 2) + "G", end="")
		print(" " * 75 + "\r", end="")

	def pwb(value, end = ""): # to simplify printing - print_within_brackets
		print("[%s]" % (value), end=end)
		return

	def print_board(board): # general printing board such as debugging or tutorial
		print("\033[23;" + str(shift + 20) + "H", end="")
		clearline()
		print("\033[23;" + str(shift + 20) + "H   a  b  c  d  e  f  g  h  i  j ") # x-axis
		for row in range(10):
			clearline()
			print("\033[" + str(row + 24) + ";" + str(shift + 20) + "H" + str(row + 1), end=" " if row != 9 else "") # row number, if it is 10, don't print last space
			for column in range(10): # prints columns
				pwb(board[row][column]) # print tiles of the defined board
			print("") # print on new line

	def print_game_board(): # game board that is printed, change this to work with game
		print("          Your Board              |        Your Guessed Board")
		print("   a  b  c  d  e  f  g  h  i  j   |     a  b  c  d  e  f  g  h  i  j")
		for row in range(10):
			print(row + 1, end="" if row == 9 else " ") # prints side numbers
			for column in range(10): # prints each tile
				if kaiGuessBoard[row][column] != " ": 
					pwb("X" if any(ship.startswith(board[row][column]) for ship in sunkShip) else kaiGuessBoard[row][column])
				else: 
					pwb(board[row][column])
			print("  |  ", end="") # print middle line
			print(row + 1, end="" if row == 9 else " ") # prints side numbers
			for column in range(10): # print guessBoard tiles
				pwb(guessBoard[row][column])
			print("")
	
	def generate_board(): # ai generate the board
		for piece in pieces:
			while True:
				position = [randint(0,9), randint(0,9)]
				if kaiBoard[position[0]][position[1]] != " ": continue
				
				global posspositions
				posspositions = [[position[0], position[1] + piece[1] - 1], [position[0], position[1] - piece[1] + 1], [position[0] + piece[1] - 1, position[1]], [position[0] - piece[1] + 1, position[1]]]
				
				def invalid_coord():
					global posspositions
					posspositions[index] = ""
					return True

				for index, coord in enumerate(posspositions):
					shiplength = 0
					if (any(number not in range(10) for number in coord)) and invalid_coord(): continue
					axis = floor(index / 2)
					gradient = -1 if index % 2 == 0 else 1
					for space in range(coord[1 - axis], position[1 - axis] + gradient, gradient):
						shiplength += 1
						if axis == 0 and kaiBoard[coord[0]][space] != " ": break
						if axis == 1 and kaiBoard[space][coord[1]] != " ": break
					if shiplength != piece[1] and invalid_coord(): continue
				
				posspositions = [coord for coord in posspositions if bool(coord)]
				if not bool(posspositions): continue
				endcoord = choice(posspositions)

				eqAxis = 1 if position[0] == endcoord[0] else 0
				gradient = -1 if position[eqAxis] > endcoord[eqAxis] else 1
				for i in range(position[eqAxis], endcoord[eqAxis] + gradient, gradient):
					kaiBoard[position[0] if eqAxis == 1 else i][i if eqAxis == 1 else position[1]] = piece[0][0]
				break

	def kai_guess():
		global kaiSuccessAtk, sunkShips
		cleared = False
		tgtLen = max([index for index, value in enumerate(userPieces) if len(value) > 0]) + 2
		atkcoords, atkcoordsall = [], []

		if kaiSuccessAtk == True:
			for row in range(10):
				for column in range(10):
					if kaiGuessBoard[row][column] == "X": atkcoordsall.append(str(row) + str(column))
			atkcoords.append(atkcoordsall[0])

			for coord1 in set(atkcoordsall) - set(atkcoords):
				atkcoords.append(coord1)
				atkdirection = 0 if atkcoords[0][0] == atkcoords[1][0] else 1
				atkdirone = atkdirection == 1

				for coord2 in set(atkcoordsall) - set(atkcoords):
					if coord2[atkdirection] == atkcoords[0][atkdirection]: atkcoords.append(coord2)
				if tgtLen <= len(atkcoords):
					atkcoords = [atkcoords[0]]
					continue

				limitbreak = [False, False]
				lwrlimit = int(min(atkcoords)[1 - atkdirection]) - 1
				uprlimit = int(max(atkcoords)[1 - atkdirection]) + 1
				if lwrlimit < 0:
					limitbreak[0] = True
					lwrlimit = 0
				if uprlimit > 9:
					limitbreak[1] = True
					uprlimit = 9
				condition1 = (kaiGuessBoard[lwrlimit if atkdirone else int(atkcoords[0][0])][int(atkcoords[0][1]) if atkdirone else lwrlimit] == "O" or limitbreak[0])
				condition2 = (kaiGuessBoard[uprlimit if atkdirone else int(atkcoords[0][0])][int(atkcoords[0][1]) if atkdirone else uprlimit] == "O" or limitbreak[1])
				if condition1 and condition2:
					atkcoords = [atkcoords[0]]
					continue
				else: break

			possibleCoords = [[], []]
			limit = tgtLen - len(atkcoords)
			if len(atkcoords) > 1:
				axis = 1 if atkcoords[0][0] == atkcoords[1][0] else 0
				lwrlimit = int(min(atkcoords)[axis]) - limit
				uprlimit = int(max(atkcoords)[axis]) + limit
				if lwrlimit < 0: lwrlimit = 0
				if uprlimit > 9: uprlimit = 9
				for gradient in range(1, -3, -2):
					for space in range(lwrlimit if gradient == 1 else uprlimit, int(min(atkcoords)[axis]), gradient):
						if axis == 1 and kaiGuessBoard[int(atkcoords[0][0])][space] == " ": possibleCoords[0 if gradient == 1 else 1].append(atkcoords[0][0] + str(space))
						if axis == 0 and kaiGuessBoard[space][int(atkcoords[0][1])] == " ": possibleCoords[0 if gradient == 1 else 1].append(str(space) + atkcoords[0][1])
				temp = [str(atkcoords[0][1 - axis]), str(max(possibleCoords[0], possibleCoords[1], key=len)[-1][axis])]
				target = temp[1 - axis] + temp[axis]
			else:
				spaces = [[], [], [], []]
				for axis in range(2):
					for gradient in range(-1, 3, 2):
						for space in range(int(atkcoords[0][axis]), -1 if gradient == -1 else 10, gradient):
							if axis == 0 and not (kaiGuessBoard[space][int(atkcoords[0][1])] == " " or kaiGuessBoard[space][int(atkcoords[0][1])] == "X" and (str(space) + atkcoords[0][1]) in atkcoords): break
							if axis == 1 and not (kaiGuessBoard[int(atkcoords[0][0])][space] == " " or kaiGuessBoard[int(atkcoords[0][0])][space] == "X" and (atkcoords[0][0] + str(space)) in atkcoords): break
							spaces[(0 if gradient == -1 else 2) + axis].append(str(atkcoords[0][0] if axis == 1 else space) + str(atkcoords[0][1] if axis == 0 else space))
				len1 = len(spaces[0]) + len(spaces[2])
				len2 = len(spaces[1]) + len(spaces[3])
				direction = randint(0, 1) if len1 == len2 else (0 if len1 > len2 else 1)
				target = spaces[randint(0, 1) * 2 + direction][1] if len(spaces[direction]) == len(spaces[direction + 2]) else max(spaces[direction], spaces[direction + 2], key=len)[1]
			
			spaces = {key: [] for key in sum(userPieces, [])}
			for ship in spaces:
				for row in range(len(board)):
					for column in range(len(board[row])):
						if board[row][column] == ship[0]: 
							spaces[ship].append(str(row) + str(column))
				if all((value in set(atkcoords + atkcoordsall + [target])) for value in spaces[ship]):
					cleared = True
					print("I sunk your %s! HAHAHAHA." % (ship))
					print(kaiTaunts[2][randint(0, len(kaiTaunts[2]) - 1)])
					userPieces[len(spaces[ship]) - 2].remove(ship)
					sunkShip.append(ship)
		else:
			lwstScore = [100, []]
			for rowindex, row in enumerate(kaiGuessBoard):
				for columnindex, column in enumerate(row):
					if kaiGuessBoard[rowindex][columnindex] == "O": continue
					thisScore = 0
					spaces = [[],[],[],[]] # up, left, down, right
					for direction in range(4):
						axis = 1 if direction % 2 == 0 else 0
						gradient = floor(direction/2) == 0
						for space in range(rowindex if direction % 2 == 0 else columnindex, 10 if gradient else -1, 1 if gradient else -1):
							temp = [space, columnindex if axis == 1 else rowindex]
							if kaiGuessBoard[temp[1 - axis]][temp[axis]] not in [" ", "X"]: break
							if (str(temp[1 - axis]) + str(axis)) not in spaces[direction]: spaces[direction].append(str(temp[1 - axis]) + str(temp[axis]))
						thisScore += ((len(spaces[direction]) % tgtLen)/(floor(len(spaces[direction]))/tgtLen + 1))
					for i in range(2):
						thisScore += ((len(spaces[i] + spaces[2 + i]) % tgtLen)/(floor(len(spaces[i] + spaces[2 + i])/tgtLen) + 1))/2

					if thisScore == lwstScore[0]:
						lwstScore.append([rowindex, columnindex])
					if thisScore < lwstScore[0]:
						lwstScore[0] = thisScore
						lwstScore[1:] = []
						lwstScore.append([rowindex, columnindex])
			target = lwstScore[randint(1, len(lwstScore) - 1)]

		if board[int(target[0])][int(target[1])] == " ":
			kaiGuessBoard[int(target[0])][int(target[1])] = "O"
			print("I attacked %s" % (columns[int(target[1])] + str(int(target[0]) + 1)))
		else:
			kaiGuessBoard[int(target[0])][int(target[1])] = "O" if cleared else "X"
			if cleared:
				if len(atkcoordsall) <= len(atkcoords): kaiSuccessAtk = False
				for coord in spaces[sunkShip[-1]]:
					kaiGuessBoard[int(coord[0])][int(coord[1])] = "O"
				cleared = False
			else:
				kaiSuccessAtk = True
				print("I attacked %s" % (columns[int(target[1])] + str(int(target[0]) + 1)))


	print("") # Start of running all code: change print statements in here
	board_template = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]
	kaiBoard = copy.deepcopy(board_template)
	guessBoard = copy.deepcopy(board_template)
	kaiGuessBoard = copy.deepcopy(board_template)
	pieces = [["Aircraft Carrier", 5], ["Battleship", 4], ["Cruiser", 3], ["Submarine", 3], ["Destroyer", 2], ["Frigate", 2]]
	columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
	
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
	
	time.sleep(0.2)
	ready = False
	while ready == False:
		board = copy.deepcopy(board_template)
		validationError = ["\033[41;" + str(shift + 2) + "HThis is an invalid position. Please choose somewhere else.", "\033[41;" + str(shift + 2) + "HThere is already a piece here. Please choose somewhere else.", "\033[41;" + str(shift + 2) + "HYou can't place it here. Please choose somewhere else.", ""]
		for piece in pieces:
			validationError[3] = "A %s cannot fit in this region. Please choose somewhere else." % (piece[0])
			while True: # Start to place
				print_board(board)
				position = ["", ""]
				position[0] = input("\033[37;" + str(shift + 2) + "HPlace the head of %s (Length: %s) (e.g. a1, d5): " % (piece[0], piece[1]))
				if not bool(position[0]) or not(len(position[0]) == 2 or position[0][1:] == "10"):
					print(validationError[0])
					continue
				if not (position[0][0] in columns and position[0][1:] in [str(x) for x in range(1, 11)]):
					print(validationError[0])
					continue
				position[1] = input("\033[38;" + str(shift + 2) + "HPlace the end of %s (e.g. a3, g5): " % (piece[0]))
				if not bool(position[1]) or not(len(position[1]) == 2 or position[1][1:] == "10"):
					print(validationError[0])
					continue
				if not (position[1][0] in columns and position[1][1:] in [str(x) for x in range(1, 11)]):
					print(validationError[0])
					continue
				if not (position[0][0] == position[1][0] or position[0][1:] == position[1][1:]) or position[0] == position[1]:
					print(validationError[3])
					continue
				# Update board[]
				changedcoords = []
				shiplength = 0
				obstruction = False
				# if same column
				if position[0][0] == position[1][0]:
					gradient = 0 if int(position[0][1:]) > int(position[1][1:]) else 1
					for i in range(int(position[1 - gradient][1:]) - 1, int(position[gradient][1:])):
						print(i)
						shiplength += 1
						if not (board[i - 1][columns.index(position[0][0])] == " "):
							print(validationError[1])
							obstruction = True
							break
						changedcoords.append(i)
				else:
					gradient = 0 if columns.index(position[0][0]) > columns.index(position[1][0]) else 1
					for i in range(columns.index(position[1 - gradient][0]), columns.index(position[gradient][0]) + 1):
						shiplength += 1
						if not (board[int(position[0][1:]) - 1][i] == " "):
							print(validationError[1])
							obstruction = True
							break
						changedcoords.append(columns[i])
				if obstruction == True:
					print(validationError[1])
					continue
				if shiplength != piece[1]:
					print(validationError[3])
					print("Your %s needs to be length %s." % (piece[0], piece[1]))
					clear()
					continue
				axis = isinstance(changedcoords[0], int)
				print(changedcoords)
				for space in changedcoords:
					board[space if axis else int(position[0][1:]) - 1][columns.index(position[0][0] if axis else space)] = piece[0][0]
					clear()
				break
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
	true_turn = 0
	turn = [0, "kai"]
	gamestate = "ongoing"
	playerSunkShip = [piece[0] for piece in pieces]

	# ai use variables only
	global kaiSuccessAtk
	global sunkShip
	sunkShip = []
	kaiSuccessAtk = False
	userPieces = [["Frigate", "Destroyer"], ["Submarine", "Cruiser"], ["Battleship"], ["Aircraft Carrier"]]


	while gamestate == "ongoing":
		clear()
		print("--------Turn %s--------" % (floor(turn[0] / 2) + 1))
		print_game_board()
		# print_board(kaiBoard)    ### For debugging purposes only
		if true_turn == 0:
			print("This is the first turn.")
			time.sleep(0.4)
			print("As my guest,")
			time.sleep(0.4)
			print("I'll let you attack first.")
			time.sleep(0.4)
			print("Your goal is to attack coordinates that may contain my ships. ")
			time.sleep(0.4)
			print("If you can shoot all my ships out of the water,")
			time.sleep(0.4)
			print("You would win.")
			time.sleep(0.4)
			print("But.", end="")
			print(".", end="")
			print(".", end="")
			print("That's not happening.")
			time.sleep(0.4)
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
			while target == "":
				target = input("Where would you like to attack?(e.g. a1, d5) ")
				if not (len(target) == 2 or target[1:] == "10") or not target[0].isalpha() or not target[1].isdigit():
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
			shotShip = kaiBoard[int(target[1:]) - 1][columns.index(target[0])] # identify hit ship
			if shotShip != " ": # if targeted coord is not empty
				spaces = [] # declare spaces list
				for rowindex, row in enumerate(kaiBoard): # check where the shotShip exists
					for columnindex, column in enumerate(row):
						if column == shotShip:
							spaces.append(str(rowindex) + str(columnindex))
				guessBoard[int(target[1:]) - 1][columns.index(target[0])] = "X" # guessBoard update to 'hit'
				breakFor = False
				for coord in spaces:
					if guessBoard[int(coord[0])][int(coord[1])] != "X": # if the ship is not sunk
						breakFor = True # breakFor
						break
				if breakFor:
					print("You have hit my ship! %s" % (kaiTaunts[0][randint(0, len(kaiTaunts[0]) - 1)]))
					time.sleep(1.5)
				else:
					print("You have sunk my %s!" % ([value for index, value in enumerate(pieces) if value[0][0] == shotShip][0][0]))
					for coord in spaces:
						guessBoard[int(coord[0])][int(coord[1])] = shotShip # guessBoard update to 'hit'
					playerSunkShip.remove([ship for ship in playerSunkShip if ship[0] == shotShip][0])
					if len(playerSunkShip) == 0:
						gamestate = "user"
					time.sleep(1.5)

			else:
				guessBoard[int(target[1:]) - 1][columns.index(target[0])] = "O"
				print(kaiTaunts[1][randint(0, len(kaiTaunts[1]) - 1)])
		else:
			print("---His Turn---")
			kai_guess()
			time.sleep(2)
			if len(sunkShip) == 6:
				gamestate = "kai"


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

	match gamestate:
		case "kai":
			print("HAHAHAHAHA! I have defeated you! %s" % (kaiTaunts[3][randint(0, len(kaiTaunts[3]) - 1)]))
		case "user":
			print("NOOOOOOO! How have I lost, it cannot be! %s" % (kaiTaunts[4][randint(0, len(kaiTaunts[4]) - 1)]))
	time.sleep(5)

# batlshit(30)
