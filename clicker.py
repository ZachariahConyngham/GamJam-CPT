import os, time, math, sys, copy
import msvcrt

from Minigames import (
    hangman,
    blackjack,
    ROSHAMBO,
    snakes_ladders,
    skills_gamblingtime,
)


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
gnart = [
    [
        "-------------------------------------",
        "|                                   |",
        "|          _┌┬┬┬┬┬┬┬┬┬┬┬┬┬┐         |",
        "|         |\|    Market   |         |",
        "|         | ╞╧╧╧╧╧╧╧╧╧╧╧╧╧╡         |",
        "|         | |     (ö)     |         |",
        "|         |\|     {█}     |         |",
        "|_________| ╞‡‡‡‡‡‡‡‡‡‡‡‡‡╡_________|",
        "|          \[_____________]         |",
        "|                                   |",
        "-------------------------------------",
    ],
    [
        "-------------------------------------",
        "|                +-^-+              |",
        "|                ┘ ⌂ └              |",
        "|            Green Grocery          |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "-------------------------------------",
    ],
    [
        "-------------------------------------",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "-------------------------------------",
    ],
    [
        "-------------------------------------",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "-------------------------------------",
    ],
    [
        "-------------------------------------",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "-------------------------------------",
    ],
    [
        "-------------------------------------",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "-------------------------------------",
    ],
    [
        "-------------------------------------",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "-------------------------------------",
    ],
    [
        "-------------------------------------",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "-------------------------------------",
    ],
    [
        "-------------------------------------",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "-------------------------------------",
    ],
    [
        "-------------------------------------",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "-------------------------------------",
    ],
    [
        "-------------------------------------",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "|                                   |",
        "-------------------------------------",
    ],
]
print("------------------------------------------")
print("|                                        |")
print("|                                        |")
print("|                                        |")
print("|                                        |")
print("|                                        |")
print("|                                        |")
print("|                                        |")
print("|                                        |")
print("|                                        |")
print("------------------------------------------")
gn = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bmps = [0.5, 6, 24, 60, 200, 750, 1400, 5500, 18000, 40000, 125000]
mps = [0.5, 6, 24, 60, 200, 750, 1400, 5500, 18000, 40000, 125000]
tmps = 0.5
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
    "Guess the Number",
    "Roshambo",
    "Hangman",
    "Blackjack",
    "Snakes and Ladders",
    "Battleships",
]

upg = [
    "More Cash",
    "Marketing Increase",
    "Better Fruits",
    "Exquisite Soap",
    "16 Hour Shifts",
    "More Cooks",
    "Trading Hub",
    "Child Labour",
    "Red House Monopoly",
    "Thousand Dollar Bills",
    "Weighty Dice",
    "Radioactive Waste",
    "Increased Profits",
]
upgdesc = [
    "Produce a little more money.",
    "The better your marketing is, the more you'll make.",
    "Finer fruits sell for more profits.",
    "These cars are gonna be eaten off when you're done with them.",
    "There's no way this is legal.",
    "If there's one thing we all hate, it's waiting for fo.",
    "The hub of all trade - one might call it a trading hub.",
    "Who doesn't love a pinch of child labour?",
    "You already know that landing here is going to charge $2000 at best.",
    "Condensed bills will make your stacks worth more.",
    "It's almost as if these die always roll a six.",
    "The more radioactive it is, the more it sells for.",
    "Cash moneys.",
]
upgcost = [
    500,
    2000,
    8000,
    30000,
    160000,
    1300000,
    24000000,
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
sanity = 100
sanmult = 1
warp = 0


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
        " trevigintillion",
        " quattuorvigintillion",
        " quinvigintillion",
        " sexvigintillion",
        " septvigintillion",
        " octovigintillion",
        " novemvigintillion",
        " trigintillion",
        " untrigintillion",
        " duotrigintillion",
        " tretrigintillion",
        " quattuortrigintillion",
        " quintrigintillion",
        " sestrigintillion",
        " septentrigintillion",
        " octotrigintillion",
        " noventrigintillion",
        " quadragintillion",
    ]  # add quinquagintillions, sexagintillions, septuagintillions, octogintillions, nonagintillions, centillions, decicentillions, viginticentillions, trigintacentillions, quadragintacentillions, quinquagintacentillion, sexagintacentillion, septuagintacentillion, octogintacentillion, nonaginticentillion etc.
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

    print("\n\n\n")

    print("---------------------------------------------------------------------------")

    print("\n\n\n\n\n\n\n\n\n\n\n\n")

    print("---------------------------------------------------------------------------")

    print("\n\n\n\n")

    print("---------------------------------------------------------------------------")


