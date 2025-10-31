import random

words = [
    "MEGA KNIGHT",
    "POLYMORPHISM",
    "JAZZY",
    "GUZZLER",
    "PNEUMONOULTRAMICROSCOPICSILICOVOLCANOCONIOSIS",
    "CHARGOGGAGOGGMANCHAUGAGGOGGCHAUBUNAGUNGAMAUGG",
    "QQQQQQ",
    "CLANKER",
    "SCHLORPWIGGLERMANG",
    "GOONTARD",
    "SIX SEVEN",
    "HOLLOW KNIGHT: SILKSONG",
    "B",
    "QWERTYUIOP",
    "ABSOLUTE RADIANCE",
    "SEISMOGRAPH",
    "BEAN",
]
name = input("What is your name? ")
letters = []
alrguess = []
wrong = [""]
guess = ""
mistakes = 6
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

print(" ".join(letters))


def guessletter():
    print("yes")


while "_" in letters and not mistakes < 1:
    guess = ""
    while not len(guess) == 1:
        guess = (input("\nGuess a letter. ")).upper()
        if not len(guess) == 1:
            print("That's not a letter. Try again. ")
        elif guess in alrguess:
            print("Letter has already been guessed.")
        elif guess.isalpha() == False:
            print("Broseph that is NOT a letter.")
        else:
            if guess in words[id]:
                print("The word contains a '" + guess + "'.")
                start_index = 0
                while True:
                    index = words[id].find(guess, start_index)
                    if index == -1:
                        break
                    letters[index] = guess
                    start_index = index + 1
                alrguess.append(guess)
            else:
                print("The word does not contain a '" + guess + "'.")
                mistakes -= 1
                alrguess.append(guess)

        print(" ".join(letters))
        print("Already guessed: " + ", ".join(alrguess))
        print("Errors left: " + str(mistakes))


if mistakes < 1:
    print("You lose!")
else:
    print("You win!")
