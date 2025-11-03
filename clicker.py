import os, time
import msvcrt
import shutil

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
    "(Everything seems the wrong colour.)","(You might have to survive on your own for a while.)"
]
select = 0
selectcol = 0
location = "???"
matnames = ["Wood", "Water", "Berries", "Scraps", "Iron", "Fuel"]
materials = [2, 2, 0, 0, 0, 0] # wood, food, water, scraps, iron, fuel
gnnames = ["Trees", "Bushes"]
gn = [0, 0]

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

    print(
        "----------------------------------------------------------------------------"
    )
    print("\nCurrent location: " + location + "\n\n\n")
    print("Resources: ")
    for i in range(6):
        if materials[i] > 0:
            if select == i and selectcol == 0:
                left_lines.append(f"{matnames[i]}: {materials[i]} <")
            else:
                left_lines.append(f"{matnames[i]}: {materials[i]}")
    for i in range(len(gn)):
        if select == i and selectcol == 1:
            right_lines.append(f"{gnnames[i]}: {gn[i]} <")
        else:
            right_lines.append(f"{gnnames[i]}: {gn[i]}")  

    for i in range(len(left_lines)):
        if i < len(right_lines):
            print(f"{left_lines[i]:<40}{right_lines[i]}")
        else:
            print(left_lines[i])



    print(
        "\n----------------------------------------------------------------------------\n"
    )
    print("Select: " + str(select) + ", Selectcol: " + str(selectcol))




skip = input("Do you want to skip opening dialogue? (Y/N) ").upper()
if skip == "Y":
    for line in dialogue:
        yap(line)
        time.sleep(1)
        print("\n")

load()

while True:
    if msvcrt.kbhit():  # Check if a key was hit
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
        select = max(0, min(select, 5))
        selectcol = max(0, min(selectcol, 1))
        load()
