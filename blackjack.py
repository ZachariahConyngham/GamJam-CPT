import random
facecards = ["Jack", "Queen", "King"]
cardsnumber = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
Cards = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
Suits = ["Diamonds", "Spades", "Hearts", "Clubs"]

wins=0
dealertotal = 0
while wins < 10:
    hit = "Y"
    print("The dealer has:")
    if hit == "Y":
        cardnumber = random.choice(cardsnumber)
        dealertotal += cardnumber
        match cardnumber:
            case 1:
                facecard = "Ace"
            case 2:
                facecard = "2"
            case 3:
                facecard = "3"
            case 4:
                facecard = "4"
            case 5:
                facecard = "5"
            case 6:
                facecard = "6"
            case 7:
                facecard = "7"
            case 8:
                facecard = "8"
            case 9:
                facecard = "9"
            case 10:
                facecard = random.choice(facecards)
        print(facecard, "of", random.choice(Suits))

    print("Your cards are:")
    total = 0
    facecard = 0
    while hit == "Y":
        cardnumber = random.choice(cardsnumber)
        total += cardnumber
        match cardnumber:
            case 1:
                facecard = "Ace"
            case 2:
                facecard = "2"
            case 3:
                facecard = "3"
            case 4:
                facecard = "4"
            case 5:
                facecard = "5"
            case 6:
                facecard = "6"
            case 7:
                facecard = "7"
            case 8:
                facecard = "8"
            case 9:
                facecard = "9"
            case 10:
                facecard = random.choice(facecards)
        print(facecard, "of", random.choice(Suits))
        print("Your current total is", total)
        match total:
            case 1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20:
                hit = str(input("Do you want another card? (Y or N)"))
            case 21:
                print("You Win")
                wins += 1
            case _:
                print("You lose")


    while dealertotal < 17:
        print("The Dealers next card is:")
        cardnumber = random.choice(cardsnumber)
        dealertotal += cardnumber
        match cardnumber:
            case 1:
                facecard = "Ace"
            case 2:
                facecard = "2"
            case 3:
                facecard = "3"
            case 4:
                facecard = "4"
            case 5:
                facecard = "5"
            case 6:
                facecard = "6"
            case 7:
                facecard = "7"
            case 8:
                facecard = "8"
            case 9:
                facecard = "9"
            case 10:
                facecard = random.choice(facecards)
        print(facecard, "of", random.choice(Suits))
    if dealertotal > 21:
        print("You win")
    else:
        print("Your total is", total)
        print("The dealers total is", dealertotal)
        if dealertotal < total:
            print("You win")
            wins += 1
        else:
            print("you lose")
print("Congratulations, you have beaten the blackjack minigame")
