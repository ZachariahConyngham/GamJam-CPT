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

matnames = ["Wood", "Water", "Berries", "Fish", "Scraps", "Metal", "Fuel"]
matdesc = [
    "A log of wood that is useful for crafting.",
    "Drinkable water that is great for ensuring you don't die of thirst.",
    "A purple berry that grows on bushes and trees. Very delicious.",
    "A very very normal looking fish. Edible (probably).",
    "A scrap of metal that could be smelted into something useful.",
    "A fully smelted ingot of metal that is vital for crafting.",
    "Fuel for your rocket. Might come in handy later.",
]
mat = [2, 2, 0, 0, 0, 0, 0]


gnnames = ["Trees", "Bushes", "Ponds", "Mines", "Smeltries"]
gndesc = [
    "A normal looking tree that produces plenty of wood and a small chance of berries.",
    "A bush that generates berries for harvesting.",
    "A fishing pond that produces a seemingly infinite amount of fish and water.",
    "A mine that allows you to harvest metal and scraps.",
    "A smeltry that can cook your items to make them better." "",
]
gn = [0, 0, 0, 0, 0]

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

    left_lines = []
    right_lines = []

    print("---------------------------------------------------------------------------")
    cl = "\nCurrent location: " + location
    mn = "Money: $" + str(money) + "\n"
    print(f"{cl:<40}{mn}")

    print(
        "---------------------------------------------------------------------------\n"
    )

    print("Resources:\n\n\n\n\n\n\n\n")

    print(
        "\n----------------------------------------------------------------------------\n"
    )


def update():
    left_lines = []
    right_lines = []

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
        sys.stdout.write(f"\033[{i + 9};{0}H")
        sys.stdout.flush()
        if i < len(right_lines):
            print(f"{left_lines[i]:<40}{right_lines[i]}", flush=True)
        else:
            print(left_lines[i])
    # print("Select: " + str(select) + ", Selectcol: " + str(selectcol))

    sys.stdout.write(f"\033[{19};{0}H")
    sys.stdout.flush()
    print("\033[2K", end="")
    if selectcol == 0:
        print(matdesc[select])
        print("\033[2K", end="")
        print("You currently have: " + str(math.floor(mat[select])))
    else:
        print(gndesc[select])
        print("\033[2K", end="")
        print("You currently own: " + str(math.floor(gn[select])))


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
            case "s":
                select += 1
            case "a":
                selectcol -= 1
            case "d":
                selectcol += 1
        if selectcol == 0:
            select = max(0, min(select, len(mat) - 1))
        else:
            select = max(0, min(select, len(gn) - 1))
        selectcol = max(0, min(selectcol, 1))
    update()
    time.sleep(1 / 50)
    mat[0] += 0.5 * 0.02
