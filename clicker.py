import os, time, math, sys
import msvcrt
import shutil

os.system("")

dialogue = [
    "...",
    "Hello?",
    "(The room is smoky.)",
    "(You stand up. Your legs are shaking. Your ears are ringing.)",
    "(You cough.)",
    "(You look around. You're in some kind of tube. A spaceship, perhaps?)",
    "(You notice a sliding door in front of you with a big red button next to it.)",
    "(Tempted, you walk forward and press the button.)",
    "(Outside, everything looks... different?)",
    "(Everything seems the wrong colour.)",
    "(You might have to survive on your own for a while.)",
]
select = 0
selectcol = 1
location = "???"


gnnames = ["Market Stand", "Green Grocer", "Car Wash", "McDolands", "Restaurant", "Marketplace", "Warehouse", "Hotel", "Bank", "Casino", "Power Plant"]
gndesc = [
    "A small market stand that will earn you some cash.",
    "A store that sells vegetables for a modest price.",
    "A new brand of Crystal Car Wash that will earn you some bucks.",
    "A factory of minimum wage workers doing the least amount of work possible.",
    "A pristine Italian restaurant that serves only the finest spaghetti.",
    "A large marketplace center that acts as the hub of shopping.",
    "A production warehouse that makes the latest line of toys, games, and everything in between.",
    "A manky has-been hotel that somehow still attracts visitors.",
    "A definitely-not-a-scam bank that prints hard cash.",
    "An illegal gambling facility, only for the elite.",
    "A nuclear power plant. Makes money one way or another.",
]
gn = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
mps = [0.5, 6, 24, 60, 200, 750, 1400, 5500, 18000, 40000, 125000]
cost = [2, 60, 900, 8500, 55000, 240000, 3500000, 20000000, 444444444, 7000000000, 80000000000]
selected = False
ramping = 1.25  # Increase by 25% per purchase

money = 0
day = 0

columns = shutil.get_terminal_size().columns
half = columns // 2


def clear():  # Clears the terminal
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")


def yap(line):  # yappin
    for letter in line:
        print(letter, end="", flush=True)
        time.sleep(0.05)


def shorten(n):
    suffixes = ['', 'k', ' million', ' billion', ' trillion', ' quadrillion', ' quintillion', ' sextillion', ' septillion', ' octillion', ' nonillion']
    if n == 0:
        return '0'
    magnitude = int(math.log10(abs(n)) // 3)
    magnitude = max(0, min(magnitude, len(suffixes) - 1))
    short = n / (10 ** (3 * magnitude))

    if short.is_integer():
        short_str = str(int(short))
    else:
        short_str = f"{short:.2f}".rstrip('0').rstrip('.')
    
    return f"{short_str}{suffixes[magnitude]}"



def load():
    clear()

    print(
        "---------------------------------------------------------------------------\n"
    )

    print("\n")

    print(
        "---------------------------------------------------------------------------\n"
    )

    print("\n")

    print(
        "---------------------------------------------------------------------------\n"
    )

    print("Resources:\n\n\n\n\n\n\n\n\n\n\n")

    print(
        "----------------------------------------------------------------------------\n\n"
    )


def update():
    sys.stdout.write(f"\033[{3};{0}H")
    sys.stdout.flush()

    print(f"{"Settings Menu":<40}{"Settings Menu"}")

    sys.stdout.write(f"\033[{7};{0}H")
    sys.stdout.flush()

    dc = "Current Day: " + str(day)
    mn = "Money: $" + shorten(money)
    print("\033[2K", end="")
    print(f"{dc:<40}{mn}")

    sys.stdout.write(f"\033[{11};{0}H")
    sys.stdout.flush()

    for i in range(len(gn)):
        if select == i and selectcol == 1:
            print(
                f"{gnnames[i] + ": " + str(math.floor(gn[i])) + " <     "}"
            )
        else:
            print(
                f"{gnnames[i] + ": " + str(math.floor(gn[i]))}" + "     "
            )

    # for i in range(len(left_lines)):
        # sys.stdout.write(f"\033[{i + 13};{0}H")
        # sys.stdout.flush()
        # if i < len(right_lines):
            # print(f"{left_lines[i]:<40}{right_lines[i]}", flush=True)
        # else:
            # print(left_lines[i])
    # print("Select: " + str(select) + ", Selectcol: " + str(selectcol))

    sys.stdout.write(f"\033[{24};{0}H")
    sys.stdout.flush()
    print("\033[2K", end="")
    if selected == False:
        print(gndesc[select])
        print("\033[2K", end="")
        print("You currently own: " + str(math.floor(gn[select])) + " (Producing $" + shorten(mps[select] * gn[select]) + " per second)")
        print("\033[2K", end="")
    else:
        if money >= cost[select] * (ramping ** gn[select]):
            print(
                "Buy one for $"
                + shorten(cost[select] * (ramping ** gn[select]))
                + "? (SPACE to confirm, X to cancel)"
            )
        else:
            print(
                "Buy one for $"
                + shorten(cost[select] * (ramping ** gn[select]))
                + "? (Just kidding you're way too poor to afford that loser)"
            )
        print("\033[2K", end="")
        print("\033[2K", end="")


skip = input("Do you want to skip opening dialogue? (Y/N) ").upper()
if skip == "Y":
    for line in dialogue:
        yap(line)
        time.sleep(1)
        print("\n")

# where the running actually starts

load()
print("\033[?25l", end="")

while True:
    if msvcrt.kbhit():  # Key check
        key = msvcrt.getch().decode()
        match key:
            case "w":
                select -= 1
                selected = False
            case "s":
                select += 1
                selected = False
            case "a":
                selectcol -= 1
                selected = False
            case "d":
                selectcol += 1
                selected = False
            case " ":
                if selectcol == 1:
                    if selected == False:
                        selected = True
                    else:
                        selected = False
                        if money >= cost[select] * (ramping ** gn[select]):
                            money -= round(cost[select] * (ramping ** gn[select]), 2)
                            gn[select] += 1
            case "x":
                if selected == True:
                    selected = False
        if selectcol == 1:
            select = max(0, min(select, len(gn) - 1))
        selectcol = max(1, min(selectcol, 1))
    update()
    time.sleep(1 / 50)

    for i in range(len(gn)):
        money += mps[i] * gn[i] * 0.02
