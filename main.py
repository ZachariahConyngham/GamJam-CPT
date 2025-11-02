
from blackjack import blackjack
import time
Keys = 0


time.sleep(3)
print(".")
time.sleep(3)
print(".")
time.sleep(3)
print(".")
time.sleep(3)

print("Hello")
print("Don't be alarmed")
print("It is just me")
print("I am here to help you")
name = str(input("What is your name?"))
print("The only way for you to escape is to follow my lead")
print("You need to get 3 keys")
print("And then you are free!!!")
print("You must complete 1 challenge per key")



while Keys < 10: #total keys needed should be less than the total amount of minigames
    if Keys > 3:
        game = str(input("Do you want to move on (Y) or try move of the minigames (N), Y or N"))
        if game == "Y":
            Keys = 10
    else:
        game = "e"
    match Keys:
        case 1:
            print("Great Job, you got the first key!!!")
            print("You just need two more until you can escape from these pitiful challenges")
        case 2:
            print("Just 1 key to go!")
            print("I can't wait!")
            print("It is going to be so much fun!")
            print("Go on, get the final key and escape!")

    game = str(input("Choose your next challenge: G, H, R, U, B, B, S")) #write the first letter of the game here, make sure it is different for each game
    match game:
        case "G": 
            print("Notfinishedyet") #Gambling game here
        case "H":
            print("Notfinishedyet") #hangman here
        case "R":
            print("Notfinishedyet") #Roshambo here
        case "U":
            print("Notfinishedyet") #Uno
        case "Bl":
            blackjack() #Blackjack FINISHED AND IMPLEMENTED
            print("nonfinishedyet") #Blackjack
        case "Ba":
            print("nonfinishedyet") #Battleships
        case "S":
            print("nonfinishedyet") #Snakesandladders








if Keys == 3:
    print("Finally!!")
    time.sleep(1)
    print("You have made it")
    time.sleep(1)
    print("All that is left is to leave")
    time.sleep(1)
    print("Go on")
    time.sleep(2)
    print("It is time.")
    time.sleep(1)
    print("At last someone is able to make it to my domain.")
    time.sleep(1)
    print("I have waited eons for this.")
    time.sleep(1)
    print("You thought you would be free?")
    time.sleep(1)
    print("Did you really believe that was all?")
    time.sleep(1)
    print("Foolish mortal.")
    time.sleep(1)
    print("You are just like all the rest.")
    time.sleep(1)
    print("You always believe whatever you are told.")
    time.sleep(1)
    print("Time for your final challenge.")
#final minigame here