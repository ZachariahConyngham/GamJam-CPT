import os, time
import msvcrt


select = 0
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
]


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
        "----------------------------------------------------------------------------"
    )
    print(select)
    print(
        "----------------------------------------------------------------------------"
    )


while True:
    if msvcrt.kbhit():  # Check if a key was hit
        key = msvcrt.getch().decode()
        if key == "w":
            select += 1
        elif key == "s":
            select -= 1
        load()
