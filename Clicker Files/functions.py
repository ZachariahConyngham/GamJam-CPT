import sys, os, time, math, shutil
import variables as var
from variables import shift, lineshift
from ascii_art import mapArt, titletext

def clear():  # Clears the terminal
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")


def clearline():
    print("\033[" + str(shift - 3) + "G║  ┃", end="")
    print(" " * 75 + "\r", end="")


def yap(line):  # yappin
    for letter in line:
        print(letter, end="", flush=True)
        time.sleep(0.05)


def shorten(n):  # shortens numbers so that they are readable
    if n == 0:
        return "0"
    mag = int(math.log10(abs(n)) // 3)
    mag = max(0, min(mag, len(var.suffixes) - 1))
    short = n / (10 ** (3 * mag))
    if short.is_integer():
        short_str = str(int(short))
    else:
        short_str = f"{short:.2f}".rstrip("0").rstrip(".")
    if var.settings[0] == True or mag < 2:
        return f"{short_str}{var.suffixes[mag]}"
    else:
        mag *= 3
        return f"{short_str}e{mag}"


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

    sys.stdout.write(f"\033[{lineshift + 1};{0}H")
    sys.stdout.flush()

    print("\n\n\n")

    print("\033[" + str(shift) + "G" + "┠───────────────────────────────────────────────────────────────────────────┨")

    print("\n\n")

    print("\033[" + str(shift) + "G" + "┠───────────────────────────────────────────────────────────────────────────┨")

    print("\n\n\n")

    print("\033[" + str(shift) + "G" + "┠───────────────────────────────────────────────────────────────────────────┨")

    print("\033[" + str(shift) + "G" + "\n\n\n\n\n\n\n\n\n\n\n\n")

    print("\033[" + str(shift) + "G" + "┠───────────────────────────────────────────────────────────────────────────┨")

    print("\n\n\n\n\n")

    print("\033[" + str(shift) + "G" + "┠───────────────────────────────────────────────────────────────────────────┨")


def update():  # updates certain lines every frame

    selected = var.placeNames[var.select]  # the selected generator
    cost = var.generators[selected]["Money"]["cost"]
    SMpS = var.bMpS[var.select] * var.gn[var.select]

    sys.stdout.write(f"\033[{lineshift + 7};{0}H")
    sys.stdout.flush()

    clearline()
    t1 = " Main"  # t = title
    t2 = "Upgrades"
    t3 = "Research"
    t4 = "Settings"
    if var.select == -1:
        match var.selectcol:
            case 0:
                print(f"{"":<{shift - 4}}{"║  ┃"}{t1 + " <":<20}{t2:<20}{t3:<20}{t4}")
            case 1:
                print(f"{"":<{shift - 4}}{"║  ┃"}{t1:<20}{t2 + " <":<20}{t3:<20}{t4}")
            case 2:
                print(f"{"":<{shift - 4}}{"║  ┃"}{t1:<20}{t2:<20}{t3 + " <":<20}{t4}")
            case 3:
                print(f"{"":<{shift - 4}}{"║  ┃"}{t1:<20}{t2:<20}{t3:<20}{t4 + " <"}")
    else:
        print(f"{"":<{shift - 4}}{"║  ┃"}{t1:<20}{t2:<20}{t3:<20}{t4}")

    sys.stdout.write(f"\033[{lineshift + 11};{1}H")
    sys.stdout.flush()

    if var.page != 2:
        dc = "\033[" + str(shift) + "G" + "┃ Current Day: " + str(var.day)
        mn = "Money: $" + shorten(var.money)
        sn = "\033[" + str(shift) + "G" + "┃ Sanity: " + str(math.ceil(var.sanity))
        mp = "($" + shorten(var.tMpS) + "/s)"
        clearline()
        print(f"{"":<{shift - 4}}{"║  ┃"}{dc:<47}{mn}")
        clearline()
        print(f"{"":<{shift - 4}}{"║  ┃"}{sn:<53}{mp}")
    box()

    sys.stdout.write(f"\033[{lineshift + 16};{1}H")
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
        case 4:
            page4(selected, cost, SMpS)

    for i in range(len(titletext)):
        sys.stdout.write(f"\033[{lineshift + i - 6};{24 + shift}H")
        print(titletext[i])
    print("\033[" + str(shift + 24) + "GA game by Cameron, Zac and Kai")

    sys.stdout.write(f"\033[{0};{0}H")
    sys.stdout.flush()

    for i in range(shutil.get_terminal_size()[1] - 1):
        print("\033[" + str(shift - 3) + "G║", end="")
        print("\033[" + str(shift + 79) + "G║")
    
    sys.stdout.write(f"\033[{lineshift + 2};{shift + 3}H")
    sys.stdout.flush()

    print("\x1B[3m" + var.flavortext[0][0] + "\x1B[0m")

    for i in range(4):
        sys.stdout.write(f"\033[{lineshift + i + 1};{0}H")
        sys.stdout.flush()

        print("\033[" + str(shift + 1) + "G╞", end="")
        print("\033[" + str(shift + 75) + "G╡")

def box():
    sys.stdout.write(f"\033[{lineshift};{0}H")
    sys.stdout.flush()

    print("\033[" + str(shift) + "G" + "┏", end="")
    for i in range(75):
        print("━", end="")
    print("┓")
    for i in range(34):
        print("\033[" + str(shift) + "G" + "┃", end="")
        sys.stdout.write(f"\033[{lineshift + i + 1};{76 + shift}H")
        print("┃")
    print("\033[" + str(shift) + "G" + "┗", end="")
    for i in range(75):
        print("━", end="")
    print("┛")

def page0(selected, cost, SMpS):
    left_lines = []

    for i in range(len(var.gn)):
        if var.select == i and i != -1 and var.selectcol == 0:
            left_lines.append(f"{var.gnNames[i] + ": " + str(math.floor(var.gn[i]))}" + " <     ")
        else:
            left_lines.append(f"{var.gnNames[i] + ": " + str(math.floor(var.gn[i]))}" + "      ")
    for i in range(len(left_lines)):
        if var.select != -1:
            print(f"{"":<{shift - 4}}{"║  ┃ "}{left_lines[i]:<37}{var.gnArt[var.select][var.upgBought[var.select]][i]}")
        else:
            print(f"{"":<{shift - 4}}{"║  ┃ "}{left_lines[i]:<37}{var.gnArt[-1][i]}")

    sys.stdout.write(f"\033[{lineshift + 30};{0}H")
    sys.stdout.flush()
    clearline()

    if var.selected == False:
        if var.select != -1:
            print("\033[" + str(shift) + "G" + "┃ " + var.gnDesc[var.select])
            clearline()
            print("\033[" + str(shift) + "G" + "┃ You currently own: " + str(math.floor(var.gn[var.select])) + " (Producing $" + shorten(SMpS) + " per second - " + str(round((SMpS / var.tMpS) * 100, 2)) + "%)")
            clearline()
            print("\033[" + str(shift) + "G" + "┃ (Next one costs $" + shorten(cost * (var.ramping ** var.gn[var.select])) + ")")
            clearline()
        else:
            clearline()
            print()
            clearline()
            print()
            clearline()
    else:
        if var.money >= cost * (var.ramping ** var.gn[var.select]):
            print("\033[" + str(shift) + "G" + "┃ Buy one for $" + shorten(cost * (var.ramping ** var.gn[var.select])) + "?")
            clearline()
            print("\033[" + str(shift) + "G" + "┃ (SPACE to confirm, X to cancel)")
            clearline()
        else:
            print("\033[" + str(shift) + "G" + "┃ You aren't rich enough to buy this for $" + shorten(cost * (var.ramping ** var.gn[var.select])) + ".")
            clearline()
            print("\033[" + str(shift) + "G" + "┃ You are missing $" + shorten((cost * (var.ramping ** var.gn[var.select])) - var.money) + ".")
            clearline()


def page1(selected, cost, SMpS):

    left_lines = []
    right_lines = []

    for i in range(11):
        print("\033[2K", end="")
        if i < len(var.upg):
            if var.selectcol == 1 and i == var.select:
                left_lines.append(var.upg[i][var.upgBought[i]] + " ($" + shorten(var.upgCost[i][var.upgBought[i]]) + ") <")
            else:
                left_lines.append(var.upg[i][var.upgBought[i]] + " ($" + shorten(var.upgCost[i][var.upgBought[i]]) + ")")

        if var.selectcol == 2 and i == var.select:
            right_lines.append(var.prName[i] + " " + to_roman(var.prestige[i]) + " <")
        else:
            right_lines.append(var.prName[i] + " " + to_roman(var.prestige[i]))

    for i in range(len(right_lines)):
        if len(left_lines) > i:
            print(f"{"":<{shift - 4}}{"║  ┃ "}{left_lines[i]:<74}{"┃"}")

    sys.stdout.write(f"\033[{lineshift + 30};{0}H")
    sys.stdout.flush()

    if var.select != -1:
        if var.selectcol == 1:
            clearline()
            if var.selected == False:
                print("\033[" + str(shift) + "G" + "┃ " + var.upgDesc[var.select][var.upgBought[var.select]])
                clearline()
                print("\033[" + str(shift) + "G" + "┃ Doubles the production rate of " + var.gnNames[var.select] + ".")
            else:
                print("\033[" + str(shift) + "G" + "┃ Buy for $" + shorten(var.upgCost[var.select][var.upgBought[var.select]]) + "?")
        if var.selectcol == 2:
            clearline()
            if var.selected == False:
                print("\033[" + str(shift) + "G" + "┃ Each prestige level increases " + var.gnNames[var.select] + "'s production and reduces the")
                clearline()
                print("\033[" + str(shift) + "G" + "┃ cost by 20%.")
                clearline()
                print("\033[" + str(shift) + "G" + "┃ Current bonus: " + str(20 * var.prestige[var.select]) + "%")
            else:
                print("\033[" + str(shift) + "G" + "┃ Buy for $" + shorten((var.baseCost[var.select] + 15) * (28.3729579 ** ((var.prestige[var.select]) * 2))) + "?")
    else:
        clearline()
        print()
        clearline()
        print()
        clearline()


def page2(selected, cost, SMpS): # I WILL MERGE MINIGAMES ONTO THIS TAB
    sys.stdout.write(f"\033[{lineshift + 11};{0}H")
    sys.stdout.flush()

    print(f"{"":<{shift - 1}}{"┃ Research":<40}{"Worldview"}")

    sys.stdout.write(f"\033[{lineshift + 16};{1}H")
    sys.stdout.flush()

    for i in range(len(var.map)):
        print("\033[" + str(shift) + "G" + "┃     ", end="")
        for i1 in range(len(var.map[i])):
            if var.select == i and var.selectcol == i1:
                print("  (" + var.mapKeys[var.map[i][i1]], end=") <")
            else:
                print("  (" + var.mapKeys[var.map[i][i1]], end=")  ")
        print("       ┃")

    sys.stdout.write(f"\033[{lineshift + 30};{0}H")
    sys.stdout.flush()

    clearline()
    if var.select != -1:
        print("\033[" + str(shift) + "G" + "┃ " + var.mapDesc[var.map[var.select][var.selectcol]])
        clearline()
        print("\033[" + str(shift) + "G" + "┃ Travel costs $" + shorten(10000000 + 62761.39 ** ((var.select + var.selectcol + 2))))
        clearline()
        if abs(var.select - var.unix) <= 1 and abs(var.selectcol - var.uniy) <= 1:
            print("\033[" + str(shift) + "G" + "┃ You can travel here!")
        else:
            print("\033[" + str(shift) + "G" + "┃ You can't travel here. You are not close enough.")
    else:
        clearline()
        print()
        clearline()
        print()
        clearline()


def page3(selected, cost, SMpS):
    
    for i in range(len(var.settings)):
        form = ""
        if i == 0:
            match var.settings[0]:
                case True:
                    form = "Extended"
                case False:
                    form = "Shortened"
        if var.select == i:
            print(f"{"":<{shift - 4}}{"║  ┃ "}{var.settingstxt[i] + form + " < "}")
        else:
            print(f"{"":<{shift - 4}}{"║  ┃ "}{var.settingstxt[i] + form + "   "}")

    print("")
    
    if var.select == len(var.settings):
        print(f"{"":<{shift - 4}}{"║  ┃ "}{"Get Save Code <"}")
    else:
        print(f"{"":<{shift - 4}}{"║  ┃ "}{"Get Save Code  "}")

    if var.select == len(var.settings) + 1:
        print(f"{"":<{shift - 4}}{"║  ┃ "}{"Enter Save Code <"}")
    else:
        print(f"{"":<{shift - 4}}{"║  ┃ "}{"Enter Save Code  "}")

    sys.stdout.write(f"\033[{lineshift + 30};{0}H")  # description box
    sys.stdout.flush()

def page4(selected, cost, SMpS):
    print("\033[23;" + str(shift + 2) + "H", end="")
    for gn in var.gn:
        print(gn, end="")
    print("-", end="")
    for upg in var.upgBought:
        print(upg, end="")
    print("-" + shorten(var.money) + "-" + shorten(var.sanity))

    print("\n\033[" + str(shift + 2) + "G(You can copy this code to re-enter your save file at a later date.)")

def buyupgrade():
    if var.money >= var.upgCost[var.select][var.upgBought[var.select]]:
        var.money -= var.upgCost[var.select][var.upgBought[var.select]]
        var.upgBought[var.select] += 1

def buyprestige():
    if var.money >= (var.baseCost[var.select] + 15) * (28.3729579 ** ((var.prestige[var.select]) * 2)):
        var.money -= (var.baseCost[var.select] + 15) * (28.3729579 ** ((var.prestige[var.select]) * 2))
        var.prestige[var.select] += 1