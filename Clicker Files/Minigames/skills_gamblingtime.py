import random


def gambling():
    complete = 0
    if complete == 0:
        complete = 0
        UserName = input("What is your name: ")
        print("Hello,", UserName)
        print("Would you like to play a game?")
        print("Try to guess of the number I am thinking of between 0 and 10.")
        print("Have fun!")
        Continyes = "0"
        Continu = "1"
        escape = 0
        Guesses = 0
        number = random.randint(0, 10)
        while Continu == "1":
            Answer = int(input("What number am I thinking of? "))
            if Answer > number:
                print("Try guessing a smaller number")
                Continu = "1"
            else:
                if Answer < number:
                    print("Try guessing a larger number")
                    Continu = "1"
                else:
                    if Answer == number:
                        print("Great job!")
                        print(".")
                        print(".")
                        print(".")
                        print("But I am not done with you yet")
                        Continu = "2"
        number = random.randint(0, 1000)
        print("The answer is between 0 and 1000 this time")
        print("Good Luck")
        while Continu == "2":
            Answer = int(input("What number am I thinking of? "))
            if Answer > number:
                print("Try guessing a smaller number")
                Continu = "2"
            else:
                if Answer < number:
                    print("Try guessing a larger number")
                    Continu = "2"
                else:
                    if Answer == number:
                        print("Took you long enough")
                        print("You've managed to best me twice now.")
                        print("Maybe I'll let you go...")
                        print("If you can manage to best me 1 last time")
                        Continu = "3"
        number = random.randint(0, 1000000)
        print("The answer is between 0 and 1000000")
        print("Good luck")
        print("You will need it this time")
        while Continu == "3":
            Answer = int(input("What number am I thinking of? "))
            if Answer > number:
                print("Try guessing a smaller number")
                Continu = "3"
            else:
                if Answer < number:
                    print("Try guessing a larger number")
                    Continu = "3"
                else:
                    if Answer == number:
                        print("How did you manage to do that?")
                        print("There were a million possible answers.")
                        print("Well a deal is a deal...")
                        print("Enjoy your freedom...")
                        Continu = "0"
        Contino = input("Do you wish to leave? (Y or N)")
        while Contino == "Y":
            escape = 3
            print("Did you really think I would let you escape?")
            print("After you have made a fool of me?")
            print("You will never escape.")
            number = random.randint(0, 1000)
            print("The answer is between 1 and 1000 this time")
        while escape > 0:
            Answer = int(input("What number am I thinking of? "))
            if Answer > number:
                print("Try guessing a smaller number")
            else:
                if Answer < number:
                    print("Try guessing a larger number")
                else:
                    if Answer == number:
                        escape -= 1
                        print("Give up")
                        print("You can't escape")
                        print(escape, "left")
                        if escape == 2:
                            print("What was that?")
                        if escape == 1:
                            print("Why is that number going down?")
        print("Defeated...")
        print("Well done...")
        print("No one has beaten me before...")
        print("As a reward I will give you a hint...")
        print("A Minigame is hidden on each page...")
        print("Look for a hidden M...")
        print("Good Luck...")
        complete = 1

    else:   
        continyo = "Y"
        while continyo == "Y":
            continyo = input(str("Would you like to play again? (Y or N)"))
            Continuo = int(input("What difficulty would you like? (1 to ???) "))
            number = random.randint(0, Continuo)
            Answer = int(input("What number am I thinking of? "))
            if Answer + 10 < number < Answer - 10:
                print("So close, Just 1 or 2 more guesses!")
                Guesses += 1
            else:
                if Answer > number:
                    print("Try guessing a smaller number")
                    Guesses += 1
                else:
                    if Answer < number:
                        print("Try guessing a larger number")
                        Guesses += 1
                    else:
                        if Answer == number:
                            print("Great job!")
                            print("You guessed the number in", Guesses, "Guesses")
                            length = len(str(Guesses))
                            if Guesses < (length * 3):
                                print("sanity buff")
                                #buff here
                            Continyes == input("Would you like to play again? (Y or N)")

