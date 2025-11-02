import random, time, os

view = 0
place1 = 1
place2 = 1
place3 = 1
place4 = 1
turn = 1
snakes = ["25-4", "50-30", "56-26", "83-58", "93-63", "99-42"]
ladders = ["8-27", "19-43", "33-52", "40-41", "54-66", "64-85"]
squares = [0, 0, 0, 0]

bool = True

def generate():
    os.system("cls")
    if view == 0:
        for i in range(5):
            print("\n-------------------------------------------------------------\n|", end=" ")
            for i2 in range(10):
                if ((20 * (5 - i)) - i2) in squares:
                    count = squares.count((20 * (5 - i)) - i2)
                    indexes = [x for x in squares if x == ((20 * (5 - i)) - i2)]
                    match count:
                        case 1:
                            print(" " + chr(squares.index(indexes[0]) + 65) + "  |", end=" ")
                        case 2:
                            print(chr(squares.index(indexes[0]) + 65) + " " + chr(squares.index(indexes[1], squares.index(indexes[0]) + 1) + 65) + " |", end=" ")
                        case 3:
                            print("ABC |", end=" ")
                else:
                    print(str("%03d" % ((20 * (5 - i)) - i2)) + " |", end=" ")
            if i == 0:
                print("                  Enter '1' to view pieces on the board.", end=" ")
            elif i == 1:
                print("                  Enter '3' to advance the turn.", end=" ")
            print("\n-------------------------------------------------------------\n|", end=" ")
            for i2 in range(10):
                if ((20 * (4 - i)) + i2 + 1) in squares:
                    count = squares.count((20 * (4 - i)) + i2 + 1)
                    indexes = [x for x in squares if x == ((20 * (4 - i)) + i2 + 1)]
                    match count:
                        case 1:
                            print(" " + chr(squares.index(indexes[0]) + 65) + "  |", end=" ")
                        case 2:
                            print(chr(squares.index(indexes[0]) + 65) + " " + chr(squares.index(indexes[1], squares.index(indexes[0]) + 1) + 65) + " |", end=" ")
                        case 3:
                            print("ABC |", end=" ")
                else:
                    print(str("%03d" % ((20 * (4 - i)) + i2 + 1)) + " |", end=" ")
            if i == 0:
                print("                  Enter '2' to view snakes and ladders on the board.", end=" ")
        print("\n-------------------------------------------------------------\n", end=" ")
    
    elif view == 1:
        print("\n\n-------------------------------------------------------------")
        print("| 100 | /\9 | 098 | 097 | 096 | 095 | 094 | 0/\ | 092 | 091 |                   Enter '1' to view pieces on the board.")
        print("-------/ /-----------------------------------\ \-------------")
        print("| 081 / /82 | //3 | 084 |/-/5 | 086 | 087 | 08\ \ 089 | 090 |                   Enter '2' to view snakes and ladders on the board.")
        print("-----/ /-----/ /--------/-/--------------------\ \-----------")
        print("| 08/ / 079 / /78 | 077/-/076 | 075 | 074 | 073/ /072 | 071 |                   Enter '3' to advance the turn.")
        print("----\ \----/ /--------/-/---------------------/ /------------")
        print("| 061\ \O62\ \O63 | 0/-/| 065 | 06\-\ 067 | 06\/| 069 | 070 |")
        print("------\ \---\ \--------------------\-\-----------------------")
        print("| 060  \ \9 |\/58 | 057 | 0/\ | 055 \-\S4 | 053 |/-/2 | 051 |                   Your Position (A): Square " + str(squares[0]))
        print("--------\ \----------------\ \------------------/-/----------")
        print("| |-| | 0\/ | /-/ | 044 | 04\ \ 046 | 047 | 048/-/049 | 0/\ |                   Game Master's Position (B): Square " + str(squares[1]))
        print("--|-|--------/-/-------------\ \--------------/-/--------||--")
        print("| |-| | 039 /-/38 | 037 | 036 \ /35 | 034 | 0/-/| 032 | 0|| |                   Player 3's Position (C): Square " + str(squares[2]))
        print("-----------/-/-----------------\ \-----------------------||--")
        print("| 021 | 02/-/ 023 | 024 |/\Z5 | \/6 | 02\-\ 028 | 029 | 0\/ |")
        print("---------/-/------------/ /--------------\-\-----------------")
        print("| 020 | /-/ | 018 | 017/ /016 | 015 | 014 \-\l3 | 012 | 011 |")
        print("----------------------/ /------------------\-\---------------")
        print("| 001 | 002 | 003 | 00\/| 005 | 006 | 007 | \-\ | 009 | 010 |")
        print("-------------------------------------------------------------")

