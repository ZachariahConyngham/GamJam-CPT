from blackjack import blackjack

bald = 1
value = 0
minigame = "N/A"

if value > 500:
    minigametime = str(input("Would you like to play a game for a boost to a material? Y/N"))
else:
    minigametime = "N"





while minigametime == "Y":
    minigame = str(input("WHat material would you to wager? x, y, z "))
    match minigame:
        case "x":
            blackjack()
        case "y":
            ROSHAMBO()
        case "z":
            numberguess()

