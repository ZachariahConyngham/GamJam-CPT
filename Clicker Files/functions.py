import sys, os, time, math, shutil, random
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


def yap(line, interval=0.05):  # yappin
    for letter in line:
        print(letter, end="", flush=True)
        time.sleep(interval)


def news(news):
    var.news.append([news , 0, time.time()])
    del var.news[0]


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

    dividerline = "\033[%sG┠───────────────────────────────────────────────────────────────────────────┨" % (str(shift))
    
    print(3 * "\n")
    print(dividerline)
    print(2 * "\n")
    print(dividerline)
    print(3 * "\n")
    print(dividerline)
    print(f"\033[{str(shift)}G" + 12 * "\n")
    print(dividerline)
    print(5 * "\n")
    print(dividerline)

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
    SMpS = var.bMpS[var.select] * var.gn[var.select] * (2 ** var.upgBought[var.select])

    sys.stdout.write(f"\033[{lineshift + 7};{0}H")
    sys.stdout.flush()

    
    titles = [f"{" Main  ":<20}", f"{"Upgrades  ":<20}", f"{"Research  ":<20}", f"{"Settings  ":<20}"]
    
    if var.select == -1:
        titles[var.selectcol] = f"{titles[var.selectcol][:titles[var.selectcol].find("  ")] + " <":<20}"
    print(f"{"":<{shift - 4}}║  ┃" + titles[0] + titles[1] + titles[2] + titles[3])

    sys.stdout.write(f"\033[{lineshift + 11};{1}H")
    sys.stdout.flush()

    if var.page != 2:
        tp = "\033[" + str(shift) + "G" + "┃ Time Played: " + shorten(var.time / 60 / 20) + " Days"
        mn = "Money: $" + shorten(var.money)
        sn = "\033[" + str(shift) + "G" + "┃ Sanity: " + str(math.ceil(var.sanity))
        mp = "($" + shorten(var.tMpS) + "/s)"
        clearline()
        print(f"{"":<{shift - 4}}{"║  ┃"}{tp:<47}{mn}")
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
        case 5:
            page5(selected, cost, SMpS)
    sys.stdout.write(f"\033[{lineshift + 2};{shift + 3}H")
    sys.stdout.flush()
    print("\x1B[3m" + var.flavortext[0][0] + "\x1B[0m")
    for i in range(1, min(4, len(var.news) + 1)):
        text = f"\033[{lineshift + 2 + i};{shift + 1}H╞   " + var.news[-i][0].ljust(70, ' ') + '╡'
        if var.news[-i][1] > 0.1 or var.news[-i][1] == -1:
            print(text)
        else:
            clearline()
            yap(text, 0.001)
    # printing anything here pretty much prints without issue, just don't print over the amount fo lines


    for i in range(5):
        sys.stdout.write(f"\033[{lineshift + i + 1};{0}H")
        sys.stdout.flush()
        print("\033[" + str(shift + 1) + "G╞", end="")
        print("\033[" + str(shift + 75) + "G╡")

def box():
    for i in range(len(titletext)):
        sys.stdout.write(f"\033[{lineshift + i - 6};{22 + shift}H")
        print(titletext[i])
    print("\033[" + str(shift + 24) + "GA game by Cameron, Zac and Kai")

    sys.stdout.write(f"\033[{0};{0}H")
    sys.stdout.flush()

    for i in range(shutil.get_terminal_size().lines - 1):
        print("\033[" + str(shift - 3) + "G║", end="")
        print("\033[" + str(shift + 79) + "G║")

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
        printtemp = var.gnArt[-1][i] if var.select == -1 else var.gnArt[var.select][var.upgBought[var.select]][i]
        print(f"{"":<{shift - 4}}║  ┃ {left_lines[i]:<36}{printtemp}")

    sys.stdout.write(f"\033[{lineshift + 30};{0}H")
    sys.stdout.flush()
    clearline()

    if not var.selected:
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
            print()
            clearline()
        else:
            print("\033[" + str(shift) + "G" + "┃ You aren't rich enough to buy this for $" + shorten(cost * (var.ramping ** var.gn[var.select])) + ".")
            clearline()
            print("\033[" + str(shift) + "G" + "┃ You are missing $" + shorten((cost * (var.ramping ** var.gn[var.select])) - var.money) + ".")
            if random.randint(1, 80) == 1:
                news("The %s rejected your poor status. You are emotionally hurt." % (var.gnNames[var.select]))
                var.sanity -= 10
            clearline()
            print()
            clearline()