def checker():
    global turn
    for i in range(6):
        pos1 = snakes[i].split("-")
        if squares[turn - 1] == int(pos1[0]):
            squares[turn - 1] = int(pos1[1])
            print("\nSnake! Slid down to square " + str(pos1[1]) + "!")
        pos2 = ladders[i].split("-")
        if squares[turn - 1] == int(pos2[0]):
            squares[turn - 1] = int(pos2[1])
            print("\nLadder! Climbed up to square " + str(pos2[1]) + "!")
        # print("Turn " + str(turn) + ": Checked square " + str(pos1[0] + " and " + str(pos2[0])))
    match turn:
        case 1:
            turn = 2
        case 2:
            turn = 3
        case 3:
            turn = 1
    time.sleep(1.5)
    generate()

generate()

def move():
    global turn
    global view
    os.system("cls")
    print("...\n")
    time.sleep(0.5)
    roll = random.randint(1, 6)
    match turn:
        case 1:
            print("You rolled a " + str(roll) + "!")
            squares[0] += roll
        case 2:
            print("Game Master rolled a " + str(roll) + "!")
            squares[1] += roll
        case 3:
            print("Player 3 rolled a " + str(roll) + "!")
            squares[2] += roll
    checker()
    view = 0



while bool == True:
    request = input("\n\nWhat would you like to do? ")
    if request == "1":
        view = 0
    if request == "2":
        view = 1
    if request == "3":
        request = 8
        move()
    generate()





# I love storing ASCII images

