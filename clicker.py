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
selectcol = 0
location = "???"

matnames = ["Wood", "Berries", "Water", "Fish", "Scraps", "Metal", "Fuel"]
matdesc = [
    "A log of wood that is useful for crafting.",
    "A purple berry that grows on bushes and trees. Very delicious.",
    "Drinkable water that is great for ensuring you don't die of thirst.",
    "A very very normal looking fish. Edible (probably).",
    "A scrap of metal that could be smelted into something useful.",
    "A fully smelted ingot of metal that is vital for crafting.",
    "Fuel for your rocket. Might come in handy later.",
]
mat = [0, 0, 0, 0, 0, 0, 0]
mps = [0, 0, 0, 0, 0, 0, 0]
value = [1, 1.5, 1.5, 3, 8, 40, 15]


gnnames = ["Trees", "Bushes", "Ponds", "Mines", "Supermarkets"]
gndesc = [
    "A normal looking tree that produces plenty of wood and a small chance of berries.",  # 0.5 wood, 0.1 berries
    "A bush that generates berries for harvesting.",  # 0.5 berries
    "A fishing pond that produces a seemingly infinite amount of fish and water.",  # 0.5 water, 0.2 fish
    "A mine that allows you to harvest metal and scraps.",  # 0.5 scraps, 0.025 metal
    "A market that produces literally anything and everything ever.",  # 0.5 wood/berries/water, 0.25 fish/scraps, 0.01 metal
]
gn = [1, 0, 0, 0, 0]
cost = [3, 15, 80, 350, 1400, 16400, 60000, 240000, 1350000, 8000000]
selected = False
autosell = False
ramping = 1.25  # Increase by 25% per purchase

money = 0

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

    print("Resources:\n\n\n\n\n\n\n\n\n")

    print(
        "----------------------------------------------------------------------------\n\n"
    )


def update():
    left_lines = []
    right_lines = []

    sys.stdout.write(f"\033[{3};{0}H")
    sys.stdout.flush()

    print(f"{"Autosell: False":<40}{"Settings Menu"}")

    sys.stdout.write(f"\033[{6};{0}H")
    sys.stdout.flush()

    cl = "\nCurrent location: " + location
    mn = "Money: $" + str(round(money, 2)) + "\n"
    print(f"{cl:<40}{mn}")

    for i in range(len(mat)):
        if select == i and selectcol == 0:
            left_lines.append(
                f"{matnames[i] + ": " + str(math.floor(mat[i])) + " <     "}"
            )
        else:
            left_lines.append(
                f"{matnames[i] + ": " + str(math.floor(mat[i]))}" + "     "
            )

    for i in range(len(gn)):
        if select == i and selectcol == 1:
            right_lines.append(
                f"{gnnames[i] + ": " + str(math.floor(gn[i])) + " <     "}"
            )
        else:
            right_lines.append(
                f"{gnnames[i] + ": " + str(math.floor(gn[i]))}" + "     "
            )

    for i in range(len(left_lines)):
        sys.stdout.write(f"\033[{i + 13};{0}H")
        sys.stdout.flush()
        if i < len(right_lines):
            print(f"{left_lines[i]:<40}{right_lines[i]}", flush=True)
        else:
            print(left_lines[i])
    # print("Select: " + str(select) + ", Selectcol: " + str(selectcol))

    sys.stdout.write(f"\033[{23};{0}H")
    sys.stdout.flush()
    print("\033[2K", end="")
    if selected == False:
        if selectcol == 0:
            print(matdesc[select])
            print("\033[2K", end="")
            print("You currently have: " + str(math.floor(mat[select])))
            print("\033[2K", end="")
            print(
                "Producing: "
                + str(mps[select])
                + " per second ($"
                + str(round(mps[select] * value[select], 2))
                + " per second)"
            )
        else:
            print(gndesc[select])
            print("\033[2K", end="")
            print("You currently own: " + str(math.floor(gn[select])))
            print("\033[2K", end="")
    else:
        if money >= cost[select] * (ramping ** gn[select]):
            print(
                "Buy one for $"
                + str(round(cost[select] * (ramping ** gn[select]), 2))
                + "? (SPACE to confirm, X to cancel)"
            )
        else:
            print(
                "Buy one for $"
                + str(round(cost[select] * (ramping ** gn[select]), 2))
                + "? (Just kidding you're way too poor to afford that loser)"
            )
        print("\033[2K", end="")
        print("\033[2K", end="")

    mps[0] = (gn[0] * 0.5) + (gn[4] * 0.5)
    mps[1] = (gn[0] * 0.1) + (gn[1] * 0.5) + (gn[4] * 0.5)
    mps[2] = (gn[2] * 0.5) + (gn[4] * 0.5)
    mps[3] = (gn[2] * 0.2) + (gn[4] * 0.25)
    mps[4] = (gn[3] * 0.5) + (gn[4] * 0.25)
    mps[5] = (gn[3] * 0.02) + (gn[4] * 0.01)
    mps[6] = 0


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
                else:
                    money += value[select] * math.floor(mat[select])
                    mat[select] -= math.floor(mat[select])
            case "x":
                if selected == True:
                    selected = False
        if selectcol == 0:
            select = max(0, min(select, len(mat) - 1))
        else:
            select = max(0, min(select, len(gn) - 1))
        selectcol = max(0, min(selectcol, 1))
    update()
    time.sleep(1 / 50)

    for i in range(len(mat)):
        if autosell == False:
            mat[i] += mps[i] * 0.02
        else:
            money += mps[i] * 0.02 * value[i]
