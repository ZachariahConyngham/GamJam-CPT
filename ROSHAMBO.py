import time
import random

print("Well")
time.sleep(0.25)
print("Well")
time.sleep(0.25)
print("Well")
time.sleep(2)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print("A little bird has fallen from its nest")
time.sleep(1)

print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)

print("What a shame")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)

print("Maybe I could help you little bird")
time.sleep(1)
print("But you would have to something for me")
time.sleep(1)
print("How about we play a little game?") 
time.sleep(1)
print("Have you heard of the game Roshambo?")
time.sleep(1)
print("It is a simple game")
time.sleep(1)
print("You and I will both choose either rock, scissors or paper")
time.sleep(1)
print("Rock beats scissors")
time.sleep(1)
print("Scissors beats paper")
time.sleep(1)
print("and Paper beats rock")
time.sleep(1)
print("If you win")
time.sleep(1)
print("I'll give you the key you need to get up")
time.sleep(1)
print("if you lose...")
time.sleep(1)
print("How about we get to that later...")
time.sleep(1)
print("Lets begin...")

wins = 0
while wins < 10:
    answer = "N"
    roshambolist = ["R", "S", "P"]
    answer = str(input("Choose... S for scissors... R for rock... and P for paper"))

    match answer:
        case "R":
            entity1answer = random.choice(roshambolist)
            match entity1answer:
                case "R":
                    wins += 0
                case "S":
                    wins += 1
                case "P":
                    wins = 0
        case "S":
            entity1answer = random.choice(roshambolist)
            match entity1answer:
                case "R":
                    wins = 0
                case "S":
                    wins += 0
                case "P":
                    wins += 1
        case "P":
            entity1answer = random.choice(roshambolist)
            match entity1answer:
                case "R":
                    wins += 1
                case "S":
                    wins = 0
                case "P":
                    wins += 0

print("Congratulations")
print("You beat me fair and square")
print("Here is your key")
print("I have one last request though")
print("Be weary of the one who guides you")
print("He is not the helper he seems to be")
print("Good luck, little bird")