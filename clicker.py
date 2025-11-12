import os, time, math, sys
import msvcrt

# from Minigames import snakes_ladders, ROSHAMBO, hangman, blackjack


opndialogue = [
    "...",
    "(You haven't bothered to add any dialogue intro yet.)",
    "(Very smart.)",
]
select = 0
selectcol = 0
location = "???"


gnnames = [
    "Market Stand",
    "Green Grocer",
    "Car Wash",
    "McDolands",
    "Restaurant",
    "Marketplace",
    "Warehouse",
    "Hotel",
    "Bank",
    "Casino",
    "Power Plant",
]
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
bmps = [0.5, 6, 24, 60, 200, 750, 1400, 5500, 18000, 40000, 125000]
mps = [0.5, 6, 24, 60, 200, 750, 1400, 5500, 18000, 40000, 125000]
cost = [
    2,
    60,
    900,
    8500,
    55000,
    240000,
    3500000,
    50000000,
    444444444,
    7000000000,
    80000000000,
]
selected = False
ramping = 1.25  # Base - Increase by 25% per purchase

minigames = [
    "Roshambo",
    "Snakes and Ladders",
    "Blackjack",
    "Hangman",
    "Guess the number",
]

upg = [
    "More Cash",
    "Marketing Increase",
    "Better Fruits",
    "Exquisite Soap",
    "Overworking",
    "Golden Spaghetti",
    "Trading Hub",
    "Child Labour",
    "Red House Monopoly",
    "Thousand Dollar Bills",
    "104-Card Deck",
    "Radioactive Waste",
    "Increased Profits",
]
upgdesc = [
    "Like money? Here's some more!",
    "More marketing = more money. Simple as that.",
    "Finer fruits sell for more profits.",
    "These cars are gonna be eaten off when you're done with them.",
    "The sentient corn bricks are going to be working overtime.",
    "As you all know, real Italian spaghetti was made with minerals.",
    "The hub of all trade - one might call it a trading hub.",
    "Who doesn't love a pinch of child labour?",
    "You already know that landing here is going to charge $2000 at best.",
    "Condensed bills will make your stacks worth more.",
    "How cooked would a poker game be with two decks as one?",
    "The more radioactive it is, the more it sells for.",
    "Cash moneys.",
]
upgcost = [
    750,
    2800,
    17500,
    80000,
    900000,
    7500000,
    38000000,
    144000000,
    750000000,
    9000000000,
    85000000000,
    240000000000,
    6500000000000,
]
upgab = [
    "a-2",
    "0-2",
    "1-2",
    "2-2",
    "3-2",
    "4-2",
    "5-2",
    "6-2",
    "7-2",
    "8-2",
    "9-2",
    "10-2",
    "a-3",
]
bought = []


money = 0
day = 0
page = 0
sanity = 0


def clear():  # Clears the terminal
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")


def yap(line):  # yappin
    for letter in line:
        print(letter, end="", flush=True)
        time.sleep(0.05)


