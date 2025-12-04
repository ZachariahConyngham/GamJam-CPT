import sys, os, time, math
from pynput.mouse import Controller
import variables as var
from ascii_art import mapArt, titletext


def clear():  # Clears the terminal
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")


def clearline():
    print("\033[76G\x1b[1K\r", end="")
    print("┃                                                                           ┃\r", end="")


def yap(line):  # yappin
    for letter in line:
        print(letter, end="", flush=True)
        time.sleep(0.05)


def shorten(n):  # shortens numbers so that they are readable
    if n == 0:
        return "0"
    if var.longform == True:
        magnitude = int(math.log10(abs(n)) // 3)
        magnitude = max(0, min(magnitude, len(var.suffixes) - 1))
        short = n / (10 ** (3 * magnitude))
        if short.is_integer():
            short_str = str(int(short))
        else:
            short_str = f"{short:.2f}".rstrip("0").rstrip(".")
        return f"{short_str}{var.suffixes[magnitude]}"
    else: # e thing doesn't work yet
        magnitude = int(math.log10(abs(n)) // 1)
        short = n / (10 ** (3 * magnitude))
        if magnitude >= 6:
            return f"{str(n)[0] + "." + str(n)[1] + str(n)[2] + str(n)[3]}{"e"}{magnitude}"
        if magnitude < 6 and magnitude >= 3:
            num = []
            for i in range(len(str(n))):
                if i == len(str(n)) - 5:
                    num.append(",")
                num.append(str(n)[i])
            return "".join(num)
        else:
            return str(round(n, 2))


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

    print("\n")

    print("┠───────────────────────────────────────────────────────────────────────────┨")

    print("\n\n")

    print("┠───────────────────────────────────────────────────────────────────────────┨")

    print("\n\n\n")

    print("┠───────────────────────────────────────────────────────────────────────────┨")

    print("\n\n\n\n\n\n\n\n\n\n\n\n")

    print("┠───────────────────────────────────────────────────────────────────────────┨")

    print("\n\n\n\n\n")

    print("┠───────────────────────────────────────────────────────────────────────────┨")


def update():  # updates certain lines every frame

    selected = var.placeNames[var.select]  # the selected generator
    cost = var.generators[selected]["Money"]["cost"]
    SMpS = var.bMpS[var.select] * var.gn[var.select]

    sys.stdout.write(f"\033[{5};{1}H")
    sys.stdout.flush()

    clearline()
    t1 = "┃ Main"  # t = title
    t2 = "Upgrades"
    t3 = "Research"
    t4 = "Settings"
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

    sys.stdout.write(f"\033[{9};{1}H")
    sys.stdout.flush()

    if var.page != 2:
        dc = "┃ Current Day: " + str(var.day)
        mn = "Money: $" + shorten(var.money)
        sn = "┃ Sanity: " + str(math.ceil(var.sanity))
        mp = "($" + str(var.tMpS) + "/s)"
        clearline()
        print(f"{dc:<40}{mn}")
        if var.sanity > 0:
            print(f"{sn:<46}{mp}")
        else:
            clearline()

    box()

    sys.stdout.write(f"\033[{14};{1}H")
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

    for i in range(len(titletext)):
        sys.stdout.write(f"\033[{i + 1};{78}H")
        print(titletext[i])

def box():
    sys.stdout.write(f"\033[{0};{0}H")
    sys.stdout.flush()
    print("┏", end="")
    for i in range(75):
        print("━", end="")
    print("┓")
    for i in range(33):
        print("┃", end="")
        sys.stdout.write(f"\033[{i + 2};{77}H")
        print("┃")
    print("┗", end="")
    for i in range(75):
        print("━", end="")
    print("┛")

def page0(selected, cost, SMpS):
    left_lines = []

    for i in range(len(var.gn)):
        if var.select == i and i != -1 and var.selectcol == 0:
            left_lines.append(f"{"┃ " + var.gnNames[i] + ": " + str(math.floor(var.gn[i])) + " <     "}")
        else:
            left_lines.append(f"{"┃ " + var.gnNames[i] + ": " + str(math.floor(var.gn[i]))}" + "      ")
    for i in range(len(left_lines)):
        if var.select != -1:
            print(f"{left_lines[i]:<37}{var.gnArt[var.select][var.upgBought[var.select]][i]}")
        else:
            print(f"{left_lines[i]}")

    sys.stdout.write(f"\033[{28};{1}H")
    sys.stdout.flush()



    sys.stdout.write(f"\033[{28};{1}H")
    sys.stdout.flush()
    clearline()

    if var.selected == False:
        if var.select != -1:
            print("┃ " + var.gnDesc[var.select])
            clearline()
            print("┃ You currently own: " + str(math.floor(var.gn[var.select])) + " (Producing $" + shorten(SMpS) + " per second - " + str(round((SMpS / var.tMpS) * 100, 2)) + "%)")
            clearline()
            print("┃ (Next one costs $" + shorten(cost * (var.ramping ** var.gn[var.select])) + ")")
            clearline()
    else:
        if var.money >= cost * (var.ramping ** var.gn[var.select]):
            print("┃ Buy one for $" + shorten(cost * (var.ramping ** var.gn[var.select])) + "?")
            clearline()
            print("┃ (SPACE to confirm, X to cancel)")
            clearline()
        else:
            print("┃ You aren't rich enough to buy this for $" + shorten(cost * (var.ramping ** var.gn[var.select])) + ".")
            clearline()
            print("┃ You are missing $" + shorten((cost * (var.ramping ** var.gn[var.select])) - var.money) + ".")
            clearline()


def page1(selected, cost, SMpS):

    left_lines = []
    right_lines = []

    for i in range(11):
        print("\033[2K", end="")
        if i < len(var.upg):
            if var.selectcol == 1 and i == var.select:
                left_lines.append("┃ " + var.upg[i][var.upgBought[i]] + " ($" + shorten(var.upgCost[i][var.upgBought[i]]) + ") <")
            else:
                left_lines.append("┃ " + var.upg[i][var.upgBought[i]] + " ($" + shorten(var.upgCost[i][var.upgBought[i]]) + ")")

        if var.selectcol == 2 and i == var.select:
            right_lines.append(var.prName[i] + " " + to_roman(var.prestige[i]) + " <")
        else:
            right_lines.append(var.prName[i] + " " + to_roman(var.prestige[i]))

    for i in range(len(right_lines)):
        if len(left_lines) > i:
            print(f"{left_lines[i]:<40}{right_lines[i]:<36}{"┃"}")
        else:
            print(f"{"":<40}{right_lines[i]}")

    sys.stdout.write(f"\033[{28};{1}H")
    sys.stdout.flush()

    if var.select != -1:
        if var.selectcol == 1:
            clearline()
            if var.selected == False:
                print("┃ " + var.upgDesc[var.select][var.upgBought[var.select]])
                clearline()
                print("┃ Doubles the production rate of " + var.gnNames[var.select] + ".")
            else:
                print("┃ Buy for $" + shorten(var.upgCost[var.select][var.upgBought[var.select]]) + "?")
        if var.selectcol == 2:
            clearline()
            if var.selected == False:
                print("┃ Each prestige level increases " + var.gnNames[var.select] + "'s production and reduces the")
                clearline()
                print("┃ cost by 20%.")
                clearline()
                print("┃ Current bonus: " + str(20 * var.prestige[var.select]) + "%")
            else:
                print("┃ Buy for $" + shorten((var.baseCost[var.select] + 15) * (28.3729579 ** ((var.prestige[var.select]) * 2))) + "?")


def page2(selected, cost, SMpS): # I WILL MERGE MINIGAMES ONTO THIS TAB
    sys.stdout.write(f"\033[{9};{1}H")
    sys.stdout.flush()

    print(f"{"┃ Research":<40}{"Worldview"}")

    sys.stdout.write(f"\033[{14};{1}H")
    sys.stdout.flush()

    for i in range(len(var.map)):
        print("┃     ", end="")
        for i1 in range(len(var.map[i])):
            if var.select == i and var.selectcol == i1:
                print("  (" + var.mapKeys[var.map[i][i1]], end=") <")
            else:
                print("  (" + var.mapKeys[var.map[i][i1]], end=")  ")
        print("       ┃")

    sys.stdout.write(f"\033[{28};{1}H")
    sys.stdout.flush()

    clearline()
    if var.select != -1:
        print("┃ " + var.mapDesc[var.map[var.select][var.selectcol]])
        clearline()
        print("┃ Travel costs $" + shorten(1000000000000000 + 82761.39 ** ((var.select + var.selectcol + 2) * 1.5)))
        clearline()
        if abs(var.select - var.unix) <= 1 and abs(var.selectcol - var.uniy) <= 1:
            print("┃ You can travel here!")
        else:
            print("┃ You can't travel here. You are not close enough.")


def page3(selected, cost, SMpS):
    print("YESYSEY")

    sys.stdout.write(f"\033[{28};{1}H")  # description box
    sys.stdout.flush()


def buyupgrade():
    if var.money >= var.upgCost[var.select][var.upgBought[var.select]]:
        var.money -= var.upgCost[var.select][var.upgBought[var.select]]
        var.upgBought[var.select] += 1

def buyprestige():
    if var.money >= (var.baseCost[var.select] + 15) * (28.3729579 ** ((var.prestige[var.select]) * 2)):
        var.money -= (var.baseCost[var.select] + 15) * (28.3729579 ** ((var.prestige[var.select]) * 2))
        var.prestige[var.select] += 1