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
print("")


while Keys < 3: #total keys needed should be less than the total amount of minigames
    game = "e"
game = str(input("Choose your next challenge: G, H, R")) #write the first letter of the game here, make sure it is different for each game

match game:
    case "G": 
        print("Notfinishedyet") #Gambling game here
    case "H":
        print("Notfinishedyet") #hangman here
    case "R":
        print("Notfinishedyet") #Roshambo here








if Keys == 3:
#final minigame here
    print("Time for your final challenge")