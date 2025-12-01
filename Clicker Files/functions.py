import sys, os, time, math
import variables as var
from ascii_art import mapArt


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
    if n == 0:
        return "0"
    magnitude = int(math.log10(abs(n)) // 3)
    magnitude = max(0, min(magnitude, len(var.suffixes) - 1))
    short = n / (10 ** (3 * magnitude))

    if short.is_integer():
        short_str = str(int(short))
    else:
        short_str = f"{short:.2f}".rstrip("0").rstrip(".")

    return f"{short_str}{var.suffixes[magnitude]}"


def to_roman(num):  # roman numeral converter (literally just for prestiges)
    roman_map = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }
    roman_numeral = ""
    for value, symbol in sorted(roman_map.items(), reverse=True):
        while num >= value:
            roman_numeral += symbol
            num -= value
    return roman_numeral


def load():  # loads the base page
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


def update():  # updates certain lines every frame

    selected = var.placeNames[var.select]  # the selected generator
    cost = var.generators[selected]["Money"]["cost"]
    SMpS = var.bMpS[var.select] * var.gn[var.select]

    sys.stdout.write(f"\033[{3};{0}H")
    sys.stdout.flush()

    print("\033[2K", end="")
    t1 = "Main"  # t = title
    t2 = "Upgrades"
    t3 = "Minigames"
    t4 = "Research"
    if var.select == -1:
        match var.selectcol:
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

    if var.page != 3:
        dc = "Current Day: " + str(var.day)
        mn = "Money: $" + shorten(var.money)
        sn = "Sanity: " + str(math.ceil(var.sanity))
        mp = "($" + str(var.tMpS) + "/s)"
        print("\033[2K", end="")
        print(f"{dc:<40}{mn}")
        if var.sanity > 0:
            print(f"{sn:<46}{mp}")
        else:
            print("\033[2K", end="")

    sys.stdout.write(f"\033[{12};{0}H")
    sys.stdout.flush()

    match var.page:
        case 0:
            page0(selected, cost, SMpS)
        case 1:
            page1(selected, cost, SMpS)
        case 2:
            page2(selected, cost, SMpS)
        case 3:
            page3(selected, cost, SMpS)

    for i in range(40):
        sys.stdout.write(f"\033[{12};{81}H")
        sys.stdout.flush()
        print("|")


def page0(selected, cost, SMpS):
    left_lines = []

    for i in range(len(var.gn)):
        if var.select == i and i != -1 and var.selectcol == 0:
            left_lines.append(
                f"{var.gnNames[i] + ": " + str(math.floor(var.gn[i])) + " <     "}"
            )
        else:
            left_lines.append(
                f"{var.gnNames[i] + ": " + str(math.floor(var.gn[i]))}" + "      "
            )
    for i in range(len(left_lines)):
        if var.select != -1:
            print(f"{left_lines[i]:<38}{var.gnArt[var.select][0][i]}")
        else:
            print("\033[2K", end="")
            print(left_lines[i])

    sys.stdout.write(f"\033[{26};{0}H")
    sys.stdout.flush()
    print("\033[2K", end="")
    if var.selected == False:
        if var.select != -1:
            print(var.gnDesc[var.select])
            print("\033[2K", end="")
            print(
                "You currently own: "
                + str(math.floor(var.gn[var.select]))
                + " (Producing $"
                + shorten(SMpS)
                + " per second - "
                + str(round((SMpS / var.tMpS) * 100, 2))
                + "%)"
            )
            print("\033[2K", end="")
            print(
                "(Next one costs $"
                + shorten(cost * (var.ramping ** var.gn[var.select]))
                + ")"
            )
        else:
            print("\033[2K")
            print("\033[2K")
            print("\033[2K")
    else:
        if var.money >= cost * (var.ramping ** var.gn[var.select]):
            print(
                "Buy one for $"
                + shorten(cost * (var.ramping ** var.gn[var.select]))
                + "? (SPACE to confirm, X to cancel)"
            )
        else:
            print(
                "You aren't rich enough to buy this for $"
                + shorten(cost * (var.ramping ** var.gn[var.select]))
                + "."
            )
            print("\033[2K", end="")
            print(
                "You are missing $"
                + shorten((cost * (var.ramping ** var.gn[var.select])) - var.money)
                + ". Lock in."
            )
        print("\033[2K")
        print("\033[2K")


def page1(selected, cost, SMpS):

    left_lines = []
    right_lines = []

    for i in range(11):
        print("\033[2K", end="")
        if i < len(var.upg):
            if var.selectcol == 1 and i == var.select:
                left_lines.append(
                    var.upg[i][var.upgBought[i]]
                    + " ($"
                    + shorten(var.upgCost[i][var.upgBought[i]])
                    + ") <"
                )
            else:
                left_lines.append(
                    var.upg[i][var.upgBought[i]]
                    + " ($"
                    + shorten(var.upgCost[i][var.upgBought[i]])
                    + ")"
                )

        if var.selectcol == 2 and i == var.select:
            right_lines.append(var.prName[i] + " " + to_roman(var.prestige[i]) + " <")
        else:
            right_lines.append(var.prName[i] + " " + to_roman(var.prestige[i]))

    for i in range(len(right_lines)):
        print("\033[2K", end="")
        if len(left_lines) > i:
            print(f"{left_lines[i]:<40}{right_lines[i]}")
        else:
            print(f"{"":<40}{right_lines[i]}")

    sys.stdout.write(f"\033[{26};{0}H")
    sys.stdout.flush()
    print("\033[2K", end="")

    if var.select != -1:
        print(var.upgDesc[var.select][var.upgBought[var.select]])
        print("\033[2K", end="")
        # print(len(bought))
        # print(str(select) + " " + str(selectcol))
    print("\033[2K")
    print("\033[2K")


def page2(selected, cost, SMpS):
    print("YESYSEY")

    sys.stdout.write(f"\033[{26};{0}H")  # description box
    sys.stdout.flush()


def page3(selected, cost, SMpS):
    sys.stdout.write(f"\033[{7};{0}H")
    sys.stdout.flush()

    print(f"{"Research":<40}{"Worldview"}")

    sys.stdout.write(f"\033[{12};{0}H")
    sys.stdout.flush()

    for i in range(len(var.map)):
        print("\033[2K", end="")
        print("|    ", end="")
        for i1 in range(len(var.map[i])):
            if var.select == i and var.selectcol == i1:
                print("  (" + var.mapKeys[var.map[i][i1]], end=") <")
            else:
                print("  (" + var.mapKeys[var.map[i][i1]], end=")  ")
        print("      |")

    sys.stdout.write(f"\033[{26};{0}H")
    sys.stdout.flush()

    print("\033[2K", end="")
    if var.select != -1:
        print(var.mapDesc[var.map[var.select][var.selectcol]])
        print("\033[2K", end="")
        print(
            "Travel costs $"
            + shorten(
                1000000000000000 + 82761.39 ** ((var.select + var.selectcol + 2) * 1.5)
            )
        )
        print("\033[2K", end="")
        if abs(var.select - var.unix) <= 1 and abs(var.selectcol - var.uniy) <= 1:
            print("You can travel here!")
        else:
            print("You can't travel here. You are not close enough.")
    print("\033[2K")
    print("\033[2K")


def buyupgrade():
    if var.money >= var.upgCost[var.select][var.upgBought[var.select]]:
        var.money -= var.upgCost[var.select][var.upgBought[var.select]]
        var.upgBought[var.select] += 1
