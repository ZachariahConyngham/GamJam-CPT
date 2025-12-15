import sys, time, os, math, msvcrt, shutil, json
import functions as func
import variables as var
from Minigames import hangman, blackjack, ROSHAMBO, snakes_ladders, skills_gamblingtime, battleshipsadv

disable = False
func.clear()
func.box()

time.sleep(1)

def savedata():
    player_data = {
        "money": var.money,
        "gn": var.gn,
        "upg": var.upgBought,
        "sanity": var.sanity,
        "time": var.time
    }
    with open("savefile.json", "w") as f:
        json.dump(player_data, f, indent=4)

def load_data(filename="savefile.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return None

print("\033[" + str(var.lineshift + 2) + ";" + str(var.shift + 2) + "H", end="")
save = ""
while save == "":
    save = input("Do you want to load your save? (Y/N) ").upper()
    match save:
        case "Y":
            data = load_data()
            if data != "{}":
                var.money = data["money"]
                var.gn = data["gn"]
                var.upgBought = data["upg"]
                var.sanity = data["sanity"]
                var.time = data["time"]
        case "N":
            with open("savefile.json", "w") as f:
                f.write("{}")
        case "JIM":
            var.money = 1234567890123456789012345678901234567890
            var.gn = [1] + 10 * [0]
            var.upgBought = 11 * [0]
            var.sanity = 100
            var.time = 0
        case _:
            print("Sorry, Y and N only.")
            save = ""

print("\033[" + str(var.lineshift + 2) + ";" + str(var.shift + 2) + "H", end="")

if (input("Do you want to read the opening dialogue? (Y/N) ")).upper() == "Y":
    func.clear()
    func.box()
    print("\033[" + str(var.lineshift + 2) + ";" + str(var.shift + 2) + "H", end="")
    for line in var.dialogue[0]:
        if line == "clear":
            func.clear()
            func.box()
            print("\033[" + str(var.lineshift + 2) + ";" + str(var.shift + 2) + "H", end="")
        else:
            func.yap("\033[" + str(var.shift + 2) + "G\033[?25h" + line)
            print("\033[?25l\n")
            time.sleep(0.5)

print("\033[?25l", end="")  # Hides the player cursor
func.clear()
func.box()
func.load()



while True:
    if msvcrt.kbhit():  # Key check
        key = msvcrt.getch().decode()
        match key:
            case "w":
                var.select -= 1
                var.selected = False
            case "s":
                var.select += 1
                var.selected = False
            case "a":
                var.selectcol -= 1
                var.selected = False
            case "d":
                var.selectcol += 1
                var.selected = False
            case " ":
                if var.page == 0 and var.selectcol == 0 and var.select != -1:
                    if var.money >= var.generators[var.placeNames[var.select]]["Money"]["cost"] and (var.ramping ** var.gn[var.select]) and var.selected:
                        var.money -= round(var.generators[var.placeNames[var.select]]["Money"]["cost"] * (var.ramping ** var.gn[var.select]), 2)
                        var.gn[var.select] += 1
                        if var.gn[var.select] in var.gnMilestones and [var.gn[var.select], var.gnNames[var.select]] not in var.milestonesUnlocked:
                            match var.gn[var.select]:
                                case 1:
                                    func.news("You have bought your FIRST %s, congratulations!" % (var.gnNames[var.select]))
                                    var.money += var.baseCost[var.select] / 2
                                case 420:
                                    func.news("The meaning of life. Have a bonus!")
                                    var.money += var.baseCost[var.select] * 420 * 100
                                case 314:
                                    func.news("It's Pi!")
                                    var.money += var.baseCost[var.select] * 31415 * 3.1415
                                case 1000000:
                                    func.news("Your dedication astounds us. Have a huge bonus!")
                                    var.money += var.baseCost[var.select] * var.gn[var.select] * 31415926
                                case milestone:
                                    func.news("You have bought %s %s!" % (var.gn[var.select], var.gnNamesPlural[var.select]))
                                    var.money += var.baseCost[var.select] * milestone / 5
                            milestonesUnlocked += [var.gn[var.select], var.gnNames[var.select]]
                if var.page == 1 and var.select != -1 and var.selected and var.can:
                    if var.selectcol == 1:
                        func.buyupgrade()
                    if var.selectcol == 2:
                        func.buyprestige()
                if var.page == 3 and var.select != -1 and not var.select >= len(var.settings):
                    var.settings[var.select] = not var.settings[var.select]
                if var.page == 3 and var.select == len(var.settings):
                    var.page == 5
                    func.clear()
                    func.load()
                    func.box()
                    battleshipsadv.batlshit(var.shift)
                    func.clear()

                if var.page == 8 and var.select != -1:  # ZAC PUT YO SHI HEREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEe
                    var.page = 5
                    func.clear()
                    match var.select:
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
                            func.yap("cameron is short")
                            # battleshipsadv.batlshit()
                if var.select == -1:
                    var.selected = False
                    func.load()
                    match var.selectcol:
                        case 0:
                            var.page = 0
                        case 1:
                            var.page = 1
                        case 2:
                            var.page = 2
                        case 3:
                            var.page = 3
                else:
                    var.selected = not var.selected
            case "x":
                if var.selected == True:
                    var.selected = False
            case "r":
                var.shift = round((shutil.get_terminal_size().columns / 2) - 40)
                func.load()
        match var.page:
            case 0:
                var.select = max(-1, min(var.select, len(var.gn) - 1))
            case 1:
                if len(var.upg) < 11:
                    var.select = max(-1, min(var.select, len(var.upg) - 1))
                else:
                    var.select = max(-1, min(var.select, 10))
            case 2:
                var.select = max(-1, min(var.select, 10))
            case 3:
                var.select = max(-1, min(var.select, len(var.settings)))
            case 4:
                var.select = -1

        if var.select == -1:
            var.selectcol = max(0, min(var.selectcol, 3))
        elif var.page == 1:
            var.selectcol = max(1, min(var.selectcol, 1))
        elif var.page == 2 and var.select > -1:
            var.selectcol = max(0, min(var.selectcol, 8))
        else:
            var.selectcol = 0
    
    if shutil.get_terminal_size().lines <= 42:
        print("\033[H", end="")
        for i in range(shutil.get_terminal_size().lines):
            if i != 19:
                print("x1b[" + str(i + 1) + ";80H\033[2K")
        print("\x1b[20;80HScreen not big enough.")
    if disable == False:
        func.update()
    else:
        func.box()


    if 0 < var.sanity <= 50:
        func.news("You decide to play Battleships to anchor your sanity.")
        func.news("You are overwhelmed by the insanity of the world.")
        battleshipsadv.batlshit(var.shift)
        disable = True
    else:
        jim = "Bald"

    if var.sanity <= 0:
        snakes_ladders.snekandeladr()
        disable = True
    else:
        jim = "Short"
    #if  =  :
    #    e
    #else:
    #    e

    time.sleep(0.02)
    var.time += 0.02

    for index, news in enumerate(var.news):
        if news[1] >= 7:
            var.news[index] = [70 * " " + "╡", -1]
        else:
            if news[1] != -1:
                news[1] = time.time() - news[2]

    savedata()

    shift = round((shutil.get_terminal_size().columns / 2) - 40)

    var.tMpS = 0
    
    if var.page != 4:
        for i in range(len(var.gn)):  # calculating money increase and sanity loss
            mult = 1
            var.tMpS += var.MpS[i] * var.gn[i] * (2 ** (var.upgBought[i])) * (1.2 ** (var.prestige[i] - 1))

            var.money += var.MpS[i] * var.gn[i] * (2 ** (var.upgBought[i])) * (1.2 ** (var.prestige[i] - 1)) * 0.02

            var.cost[i] = var.baseCost[i] * (0.8 ** (var.prestige[i] - 1))
        var.sanity -= var.sanmult * 0.02 * (1 / 60)

    for milestone in var.moneyMilestones:
        if var.money > milestone[0] and milestone not in var.milestonesUnlocked:
            func.news(milestone[1])
            var.milestonesUnlocked.append(milestone)
