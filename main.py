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
print("The only way for you to escape is to follow my lead")
print("You need to get 3 keys")
print("And then you are free!!!")
print("You must complete 1 challenge per key")



while Keys < 3: #total keys needed should be less than the total amount of minigames
    game = "e"
    match Keys:
        case 1:
            print("Great Job, you got the first key!!!")
            print("You just need two more until you can escape from these pitiful challenges")
        case 2:
            print("Juat 1 key to go!")
            print("I can't wait!")
            print("It is going to be so much fun!")
            print("Go on, get the final key and escape!")

    game = str(input("Choose your next challenge: G, H, R")) #write the first letter of the game here, make sure it is different for each game
    match game:
        case "G": 
            print("Notfinishedyet") #Gambling game here
        case "H":
            print("Notfinishedyet") #hangman here
        case "R":
            print("Notfinishedyet") #Roshambo here








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