import sys, time, os, math, msvcrt
import functions as func
import variables as var
from Minigames import (
    hangman,
    blackjack,
    ROSHAMBO,
    snakes_ladders,
    skills_gamblingtime,
)

func.clear()
skip = input("Do you want to skip opening dialogue? (Y/N) ").upper()
if skip != "Y":
    func.clear()
    for line in var.dialogue[0]:
        if line != "clear":
            func.yap(line)
            time.sleep(1)
            print("\n")
        else:
            func.clear()

func.load()
print("\033[?25l", end="")  # Hides the player cursor

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
                    if var.selected == False:
                        var.selected = True
                    else:
                        var.selected = False
                        if var.money >= var.generators[var.placeNames[var.select]][
                            "Money"
                        ]["cost"] * (var.ramping ** var.gn[var.select]):
                            var.money -= round(
                                var.generators[var.placeNames[var.select]]["Money"][
                                    "cost"
                                ]
                                * (var.ramping ** var.gn[var.select]),
                                2,
                            )
                            var.gn[var.select] += 1
                if var.page == 1 and var.selectcol == 0 and var.select != -1:
                    if money >= var.upgcost[var.select]:
                        money -= round(var.upgcost[var.select], 2)
                        var.bought.append(var.upgab[var.select])
                        var.upg.remove(var.upg[var.select])
                        var.upgcost.remove(var.upgcost[var.select])
                        var.upgdesc.remove(var.upgdesc[var.select][0])
                        var.upgab.remove(var.upgab[var.select])
                if (
                    var.page == 3 and var.select != -1
                ):  # ZAC PUT YO SHI HEREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEe
                    var.page = 4
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
                var.select = max(-1, min(var.select, len(var.minigames) - 1))
            case 3:
                var.select = max(-1, min(var.select, 10))

        if var.select == -1:
            var.selectcol = max(0, min(var.selectcol, 3))
        elif var.page == 1:
            var.selectcol = max(1, min(var.selectcol, 2))
        elif var.page == 3 and var.select > -1:
            var.selectcol = max(0, min(var.selectcol, 8))
        else:
            var.selectcol = 0

    func.update()
    time.sleep(0.02)

    var.tMpS = 0

    for i in range(len(var.gn)):  # calculating money increase and sanity loss
        mult = 1
        var.tMpS += var.MpS[i] * var.gn[i]

        var.money += var.MpS[i] * var.gn[i] * 0.02
    var.sanity -= var.sanmult * 0.02 * (1 / 60)
