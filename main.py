


Keys = 0


while Keys < 3: #total keys needed should be less than the total amount of minigames
    game = "e"
    input(game("Choose your next challenge: G, H, R")) #write the first letter of the game here, make sure it is different for each game

match game:
    case "G": 
        print("notfinishedyet") #Gambling game here
    case "H":
        print("notfinishedyet") #hangman here
    case "R":
        print("Notfinishedyet") #Roshambo here








if Keys == 3:
#final minigame here
    print("Time for your final challenge")