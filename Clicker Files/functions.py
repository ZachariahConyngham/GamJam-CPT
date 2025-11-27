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


selected = 0
cost = 0
SMpS = 0  # selected money per second


def update():  # updates certain lines every frame

    selected = var.placeNames[var.select]  # the selected generator
    cost = var.generators[selected]["Money"]["cost"]
    SMpS = var.MpS[var.select] * var.gn[var.select]

    sys.stdout.write(f"\033[{3};{0}H")
    sys.stdout.flush()

    print("\033[2K", end="")
    t1 = "Main"  # t = title
    t2 = "Upgrades"
    t3 = "Minigames"
    t4 = "Worldview"
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
            page0()
        case 1:
            page1()
        case 2:
            page2()
        case 3:
            page3()


def page0():
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
        if var.money >= var.generators[selected]["Money"]["cost"] * (
            var.ramping ** var.gn[var.select]
        ):
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


def page1():

    left_lines = []
    right_lines = []

    for i in range(11):
        print("\033[2K", end="")
        if i < len(var.upg):
            if var.selectcol == 1 and i == var.select:
                left_lines.append(
                    var.upg[i][0] + " ($" + shorten(var.upgCost[i][0]) + ") <"
                )
            else:
                left_lines.append(
                    var.upg[i][0] + " ($" + shorten(var.upgCost[i][0]) + ")"
                )
        if var.selectcol == 2 and i == var.select:
            right_lines.append(
                var.prName[i]
                + " "
                + to_roman(var.generators[selected]["Prestige"]["lvl"])
                + " <"
            )
        else:
            right_lines.append(
                var.prName[i]
                + " "
                + to_roman(var.generators[selected]["Prestige"]["lvl"])
            )

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
        print(var.upgDesc[var.select][0])
        print("\033[2K", end="")
        up = var.upgMult[var.select].split("-")
        if up[0] != "a" and up[0] is not None:
            print(var.gnNames[int(up[0])] + " - x" + up[1] + " production")
        else:
            print("All generators - x" + up[1] + " production")
        # print(len(bought))
        # print(str(select) + " " + str(selectcol))

    print("\033[2K")
    print("\033[2K")


def page2():
    print("YESYSEY")


def page3():
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
    print(var.mapDesc[var.map[i][i1]])
