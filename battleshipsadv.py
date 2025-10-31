import time
import random

print("")

gamemode = ""
while gamemode == "":
	gamemode = input("Would you like to play classic or advanced Battleships? ")
	board = [["", "", "", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", "", "", ""]]
	match gamemode:
		case "classic":
			print("Here is the board:")
			time.sleep(0.2)
			print("   a  b  c  d  e  f  g  h  i  j ")
			for i in range(10):
				if i != 9:
					print(i + 1, end=" ")
				else:
					print(i + 1, end="")
				for i in range(10):
					print("[ ]", end="")
					time.sleep(0.05)
				print("")
				"""
			print("You own 6 ships:")
			time.sleep(1)
			print("The Carrier - ", end="")
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
			remainingpieces = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer", "Frigate"]
			columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
			for piece in remainingpieces:
				placed = False
				validationError = ["This is an invalid position. Please choose somewhere else.", "There is already a piece here. Please choose somewhere else.", "You can't place it here. Please choose somewhere else.", "A %s cannot fit in this region. Please choose somewhere else." % (piece)]
				while placed == False:
					print("   a  b  c  d  e  f  g  h  i  j ")
					for i in range(10):
						if i != 9:
							print(i + 1, end=" ")
						else:
							print(i + 1, end="")
						for i in range(10):
							print("[ ]", end="")
						print("")
					position = ["", ""]
					position[0] = input("Place the head of %s" % (piece) + "(e.g. a1, d5): ")
					if position[0] == "":
						print(validationError[0])
						continue
					if not position[0][1].isdigit():
						print(validationError[0])
						continue
					if not (position[0][0] in columns and int(position[0][1]) in range(1, 11)):
						print(validationError[0])
						continue
					position[1] = input("Place the end of %s" % (piece) + "(e.g. a3, g5): ")
					if position[1] == "":
						print(validationError[0])
						continue
					if position[1][1].isdigit():
						print(validationError[0])
						continue
					if not (position[1][0] in columns and int(position[1][1]) in range(1, 11)):
						print(validationError[0])
						continue
					if not (position[0][0] == position[1][0] or position[0][1] == position[1][1]) or position[0] == position[1]:
						print(validationError[3])
						continue
					else:
						if columns.index(position[0][0]) > columns.index(position[1][0]):
							shiplength = 0
							for i in range(columns.index(position[1][0]), columns.index(position[0][0]) + 1):
								shiplength += 1
								if not (board[int(position[0][1])][i] == ""):
									print(validationError[1])
									break
							match piece:
								case "Carrier":
									if shiplength != 5:
										print(validationError[3])
								case "Battleship":
									if shiplength != 4:
										print(validationError[3])
								case "Cruiser" | "Submarine":
									if shiplength != 3:
										print(validationError[3])
								case "Destroyer" | "Frigate":
									if shiplength != 2:
										print(validationError[3])


						elif columns.index(position[0][0]) == columns.index(position[1][0]):
							pass
						else:
							pass

		case "advanced":
			pass
		case _:
			gamemode = ""
