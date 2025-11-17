import random, time, sys, os


def hangthatman():
    words = [
        "POLYMORPHISM",
        "JAZZY",
        "GUZZLER",
        "PNEUMONOULTRAMICROSCOPICSILICOVOLCANOCONIOSIS",
        "LAKE CHARGOGGAGOGGMANCHAUGAGGOGGCHAUBUNAGUNGAMAUGG",
        "CLANKER",
        "POLYNOMIAL",
        "SIX SEVEN",
        "SEISMOGRAPH",
        "BEAN",
        "GULAG",
        "BLUEPRINT",
        "PHLEGM",
        "DERMATOGLYPHICS",
        "FLOCCINAUCINIHILIPILIFICATION",
        "INCOMPREHENSIBILITIES",
        "PERMANENT",
        "MEXICO",
        "BALLOON",
        "K-POP DEMON HUNTERS",
        "NAPOLEON BONAPARTE",
        "FORT STREET HIGH SCHOOL",
        "TRIGONOMETRY",
        "AMONG US",
        "AZURE",
        "EMBEZZLE",
        "FJORD",
        "FLAPJACK",
        "CALIPH",
        "EUOUAE",
        "ASKEW",
        "ALLEGRETTO",
        "PEMULWUY",
        "DECRESCENDO",
        "HOLLOW KNIGHT",
        "SILKSONG",
        "THERE IS AN IMPOSTER AMONG US",
        "COMPUTING",
        "YI PING",
        "ZOTE",
        "THE QUICK BROWN FOX JUMPS OVER THE LADY DOG",
        "BALATRO",
        "PRACTICE",
        "PRACTISE",
        "2ND SEPTEMBER 1666",
    ]
    dialogue = [
        "...\n",
        "Hello there, squiglet.\n",
        "I see you've challenged me to a game.\n",
        "Well, the game we're gonna be playing today...\n",
        "...is Hangman. Childhood favourite, litte squiglet?\n",
        "I hate to break it to you, little squiglet, but you're NOT beating me.\n",
        "Well then...\n",
        "Shall we play, little squiglet? What do you say?\n",
        "Rules?\n",
        "Guess a letter. If you can't guess the word, you lose.\n",
        "But, if you want to solve...\n",
        "Type 'solve', I'll let you take the floor.\n",
        "Good luck, squiglet.\n",
    ]
    disrespect = [
        "You're not worth my time, squiglet.\n",
        "Haha, you're not guessing this one.\n",
        "You've still got many letters to go.\n",
        "You really think you can beat me?\n",
        "HAHAHAHAHAHAHAHAHAHA!!! YOU ABSOLUTELY SUCK!!!\n",
        "Good luck, you're gonna need it.\n",
        "A squiglet like you won't be getting this one.\n",
        "How'd you guess such an abhorrent letter, squiglet? WRONG!\n",
        "You might need to consider getting better.\n",
        "I despise you for that guess.\n",
    ]
    letters = []
    alrguess = []
    wrong = [""]
    guess = ""
    mistakes = 7
    wins = 0
    maxwins = 3
    id = random.randint(0, len(words)) - 1

    length = len(words[id])

    count = 0
    while count < length:
        letters.append("_")
        count += 1

    count = 0
    for letter in letters:
        if words[id][count].isalpha() == False:
            letters[count] = words[id][count]
        count += 1

    def generate():
        os.system("cls")
        print(" ".join(letters) + "\n")
        print("Already guessed: " + ", ".join(alrguess))
        print("Errors left: " + str(mistakes))
        print("Games won: " + str(wins) + "/" + str(maxwins))

    generate()

    while "_" in letters and not mistakes < 1:
        guess = ""
        while not len(guess) == 1:
            guess = (input("\nGuess a letter. Or die. I don't mind. ")).upper()
            if guess in alrguess:
                os.system("cls")
                time.sleep(1)
                print("...\n")
                time.sleep(1)
                print("You've already guessed that, squiglet.\n")
                time.sleep(3)
            elif guess.isalpha() == False:
                os.system("cls")
                time.sleep(1)
                print("...\n")
                time.sleep(1)
                print(
                    "Little squiglet. Do you know what a letter is? Are you braindead?\n"
                )
                time.sleep(3)
            elif guess == "SOLVE":
                os.system("cls")
                time.sleep(1)
                print("...\n")
                time.sleep(1)
                print("You wanna solve? Good luck, squiglet.\n")
                time.sleep(1)
                solve = input("Guess here: ").upper()
                if solve == words[id]:
                    os.system("cls")
                    print("You win.\n")
                    wins += 1
                    time.sleep(1)
                    if wins == 1:
                        print("But you're not done yet.\n")
                        time.sleep(1)
                        print("You best me three times, I let you go.\n")
                    elif wins == 2:
                        print("You're still not done though.\n")
                        time.sleep(1)
                        print(
                            "I said THREE games. One left. And only "
                            + str(mistakes)
                            + " errors to go.\n"
                        )
                    elif wins == 3:
                        print("You win the game.\n")
                        time.sleep(1)
                        print("Leave.\n")
                        time.sleep(1)
                        print("Come again later. If you want, squiglet.\n")
                        time.sleep(1)
                        print("We've got many more games to play.\n")
                        time.sleep(4)
                        sys.end()
                    time.sleep(3)
                    id = random.randint(0, len(words)) - 1
                    letters.clear()
                    alrguess.clear()
                    count = 0
                    length = len(words[id])
                    while count < length:
                        letters.append("_")
                        count += 1
                else:
                    os.system("cls")
                    time.sleep(1)
                    print("...\n")
                    time.sleep(1)
                    print(
                        "HAHAHHAHAHAHAH!!! YOU GOT IT WRONG!!! YOU ARE REALLY BAD AT THIS!!!\n"
                    )
                    time.sleep(2)
                    mistakes -= 1
            elif not len(guess) == 1:
                os.system("cls")
                time.sleep(1)
                print("...\n")
                time.sleep(1)
                print("That's not a letter, squiglet. That's multiple letters.\n")
                time.sleep(3)
            else:
                if guess in words[id]:
                    os.system("cls")
                    time.sleep(1)
                    print("...\n")
                    time.sleep(1)
                    print("Fine. The word contains '" + guess + "'. You happy?\n")
                    time.sleep(2)
                    start_index = 0
                    index = 0
                    while True:
                        index = words[id].find(guess, start_index)
                        if index == -1:
                            break
                        print(index)
                        letters[index] = guess
                        start_index = index + 1
                    alrguess.append(guess)
                else:
                    os.system("cls")
                    mistakes -= 1
                    time.sleep(1)
                    print("...\n")
                    time.sleep(1)
                    print(disrespect[random.randint(0, len(disrespect) - 1)])
                    time.sleep(3)
                    alrguess.append(guess)
            generate()

    print("YOU LOSE, SQUIGLET!!! HAHAHAHHHAH!")
    print(
        "By the way, the word was " + words[id] + ". How'd you even fail that? Goodbye."
    )