def update():
    sys.stdout.write(f"\033[{3};{0}H")
    sys.stdout.flush()

    print("\033[2K", end="")
    t1 = "Main"
    t2 = "Upgrades"
    t3 = "Prestige"
    t4 = "Minigames"
    if select == -1:
        match selectcol:
            case 0:
                print(f"{t1 + " <":<20}{t2:<20}{t3:<20}{t4}")
            case 1:
                print(f"{t1:<20}{t2 + " <":<20}{t3:<20}{t4}")
            case 2:
                print(f"{t1:<20}{t2:<20}{t3 + " <":<20}{t4}")
            case 3:
                print(f"{t1:<20}{t2:<20}{t3:<20}{t4 + " <"}")
    else:
        print(f"{t1:<20}{t2:<20}{t3:<20}{t4}")

    sys.stdout.write(f"\033[{7};{0}H")
    sys.stdout.flush()

    dc = "Current Day: " + str(day)
    mn = "Money: $" + shorten(money)
    sn = "Sanity: " + str(math.ceil(sanity))
    mp = "($" + str(tmps) + "/s)"
    print("\033[2K", end="")
    print(f"{dc:<40}{mn}")
    if sanity > 0:
        print(f"{sn:<46}{mp}")
    else:
        print("\033[2K", end="")

    if page == 0:  # Main page
        sys.stdout.write(f"\033[{12};{0}H")
        sys.stdout.flush()

        left_lines = []
        right_lines = []

        for i in range(len(gn)):
            if select == i and i != -1 and selectcol == 0:
                left_lines.append(
                    f"{gnnames[i] + ": " + str(math.floor(gn[i])) + " <     "}"
                )
            else:
                left_lines.append(
                    f"{gnnames[i] + ": " + str(math.floor(gn[i]))}" + "      "
                )

        for i in range(len(left_lines)):
            print(f"{left_lines[i]:<38}{gnart[select][i]}")

        sys.stdout.write(f"\033[{26};{0}H")
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
                    + " per second - "
                    + str(round(((mps[select] * gn[select]) / tmps) * 100, 2))
                    + "%)"
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
                    "You aren't rich enough to buy this for $"
                    + shorten(cost[select] * (ramping ** gn[select]))
                    + "."
                )
                print("\033[2K", end="")
                print(
                    "You are missing $"
                    + shorten((cost[select] * (ramping ** gn[select])) - money)
                    + ". Lock in."
                )
            print("\033[2K")
            print("\033[2K")

    if page == 1:  # Upgrades page
        sys.stdout.write(f"\033[{12};{0}H")
        sys.stdout.flush()
        for i in range(11):
            print("\033[2K", end="")
            if i < len(upg):
                if selectcol == 0 and i == select:
                    print(upg[i] + " ($" + shorten(upgcost[i]) + ") <")
                else:
                    print(upg[i] + " ($" + shorten(upgcost[i]) + ")")

        sys.stdout.write(f"\033[{26};{0}H")
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
            # print(len(bought))
            # print(str(select) + " " + str(selectcol))

        print("\033[2K")
        print("\033[2K")

    if (
        page == 3
    ):  # Minigames (ZAC) hereeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        sys.stdout.write(f"\033[{12};{0}H")
        sys.stdout.flush()
        for i in range(len(minigames)):
            print("\033[2K", end="")
            if i == select:
                print(minigames[i] + " <")
            else:
                print(minigames[i])


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
                if (
                    page == 3 and select != -1
                ):  # ZAC PUT YO SHI HEREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEe
                    page = 4
                    clear()
                    match select:
                        case 1:
                            skills_gamblingtime.gambling(1)
                        case 3:
                            snakes_ladders.snekandeladr(5)
                        case 2:
                            ROSHAMBO.ROSHAMBO(2)
                        case 4:
                            blackjack.blackjack(4)
                        case 5:
                            hangman.hangthatman(3)
                        case 6:
                            yap("cameron is short")
                            # battleshipsadv.batlshit()
                if select == -1:
                    load()
                    match selectcol:
                        case 0:
                            page = 0
                        case 1:
                            page = 1
                        case 2:
                            page = 2
                        case 3:
                            page = 3
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
            if page == 3:
                select = max(-1, min(select, len(minigames) - 1))
        if select == -1:
            selectcol = max(0, min(selectcol, 3))
        else:
            selectcol = max(0, min(selectcol, 0))
    update()
    time.sleep(0.02)

    tmps = 0

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
        tmps += mps[i] * gn[i]

        money += mps[i] * gn[i] * 0.02
    sanity -= sanmult * 0.02 * (1 / 60)