def page1(selected, cost, SMpS):

    left_lines = []
    right_lines = []

    for i in range(11):
        print("\033[2K", end="")
        if var.gn[i] == 0:
            left_lines.append("LOCKED" + (" <" if var.selectcol == 1 and i == var.select else ""))
        elif i < len(var.upg):
            try:
                upg = var.upg[i][var.upgBought[i]]
                upgCost = shorten(var.upgCost[i][var.upgBought[i]])
            except:
                upg = "Maxed Upgrades"
                upgCost = "None"
            left_lines.append(f"{upg} (${upgCost})" + (" <" if var.selectcol == 1 and i == var.select else ""))
            
        right_lines.append(var.prName[i] + " " + to_roman(var.prestige[i]) + (" <" if var.selectcol == 2 and i == var.select else ""))

    for i in range(len(right_lines)):
        if len(left_lines) > i:
            print(f"{"":<{shift - 4}}{"║  ┃ "}{left_lines[i]:<74}{"┃"}")

    sys.stdout.write(f"\033[{lineshift + 30};{0}H")
    sys.stdout.flush()

    if var.select != -1:
        if var.selectcol == 1:
            clearline()
            if var.gn[var.select] == 0:
                desc = "What does this do?"
                cost = ""
            elif var.upgBought[var.select] == 5:
                desc = "Maxed Upgrades."
                cost = "None"
            else:
                desc = var.upgDesc[var.select][var.upgBought[var.select]]
                cost = shorten(var.upgCost[var.select][var.upgBought[var.select]])
            if not var.selected:
                print("\033[" + str(shift) + "G┃ " + desc)
                clearline()
                if cost != "":
                    print("\033[" + str(shift) + "G" + "┃ Doubles the production rate of " + var.gnNames[var.select] + ".")
            else:
                match cost:
                    case "None":
                        print(f"\033[{shift}G┃ There is nothing to buy.")
                        var.can = False
                    case "":
                        print(f"\033[{shift}G┃ " + desc)
                    case _:
                        print(f"\033[{shift}G┃ Buy for ${cost}?")
                        var.can = True
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
        clearline()
        print()
        clearline()
    else:
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
        if var.select == var.unix and var.selectcol == var.uniy:
            print("\033[" + str(shift) + "G" + "┃ You're already here.")
            clearline()
        else:
            clearline()
            print("\033[" + str(shift) + "G" + "┃ Travel costs $" + shorten(10000000 + 62761.39 ** ((var.select + var.selectcol + 2))))
            clearline()
            if abs(var.select - var.unix) <= 1 and abs(var.selectcol - var.uniy) <= 1:
                if var.money >= 10000000 + 62761.39 ** (var.select + var.selectcol + 2):
                    print("\033[" + str(shift) + "G" + "┃ You can travel here!")
                    news("Enjoy our replayability by typing 'N' when restarting the game.")
                    news("Sorry we haven't implemented these universes yet!")
                    news("You bought this universe!")
                else:
                    print("\033[" + str(shift) + "G" + "┃ You could travel here... if you were richer.")
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
        print(f"{"":<{shift - 4}}{"║  ┃ "}{"??? <"}")
    else:
        print(f"{"":<{shift - 4}}{"║  ┃ "}{"???  "}")
    
    
    

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

def page5(selected, cost, SMpS):
    print("EIOFAFHOIEAFH")

def buyupgrade():
    if var.money >= var.upgCost[var.select][var.upgBought[var.select]]:
        news("You buy the upgrade '" + var.upg[var.select][var.upgBought[var.select]] + "' for your " + str(var.gnNames[var.select]))
        var.money -= var.upgCost[var.select][var.upgBought[var.select]]
        var.upgBought[var.select] += 1

def buyprestige():
    if var.money >= (var.baseCost[var.select] + 15) * (28.3729579 ** ((var.prestige[var.select]) * 2)):
        var.money -= (var.baseCost[var.select] + 15) * (28.3729579 ** ((var.prestige[var.select]) * 2))
        var.prestige[var.select] += 1