def shorten(n):  # shortens numbers so that they are readable
    suffixes = [
        "",
        "k",
        " million",
        " billion",
        " trillion",
        " quadrillion",
        " quintillion",
        " sextillion",
        " septillion",
        " octillion",
        " nonillion",
        " decillion",
        " undecillion",
        " duodecillion",
        " tredecillion",
        " quattuordecillion",
        " quindecillion",
        " sexdecillion",
        " septendecillion",
        " octodecillion",
        " novemdecillion",
        " vigintillion",
        " unvigintillion",
        " duovigintillion",
        " quattuorvigintillion",
        " quinvigintillion",
        " sexvigintillion",
        " septvigintillion",
        " octovigintillion",
        " novemvigintillion",
        " trigintillion",
    ]
    if n == 0:
        return "0"
    magnitude = int(math.log10(abs(n)) // 3)
    magnitude = max(0, min(magnitude, len(suffixes) - 1))
    short = n / (10 ** (3 * magnitude))

    if short.is_integer():
        short_str = str(int(short))
    else:
        short_str = f"{short:.2f}".rstrip("0").rstrip(".")

    return f"{short_str}{suffixes[magnitude]}"


def load():
    clear()

    print("---------------------------------------------------------------------------")

    print("\n\n")

    print("---------------------------------------------------------------------------")

    print("\n\n")

    print("---------------------------------------------------------------------------")

    print("\n\n\n\n\n\n\n\n\n\n\n\n")

    print("---------------------------------------------------------------------------")

    print("\n\n\n\n")

    print("---------------------------------------------------------------------------")


def update():
    sys.stdout.write(f"\033[{3};{0}H")
    sys.stdout.flush()

    print("\033[2K", end="")
    if select == -1:
        match selectcol:
            case 0:
                print(f"{"Main <":<30}{"Upgrades":<30}{"Minigames"}")
            case 1:
                print(f"{"Main":<30}{"Upgrades <":<30}{"Minigames"}")
            case 2:
                print(f"{"Main":<30}{"Upgrades":<30}{"Minigames <"}")
    else:
        print(f"{"Main":<30}{"Upgrades":<30}{"Minigames"}")

    sys.stdout.write(f"\033[{7};{0}H")
    sys.stdout.flush()

    dc = "Current Day: " + str(day)
    mn = "Money: $" + shorten(money)
    print("\033[2K", end="")
    print(f"{dc:<40}{mn}")

    if page == 0:  # Main page
        sys.stdout.write(f"\033[{11};{0}H")
        sys.stdout.flush()

        for i in range(len(gn)):
            if select == i and i != -1 and selectcol == 0:
                print(f"{gnnames[i] + ": " + str(math.floor(gn[i])) + " <     "}")
            else:
                print(f"{gnnames[i] + ": " + str(math.floor(gn[i]))}" + "     ")

        # for i in range(len(left_lines)):
        # sys.stdout.write(f"\033[{i + 13};{0}H")
        # sys.stdout.flush()
        # if i < len(right_lines):
        # print(f"{left_lines[i]:<40}{right_lines[i]}", flush=True)
        # else:
        # print(left_lines[i])
        # print("Select: " + str(select) + ", Selectcol: " + str(selectcol))
        sys.stdout.write(f"\033[{25};{0}H")
        sys.stdout.flush()
        print("\033[2K", end="")
        if selected == False:
            if select != -1:
                print(gndesc[select])
                print("\033[2K", end="")
                print(
                    "You currently own: "
                    + str(math.floor(gn[select]))
                    + " (Producing $"
                    + shorten(mps[select] * gn[select])
                    + " per second)"
                )
                print("\033[2K", end="")
                print(
                    "(Next one costs $"
                    + shorten(cost[select] * (ramping ** gn[select]))
                    + ")"
                )
            else:
                print("\033[2K")
                print("\033[2K")
                print("\033[2K")
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
            print("\033[2K")
            print("\033[2K")

    if page == 1:  # Upgrades page
        sys.stdout.write(f"\033[{11};{0}H")
        sys.stdout.flush()
        for i in range(11):
            print("\033[2K", end="")
            if i < len(upg):
                if selectcol == 0 and i == select:
                    print(upg[i] + " ($" + shorten(upgcost[i]) + ") <")
                else:
                    print(upg[i] + " ($" + shorten(upgcost[i]) + ")")

        sys.stdout.write(f"\033[{25};{0}H")
        sys.stdout.flush()
        print("\033[2K", end="")

        if select != -1:
            print(upgdesc[select])
            print("\033[2K", end="")
            up = upgab[select].split("-")
            if up[0] != "a" and up[0] is not None:
                print(gnnames[int(up[0])] + " - x" + up[1] + " production")
            else:
                print("All generators - x" + up[1] + " production")
            print(len(bought))
            print(str(select) + " " + str(selectcol))

        print("\033[2K")
        print("\033[2K")

    if (
        page == 2
    ):  # Minigames (ZAC) hereeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        sys.stdout.write(f"\033[{11};{0}H")
        sys.stdout.flush()
        for yap in minigames:
            print(yap)


# where the running actually starts


skip = input("Do you want to skip opening dialogue? (Y/N) ").upper()
if skip != "Y":
    clear()
    for line in opndialogue:
        yap(line)
        time.sleep(1)
        print("\n")

load()
print("\033[?25l", end="")  # Hides the player cursor

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
                if page == 0 and selectcol == 0 and select != -1:
                    if selected == False:
                        selected = True
                    else:
                        selected = False
                        if money >= cost[select] * (ramping ** gn[select]):
                            money -= round(cost[select] * (ramping ** gn[select]), 2)
                            gn[select] += 1
                if page == 1 and selectcol == 0 and select != -1:
                    if money >= upgcost[select]:
                        money -= round(upgcost[select], 2)
                        bought.append(upgab[select])
                        upg.remove(upg[select])
                        upgcost.remove(upgcost[select])
                        upgdesc.remove(upgdesc[select])
                        upgab.remove(upgab[select])
                if select == -1:
                    load()
                    match selectcol:
                        case 0:
                            page = 0
                        case 1:
                            page = 1
                        case 2:
                            page = 2
            case "x":
                if selected == True:
                    selected = False
            case "r":
                load()
        if selectcol == 0:
            if page == 0:
                select = max(-1, min(select, len(gn) - 1))
            if page == 1:
                if len(upg) < 11:
                    select = max(-1, min(select, len(upg) - 1))
                else:
                    select = max(-1, min(select, 10))
        if select == -1:
            selectcol = max(0, min(selectcol, 2))
        else:
            selectcol = max(0, min(selectcol, 0))
    update()
    time.sleep(1 / 50)

    for i in range(len(gn)):
        mult = 1
        if i < len(bought):
            for index in bought:
                index1 = bought[i].split("-")
                if index1[0] == "a":
                    mult *= int(index1[1])
                elif i == int(index1[0]):
                    mult *= int(index1[1])
                mps[i] = bmps[i] * mult

        money += mps[i] * gn[i] * 0.02
