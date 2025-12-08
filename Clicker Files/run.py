import sys, time, os, math, msvcrt, shutil
import functions as func
import variables as var
from Minigames import hangman, blackjack, ROSHAMBO, snakes_ladders, skills_gamblingtime

disable = False

func.load()
print("\033[?25l", end="")  # Hides the player cursor

def savecode():
    var.page = 4
    func.load()

def loadsave():
    func.clear()
    quit()

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
                    if var.money >= var.generators[var.placeNames[var.select]]["Money"]["cost"] * (var.ramping ** var.gn[var.select]) and var.selected == True:
                        var.money -= round(var.generators[var.placeNames[var.select]]["Money"]["cost"] * (var.ramping ** var.gn[var.select]), 2)
                        var.gn[var.select] += 1
                if var.page == 1 and var.select != -1 and var.selected == True:
                    if var.selectcol == 1:
                        func.buyupgrade()
                    if var.selectcol == 2:
                        func.buyprestige()
                if var.page == 3 and var.select != -1 and not var.select >= len(var.settings):
                    var.settings[var.select] = not var.settings[var.select]
                if var.page == 3 and var.select == len(var.settings):
                    savecode()
                if var.page == 3 and var.select == len(var.settings) + 1:
                    loadsave()

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
                var.select = max(-1, min(var.select, len(var.settings) + 1))
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
    func.update()
    
    time.sleep(0.02)

    shift = round((shutil.get_terminal_size().columns / 2) - 40)

    var.tMpS = 0
    
    if var.page != 4:
        for i in range(len(var.gn)):  # calculating money increase and sanity loss
            mult = 1
            var.tMpS += var.MpS[i] * var.gn[i] * (2 ** (var.upgBought[i])) * (1.2 ** (var.prestige[i] - 1))

            var.money += var.MpS[i] * var.gn[i] * (2 ** (var.upgBought[i])) * (1.2 ** (var.prestige[i] - 1)) * 0.02

            var.cost[i] = var.baseCost[i] * (0.8 ** (var.prestige[i] - 1))
        var.sanity -= var.sanmult * 0.02 * (1 / 60)

