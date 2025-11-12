import os, time
import random


def ROSHAMBO():
    def clear():  # Clears the terminal
        if os.name == "nt":
            _ = os.system("cls")
        else:
            _ = os.system("clear")

    def yap(line):  # yappin
        for letter in line:
            print(letter, end="", flush=True)
            time.sleep(0.05)

    yap("Well")
    time.sleep(0.25)
    yap("Well")
    time.sleep(0.25)
    yap("Well")
    time.sleep(2)
    yap(".")
    time.sleep(1)
    yap(".")
    time.sleep(1)
    yap(".")
    time.sleep(1)
    yap("A little bird has fallen from its nest")
    time.sleep(1)

    yap(".")
    time.sleep(1)
    yap(".")
    time.sleep(1)
    yap(".")
    time.sleep(1)

    yap("What a shame")
    time.sleep(1)
    yap(".")
    time.sleep(1)
    yap(".")
    time.sleep(1)
    yap(".")
    time.sleep(1)
    clear()
    yap("Maybe I could help you little bird")
    time.sleep(1)
    yap("But you would have to something for me")
    time.sleep(1)
    yap("How about we play a little game?")
    time.sleep(1)
    yap("Have you heard of the game Roshambo?")
    time.sleep(1)
    yap("It is a simple game")
    time.sleep(1)
    yap("You and I will both choose either rock, scissors or paper")
    time.sleep(1)
    yap("Rock beats scissors")
    time.sleep(1)
    yap("Scissors beats paper")
    time.sleep(1)
    yap("and Paper beats rock")
    time.sleep(1)
    yap("If you win")
    time.sleep(1)
    yap("I'll give you the key you need to get up")
    time.sleep(1)
    yap("if you lose...")
    time.sleep(1)
    yap("How about we get to that later...")
    time.sleep(1)
    yap("Lets begin...")
    clear()

    wins = 0
    while wins < 5:
        answer = "N"
        roshambolist = ["R", "S", "P"]
        answer = str(input("Choose... S for scissors... R for rock... and P for paper"))
        match answer:
            case "R":
                entity1answer = random.choice(roshambolist)
                match entity1answer:
                    case "R":
                        yap("I choose Rock")
                        yap("It's a tie")
                        wins += 0
                    case "S":
                        yap("I choose Scissors")
                        yap("You win this round...")
                        wins += 1
                    case "P":
                        yap("I choose Paper")
                        yap("You lost this round")
                        wins = 0
            case "S":
                entity1answer = random.choice(roshambolist)
                match entity1answer:
                    case "R":
                        yap("I choose Rock")
                        yap("You lost this round")
                        wins = 0
                    case "S":
                        yap("I choose Scissors")
                        yap("It's a tie")
                        wins += 0
                    case "P":
                        yap("I choose Paper")
                        yap("You win this round...")
                        wins += 1
            case "P":
                entity1answer = random.choice(roshambolist)
                match entity1answer:
                    case "R":
                        yap("I choose Rock")
                        yap("You win this round...")
                        wins += 1
                    case "S":
                        yap("I choose Scissors")
                        yap("You lost this round")
                        wins = 0
                    case "P":
                        yap("I choose Paper")
                        yap("It's a tie")
                        wins += 0
        clear()

    yap("Congratulations")
    yap("You beat me fair and square")
    yap("Here is your key")
    yap("I have one last request though")
    yap("Be weary of the one who guides you")
    yap("He is not the helper he seems to be")
    yap("Good luck, little bird")
    clear()