def boarddesigns():
    if view == 0:
        print("-------------------------------------------------------------                   Enter '0' to view the board with numbers")
        print("| 100 | 099 | 098 | 097 | 096 | 095 | 094 | 093 | 092 | 091 |                   Enter '0' to view snakes and ladders on the board.")
        print("-------------------------------------------------------------                   Enter '1' to view pieces on the board.")
        print("| 081 | 082 | 083 | 084 | 085 | 086 | 087 | 088 | 089 | 090 |                   Enter '2' to advance the turn.")
        print("-------------------------------------------------------------")
        print("| 080 | 079 | 078 | 077 | 076 | 075 | 074 | 073 | 072 | 071 |                   Your position: Square " + str(place1))
        print("-------------------------------------------------------------                   Game Master's position: Square " + str(place2))
        print("| 061 | 062 | 063 | 064 | 065 | 066 | 067 | 068 | 069 | 070 |                   Player 3's position: Square " + str(place3))
        print("-------------------------------------------------------------                   Player 4's position: Square " + str(place4))
        print("| 060 | 059 | 058 | 057 | 056 | 055 | 054 | 053 | 052 | 051 |")
        print("-------------------------------------------------------------")
        print("| 041 | 042 | 043 | 044 | 045 | 046 | 047 | 048 | 049 | 050 |")
        print("-------------------------------------------------------------")
        print("| 040 | 039 | 038 | 037 | 036 | 035 | 034 | 033 | 032 | 031 |")
        print("-------------------------------------------------------------")
        print("| 021 | 022 | 023 | 024 | 025 | 026 | 027 | 028 | 029 | 030 |")
        print("-------------------------------------------------------------")
        print("| 020 | 019 | 018 | 017 | 016 | 015 | 014 | 013 | 012 | 011 |")
        print("-------------------------------------------------------------")
        print("| 001 | 002 | 003 | 004 | 005 | 006 | 007 | 008 | 009 | 010 |")
        print("-------------------------------------------------------------")
    elif view == 1:
        print("-------------------------------------------------------------                   Enter '0' to view the board with numbers")
        print("|     | /\  |     |     |     |     |     |  /\ |     |     |                   Enter '1' to view snakes and ladders on the board.")
        print("-------/ /-----------------------------------\ \-------------                   Enter '2' to view pieces on the board.")
        print("|     / /   | /\  |     |/-/  |     |     |   \ \     |     |")
        print("-----/ /-----/ /--------/-/--------------------\ \-----------                   Your position: Square " + str(place1))
        print("|   / /     / /   |    /-/    |     |     |    / /    |     |                   Game Master's position: Square " + str(place2))
        print("----\ \----/ /--------/-/---------------------/ /------------                   Player 3's position: Square " + str(place3))
        print("|    \ \   \ \    |  /-/|     |   \-\     |   \/|     |     |                   Player 4's position: Square " + str(place4))
        print("------\ \---\ \--------------------\-\-----------------------")
        print("|      \ \  |\/   |     |  /\ |     \-\   |     |/-/  |     |")
        print("--------\ \----------------\ \------------------/-/----------")
        print("| |-| |  \/ | /-/ |     |   \ \     |     |    /-/    |  /\ |")
        print("--|-|--------/-/-------------\ \--------------/-/--------||--")
        print("| |-| |     /-/   |     |     \ \   |     |  /-/|     |  || |")
        print("-----------/-/-----------------\ \-----------------------||--")
        print("|     |   /-/     |     |/\   | \/  |   \-\     |     |  \/ |")
        print("---------/-/------------/ /--------------\-\------------- ---")
        print("|     | /-/ |     |    / /    |     |     \-\   |     |     |")
        print("----------------------/ /------------------\-\---------------")
        print("|     |     |     |   \/|     |     |     | \-\ |     |     |")
        print("-------------------------------------------------------------")
    elif view == 2:
        print("-------------------------------------------------------------                   Enter '0' to view the board with numbers")
        print("|     |     |     |     |     |     |     |     |     |     |                   Enter '1' to view snakes and ladders on the board.")
        print("-------------------------------------------------------------                   Enter '2' to view pieces on the board.")
        print("|     |     |     |     |     |     |     |     |     |     |")
        print("-------------------------------------------------------------                   Your position: Square " + str(place1))
        print("|     |     |     |     |     |     |     |     |     |     |                   Game Master's position: Square " + str(place2))
        print("-------------------------------------------------------------                   Player 3's position: Square " + str(place3))
        print("|     |     |     |     |     |     |     |     |     |     |                   Player 4's position: Square " + str(place4))
        print("-------------------------------------------------------------")
        print("|     |     |     |     |     |     |     |     |     |     |")
        print("-------------------------------------------------------------")
        print("|     |     |     |     |     |     |     |     |     |     |")
        print("-------------------------------------------------------------")
        print("|     |     |     |     |     |     |     |     |     |     |")
        print("-------------------------------------------------------------")
        print("|     |     |     |     |     |     |     |     |     |     |")
        print("-------------------------------------------------------------")
        print("|     |     |     |     |     |     |     |     |     |     |")
        print("-------------------------------------------------------------")
        print("|     |     |     |     |     |     |     |     |     |     |")
        print("-------------------------------------------------------------")
    elif view == 3:
        print("-------------------------------------------------------------                   Enter '0' to view snakes and ladders on the board.")
        print("| 100 | /\9 | 098 | 097 | 096 | 095 | 094 | 0/\ | 092 | 091 |                   Enter '1' to pieces on the board.")
        print("-------/ /-----------------------------------\ \-------------                   Enter '2' to advance the turn.")
        print("| 081 / /82 | //3 | 084 |/-/5 | 086 | 087 | 08\ \ 089 | 090 |")
        print("-----/ /-----/ /--------/-/--------------------\ \-----------                   Your position: Square " + str(place1))
        print("| 08/ / 079 / /78 | 077/-/076 | 075 | 074 | 073/ /072 | 071 |                   Game Master's position: Square " + str(place2))
        print("----\ \----/ /--------/-/---------------------/ /------------                   Player 3's position: Square " + str(place3))
        print("| 061\ \O62\ \O63 | 0/-/| 065 | 06\-\ 067 | 06\/| 069 | 070 |                   Player 4's position: Square " + str(place4))
        print("------\ \---\ \--------------------\-\-----------------------")
        print("| 060  \ \9 |\/58 | 057 | 0/\ | 055 \-\S4 | 053 |/-/2 | 051 |")
        print("--------\ \----------------\ \------------------/-/----------")
        print("| |-| | 0\/ | /-/ | 044 | 04\ \ 046 | 047 | 048/-/049 | 0/\ |")
        print("--|-|--------/-/-------------\ \--------------/-/--------||--")
        print("| |-| | 039 /-/38 | 037 | 036 \ /35 | 034 | 0/-/| 032 | 0|| |")
        print("-----------/-/-----------------\ \-----------------------||--")
        print("| 021 | 02/-/ 023 | 024 |/\Z5 | \/6 | 02\-\ 028 | 029 | 0\/ |")
        print("---------/-/------------/ /--------------\-\-----------------")
        print("| 020 | /-/ | 018 | 017/ /016 | 015 | 014 \-\l3 | 012 | 011 |")
        print("----------------------/ /------------------\-\---------------")
        print("| 001 | 002 | 003 | 00\/| 005 | 006 | 007 | \-\ | 009 | 010 |")
        print("-------------------------------------------------------------")

boarddesigns()