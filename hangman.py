import random, time

words = [
    "POLYMORPHISM",
    "JAZZY",
    "GUZZLER",
    "PNEUMONOULTRAMICROSCOPICSILICOVOLCANOCONIOSIS",
    "CHARGOGGAGOGGMANCHAUGAGGOGGCHAUBUNAGUNGAMAUGG",
    "CLANKER",
    "POLYNOMIAL P(X) = Q(X)A(X) + R(X)",
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
    "JONK",
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
    "You should kill yourself, squiglet.\n",
    "Haha, you're not guessing this one.\n",
    "You've still got many letters to go.\n",
    "You really think you can beat me?\n",
    "HAHAHAHAHAHAHAHAHAHA!!! YOU ABSOLUTELY SUCK!!!\n",
    "Good luck, you're gonna need it.\n",
    "A squiglet like you won't be getting this one.\n",
]
letters = []
alrguess = []
wrong = [""]
guess = ""
mistakes = 4
id = random.randint(0, len(words)) - 1

length = len(words[id])

for line in dialogue:
    time.sleep(1.5)
    print(line)

count = 0
while count < length:
    letters.append("_")
    count += 1

count = 0
for letter in letters:
    if words[id][count].isalpha() == False:
        letters[count] = words[id][count]
    count += 1

print(" ".join(letters))


while "_" in letters and not mistakes < 1:
    guess = ""
    while not len(guess) == 1:
        guess = (input("\nGuess a letter. Or die. I don't mind. ")).upper()
        if guess in alrguess:
            time.sleep(1)
            print("...\n")
            time.sleep(1)
            print("You've already guessed that, squiglet.\n")
            time.sleep(2)
        elif guess.isalpha() == False:
            time.sleep(1)
            print("...\n")
            time.sleep(1)
            print("Little squiglet. Do you know what a letter is? Are you braindead?\n")
            time.sleep(2)
        elif guess == "SOLVE":
            if guess == words[id]:
                break
            else:
                time.sleep(1)
                print("...\n")
                time.sleep(1)
                print(
                    "HAHAHHAHAHAHAH!!! YOU GOT IT WRONG!!! YOU ARE REALLY BAD AT THIS!!!\n"
                )
                time.sleep(2)
                mistakes -= 1
        elif not len(guess) == 1:
            time.sleep(1)
            print("...\n")
            time.sleep(1)
            print("That's not a letter, squiglet. That's multiple letters.\n")
            time.sleep(2)
        else:
            if guess in words[id]:
                time.sleep(1)
                print("...\n")
                time.sleep(1)
                print("Fine. The word contains '" + guess + "'. You happy?\n")
                time.sleep(2)
                start_index = 0
                while True:
                    index = words[id].find(guess, start_index)
                    if index == -1:
                        break
                    letters[index] = guess
                    start_index = index + 1
                alrguess.append(guess)
            else:
                mistakes -= 1
                time.sleep(1)
                print("...\n")
                time.sleep(1)
                print(disrespect[random.randint(0, len(disrespect) - 1)])
                time.sleep(2)
                alrguess.append(guess)

        print(" ".join(letters) + "\n")
        print("Already guessed: " + ", ".join(alrguess))
        print("Errors left: " + str(mistakes))


if mistakes < 1:
    print("You lose!")
else:
    print("You win!")
