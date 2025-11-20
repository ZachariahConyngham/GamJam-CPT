import os, time, math, sys, copy
import msvcrt


opnDialogue = [
    "...",
    "(You haven't bothered to add any dialogue intro yet.)",
    "(Very smart.)",
]
select = 0  # y pos of cursor
selectcol = 0  # x pos of cursor
location = "???"

class Generator:
    def __init__(self, name): # What is upgAB???? @campersonguy 
        self.name = name # Generator Name
        index = gnNames.index(name)
        self.desc = gnDesc[index] # Generator Description
        self.art = gnArt[index] # ASCII Art
        self.Money = Money(baseCost[index], gn[index], bMpS[index], MpS[index])
        self.Upgrades = Upgrades(upg[index], upgDesc[index], upgCost[index], upgAb[index]) # need to change upgAb[index] because there are some values like a-3 and stuff
        self.Prestige = Prestige(prestige[index], prName[index])

    class Money:
        def __init__(self, cost, bought, bMpS, MpS):
            self.baseCost = cost
            self.bought = bought
            self.bMpS = bMpS
            self.MpS = MpS
    
    class Upgrades:
        def __init__(self, upgrades, upgDescription, upgCost, upgAb):
            self.upg = upgrades
            self.upgDesc = upgDescription
            self.upgCost = upgCost
            self.upgAb = upgAb # Change this because there is a-3????

    class Prestige():
        def __init__(self, prestige, prName):
            self.pr = prestige
            self.prName = prName

gnNames = [  # generator names
    "Market Stand",
    "Green Grocer",
    "Car Wash",
    "McDolands",
    "Mine",
    "Shopping Centre",
    "Warehouse",
    "Hotel",
    "Bank",
    "Casino",
    "Power Plant",
]
gnDesc = [  # generator descriptions
    "A small market stand that will earn you some cash.",
    "A store that sells vegetables for a modest price.",
    "A new brand of Crystal Car Wash that will earn you some bucks.",
    "A factory of minimum wage workers doing the least amount of work possible.",
    "A cave full of high-value ores that can be extracted.",
    "A large marketplace centre that acts as the hub of shopping.",
    "A production warehouse that makes the latest line of toys, games, and everything in between.",
    "A manky has-been hotel that somehow still attracts visitors.",
    "A definitely-not-a-scam bank that prints hard cash.",
    "An illegal gambling facility, only for the elite.",
    "A nuclear power plant. Makes money one way or another.",
]

upg = {  # upgrade names for each generator
    0: ["Fresh Fruit", "Pesticides", "Selective Cultivar", "Tomacco", "GMF"],
    1: ["Leafy Greens", "12hr Shifts", "24hr Shifts", "Life Debt Contract", "Deal With The Manager"],
    2: ["Exquisite Soap", "SSS", "Diamond-Cutting-Water-Pressure-Jets", "Great Neptune's Ocean Wash This Dirt From My Car", "Nuclear Explosion Dried Cars"],
    3: ["Open 24/7", "Open 25/7", "Can I have 36 Burgers, 24 Large Cokes, ...", "1,000,000 Water Cups Please", "Roland McDoland's Obesity House"],
    4: ["Powerful Picks", "Drilling Machines", "Galindo Drill", "Mammoth Drill", "Explosive Beds"],
    5: ["Trading Hub", ""],
    6: ["Child Labour", ""],
    7: ["Room Service", ""],
    8: ["Thousand Dollar Bills", "Monopoly Money"],
    9: ["Weighty Dice", ""],
    10: ["Radioactive Waste", ""],
    11: ["More Cash", "Increased Profits"],
}
upgDesc = {  # upgrade descriptions
    0: ["Fresher Fruit = More Money", "Pesticides are the Besticides", "Only the best", "It's smooth and mild, and refreshingly addictive!", "Genetically Modified Fruit: Now with toys inside!"],
    1: ["Leafy Greens instead of Leafy Browns", "A long day", "A longer day and night", "You're never paying this off...", "Unfair deal: Give your soul to the manager"],
    2: ["Foamy Bubbles make for better marketing", "Super-Sonic Scrubbers", "I'm not wearing diamonds!", "Would rather / The multitudinous seas Burnt Umber / Making the green one brown", "Daily dose of Gamma Rays and free neutrons"],
    3: ["No downtime", "Owe downtime", "AAAAAAAAHHHHHHHHHHHH", "At least they said 'please'", "Honest marketing"],
    4: ["Cuts through the rock like butter", "Mining Inc", "The rocks won't see it coming", "Unnecessarily large", "SCP-████: Explodes when slept on by sentient humans. The average village does not apply"],
    5: ["Excavate through the stone even faster."],
    6: ["The hub of all trade - one might call it a trading hub."],
    7: ["Who doesn't love a pinch of child labour?"],
    8: ["Yes yes when the yes yes"],
    9: ["Condensed bills will make your stacks worth more."],
    10: ["It's almost as if these die always roll a six."],
    11: ["The more radioactive it is, the more it sells for."],
}
upgCost = {  # upgrade costs
    0: [500],
    1: [2000],
    2: [8000],
    3: [30000],
    4: [160000],
    5: [1300000],
    6: [24000000],
    7: [144000000],
    8: [750000000],
    9: [900000000],
    10: [85000000000],
    11: [500, 240000000000],
}
upgAb = [  # upgrade effects (1st is generator it affects (a is all), 2nd is amount - e.g 0-2 is market stand x2)
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

prestige = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] # what is this?
prName = [  # displays as Marketing I, Fresh Fruit I etc.
    "Advertising",
    "Variety",
    "Expensive Cars",
    "Minimum Wage",
    "Efficiency",
    "Shop Center",
    "Hard Work",
    "Housing",
    "Money Printing",
    "Gambling",
    "Radiation",
]


gnArt = [  # Depending on how many buildings, they buy, there will be a small animation that plays (like candybox2)
    [
        [
            "-------------------------------------",
            "|                                   |",
            "|          _┌┬┬┬┬┬┬┬┬┬┬┬┬┬┐         |",
            "|         |\|    Fruit    |         |",
            "|         | ╞╧╧╧╧╧╧╧╧╧╧╧╧╧╡         |",
            "|         | |     (ö)     |         |",
            "|         |\|     {█}     |         |",
            "|_________| ╞‡‡‡‡‡‡‡‡‡‡‡‡‡╡_________|",
            "|          \[▓▓▓▓▓▓▓▓▓▓▓▓▓]         |",
            "|                                   |",
            "-------------------------------------",

        ],
        [
            "-------------------------------------",
            "|                                   |",
            "|          _┌┬┬┬┬┬┬┬┬┬┬┬┬┬┐         |",
            "|         |\| Fresh Fruit |         |",
            "|         | ╞╧╧╧╧╧╧╧╧╧╧╧╧╧╡         |",
            "|         | |     (ö)     |         |",
            "|         |\|     {█}     |         |",
            "|_________| ╞‡‡‡‡‡‡‡‡‡‡‡‡‡╡_________|",
            "|          \[▓▓▓▓▓▓▓▓▓▓▓▓▓]         |",
            "|                                   |",
            "-------------------------------------",
        ],
        [
            "-------------------------------------",
            "|           ┌┬┬┬┬┬┬┬┬┬┬┬┬┬┐         |",
            "|          _|  Pest-Free  |         |",
            "|         |\| Fresh Fruit |         |",
            "|         | ╞╧╧╧╧╧╧╧╧╧╧╧╧╧╡         |",
            "|         | |     (ö)     |         |",
            "|         |\|     {█}     |         |",
            "|_________| ╞‡‡‡‡‡‡‡‡‡‡‡‡‡╡_________|",
            "|          \[▓▓▓▓▓▓▓▓▓▓▓▓▓]         |",
            "|                                   |",
            "-------------------------------------",
        ],
        [
            "-------------------------------------",
            "|           ┌┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┐   |",
            "|          _|  Pest-Free Better |   |",
            "|         |\| Fresh Fruit ├┴┴┴┴┴┘   |",
            "|         | ╞╧╧╧╧╧╧╧╧╧╧╧╧╧╡         |",
            "|         | |     (ö)     |         |",
            "|         |\|     {█}     |         |",
            "|_________| ╞‡‡‡‡‡‡‡‡‡‡‡‡‡╡_________|",
            "|          \[▓▓▓▓▓▓▓▓▓▓▓▓▓]         |",
            "|                                   |",
            "-------------------------------------",
        ],
        [
            "-------------------------------------",
            "|           ┌┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┐   |",
            "|          _|  Pest-Free Better |   |",
            "|         |\| Fresh Fruit ├┴┴┴┴┴┘   |",
            "|         | ╞╧╧╧╧╧╧╧╧╧╧╧╧╧╡         |",
            "|         | |     (ö) [Tomaccos]    |",
            "|         |\|     {█}     |         |",
            "|_________| ╞‡‡‡‡‡‡‡‡‡‡‡‡‡╡_________|",
            "|          \[▓▓▓▓▓▓▓▓▓▓▓▓▓]         |",
            "|                                   |",
            "-------------------------------------",
        ],
        [
            "-------------------------------------",
            "|           ┌┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┐   |",
            "|   ┌┬┬┬┬┬┬┬|  Pest-Free Better |   |",
            "|   |Healthy| Fresh Fruit ├┴┴┴┴┴┘   |",
            "|   └┴┴┴┴┴┴┴╞╧╧╧╧╧╧╧╧╧╧╧╧╧╡         |",
            "|         | |     (ö) [Tomaccos]    |",
            "|         |\|     {█}     |         |",
            "|_________| ╞‡‡‡‡‡‡‡‡‡‡‡‡‡╡_________|",
            "|          \[▓▓▓▓▓▓▓▓▓▓▓▓▓]         |",
            "|                                   |",
            "-------------------------------------",
        ],
    ],
    [
        [
            "-------------------------------------",
            "|                ┬─^─┬              |",
            "|           ┌────┘ ⌂ └────┐         |",
            "|     __↑___|Green Grocery|___↑     |",
            "|    |\╒╪═══╧═════════════╧═══╪╕    |",
            "|    | |      ╒════╦════╕      |    |",
            "|    | |      |    ║    |      |    |",
            "|    | |      |    ║    |      |    |",
            "|____| |      |    ║    |      |____|",
            "|     \[►─────┴────╨────┴─────◄]    |",
            "-------------------------------------",
        ],
        [
            "-------------------------------------",
            "|                ┬─^─┬              |",
            "|           ┌────┘ ⌂ └────┐         |",
            "|     __↑___|Green Grocery|___↑     |",
            "|    |\╒╪═══╧═════════════╧═══╪╕    |",
            "|    | |      ╒════╦════╕FRESH |    |",
            "|    | |      |    ║    | FRESH|    |",
            "|    | |      |    ║    |FRESH |    |",
            "|____| |      |    ║    | FRESH|____|",
            "|     \[►─────┴────╨────┴─────◄]    |",
            "-------------------------------------",
        ],
        [
            "-------------------------------------",
            "|                ┬─^─┬              |",
            "|           ┌────┘ ⌂ └────┐         |",
            "|     __↑___|Green Grocery|___↑     |",
            "|    |\╒╪═══╧═════════════╧═══╪╕    |",
            "|    | | OPEN ╒════╦════╕FRESH |    |",
            "|    | | 12/7 |    ║    | FRESH|    |",
            "|    | |      |    ║    |FRESH |    |",
            "|____| |      |    ║    | FRESH|____|",
            "|     \[►─────┴────╨────┴─────◄]    |",
            "-------------------------------------",
        ],
        [
            "-------------------------------------",
            "|                ┬─^─┬              |",
            "|           ┌────┘ ⌂ └────┐         |",
            "|     __↑___|Green Grocery|___↑     |",
            "|    |\╒╪═══╧═════════════╧═══╪╕    |",
            "|    | | OPEN ╒════╦════╕FRESH |    |",
            "|    | | 24/7 |    ║    | FRESH|    |",
            "|    | |      |    ║    |FRESH |    |",
            "|____| |      |    ║    | FRESH|____|",
            "|     \[►─────┴────╨────┴─────◄]    |",
            "-------------------------------------",
        ],
        [
            "-------------------------------------",
            "|                ┬─^─┬              |",
            "|           ┌────┘ ⌂ └────┐         |",
            "|     __↑___|Green Grocery|___↑     |",
            "|    |\╒╪═══╧═════════════╧═══╪╕    |",
            "|    | | OPEN ╒════╦════╕FRESH |    |",
            "|    | | Life |    ║    | FRESH|    |",
            "|    | | Long |    ║    |FRESH |    |",
            "|____| |      |    ║    | FRESH|____|",
            "|     \[►─────┴────╨────┴─────◄]    |",
            "-------------------------------------",
        ],
        [
            "-------------------------------------",
            "|                ┬─^─┬              |",
            "|           ┌────┘ ⌂ └────┐         |",
            "|     __↑___|Green Grocery|___↑     |",
            "|    |\╒╪═══╧═════════════╧═══╪╕    |",
            "|    | | OPEN ╒════╦════╕FRESH |    |",
            "|    | | For- |    ║    | FRESH|    |",
            "|    | | ever |    ║    |FRESH |    |",
            "|____| |      |    ║    | FRESH|____|",
            "|     \[►─────┴────╨────┴─────◄]    |",
            "-------------------------------------",
        ],
    ],
    [
        [
            "-------------------------------------",
            "|          ┌───CAR──WASH───┐        |",
            "|        |\|±±{▒▒▒▒▒▒▒▒▒}±±├┬┬┬┐    |",
            "|    ┌───┴─┤▒▒    ___    ▒▒|$$$|    |",
            "|    |Clean|▒▒ ┌─┴ΩΩΩ┴─┐ ▒▒╞╧╧╧╡    |",
            "|    |Cars!|▒▒ [_Ü_____] ▒▒|(ö)|    |",
            "|    └───┬─┤▒▒ |░░░░░░░| ▒▒|{█}|    |",
            "|________| |▒▒ []     [] ▒▒╞╬╬╬╡____|",
            "|         \|▒▒           ▒▒└╨╨╨┘    |",
            "|                                   |",
            "-------------------------------------",
        ],
        [
            "-------------------------------------",
            "|          ┌───CAR──WASH───┐        |",
            "|        |\|±±{▒▒▒▒▒▒▒▒▒}±±├┬┬┬┐    |",
            "|    ┌───┴─┤▒▒    ___    ▒▒|$$$|    |",
            "|    |Super|▒▒ ┌─┴ΩΩΩ┴─┐ ▒▒╞╧╧╧╡    |",
            "|    |Soap!|▒▒ [_Ü_____] ▒▒|(ö)|    |",
            "|    └───┬─┤▒▒ |░░░░░░░| ▒▒|{█}|    |",
            "|________| |▒▒ []     [] ▒▒╞╬╬╬╡____|",
            "|         \|▒▒           ▒▒└╨╨╨┘    |",
            "|                                   |",
            "-------------------------------------",
        ],
        [
            "-------------------------------------",
            "|          ┌───CAR──WASH───┐        |",
            "|        |\|±±{▒▒▒▒▒▒▒▒▒}±±├┬┬┬┐    |",
            "|    ┌───┴─┤▒▒    ___    ▒▒|$$$|    |",
            "|    |Super|▒▒ ┌─┴ΩΩΩ┴─┐ ▒▒╞╧╧╧╡    |",
            "|    |Fast!|▒▒ [_Ü_____] ▒▒|(ö)|    |",
            "|    └───┬─┤▒▒ |░░░░░░░| ▒▒|{█}|    |",
            "|________| |▒▒ []     [] ▒▒╞╬╬╬╡____|",
            "|         \|▒▒           ▒▒└╨╨╨┘    |",
            "|                                   |",
            "-------------------------------------",
        ],
        [
            "-------------------------------------",
            "|          ┌───CAR──WASH───┐        |",
            "|        |\|±±{▒▒▒▒▒▒▒▒▒}±±├┬┬┬┐    |",
            "|    ┌───┴─┤▒▒    ___    ▒▒|$$$|    |",
            "|    |Super|▒▒ ┌─┴ΩΩΩ┴─┐ ▒▒╞╧╧╧╡    |",
            "|    |Pure!|▒▒ [_Ü_____] ▒▒|(ö)|    |",
            "|    └───┬─┤▒▒ |░░░░░░░| ▒▒|{█}|    |",
            "|________| |▒▒ []     [] ▒▒╞╬╬╬╡____|",
            "|         \|▒▒           ▒▒└╨╨╨┘    |",
            "|                                   |",
            "-------------------------------------",
        ],
        [
            "-------------------------------------",
            "|          ┌───CAR──WASH───┐        |",
            "|        |\|±±{▒▒▒▒▒▒▒▒▒}±±├┬┬┬┐    |",
            "|    ┌───┴─┤▒▒    ___    ▒▒|$$$|    |",
            "|    |Super|▒▒ ┌─┴ΩΩΩ┴─┐ ▒▒╞╧╧╧╡    |",
            "|    |Neat!|▒▒ [_Ü_____] ▒▒|(ö)|    |",
            "|    └───┬─┤▒▒ |░░░░░░░| ▒▒|{█}|    |",
            "|________| |▒▒ []     [] ▒▒╞╬╬╬╡____|",
            "|         \|▒▒           ▒▒└╨╨╨┘    |",
            "|                                   |",
            "-------------------------------------",
        ],
        [
            "-------------------------------------",
            "|          ┌───CAR──WASH───┐        |",
            "|        |\|±±{▒▒▒▒▒▒▒▒▒}±±├┬┬┬┐    |",
            "|    ┌───┴─┤▒▒    ___    ▒▒|$$$|    |",
            "|    |Super|▒▒ ┌─┴ΩΩΩ┴─┐ ▒▒╞╧╧╧╡    |",
            "|    | Dry!|▒▒ [_Ü_____] ▒▒|(ö)|    |",
            "|    └───┬─┤▒▒ |░░░░░░░| ▒▒|{█}|    |",
            "|________| |▒▒ []     [] ▒▒╞╬╬╬╡____|",
            "|         \|▒▒           ▒▒└╨╨╨┘    |",
            "|                                   |",
            "-------------------------------------",
        ],
    ],
    [
        "-------------------------------------",
        "| ┌~─~─~~─~─~┐┌──────────────────┐  |",
        "| ‡MacDolands‡\┌──────/#\/#\──────┐ |",
        "| └~─~─╦╦-~─~┘\| WOW /#/\/\#\ WOW | |",
        "|      ╟╢    | ├─────\/────\/─────┤ |",
        "|      ╟╢    | | Bun  ╒════╕  Fry | |",
        "|______╟╢____| | Ham  |   ·|  Fry |_|",
        "|      ╟╢     \| Bun  |    | Frys | |",
        "|      ╟╢      └──────┴────┴──────┘ |",
        "|                     \     \       |",
        "-------------------------------------",
    ],
    [
        "-------------------------------------",
        "|    \_/       \__                  |",
        "|                 \_                |",
        "|    ──} THE      __\               |",  # upgrade gives Ω hat to the guy (tuff idea kai)
        "|       MINES{──  |      (ö)        |",
        "|       +---+     |      {█}        |",
        "|       |   |      \   ┌──────┐     |",
        "|      _|___|_______\  | coal | /ø\ |",
        "|    _/                └──────┘/øøø\|",
        "|___/                {── {──        |",
        "-------------------------------------",
    ],
    [
        "-------------------------------------",
        "|                ___                |",
        "|               [MON]               |",
        "|  ┌───────────[01:01]───────────┐  |",
        "|  |       (_Shop Centre_)       |  |",  # add stalls, (idk how to because it's a shop centre. But i plan to like make billboards that show after upgrades)
        "|  | [FoolForths]        [Koles] |  |",
        "|  |                             |  |",
        "|  |            ╒═╦═╕            |  |",
        "|  |            | ║ |            |  |",
        "|  └─────±±±±±──┴─╨─┴──±±±±±─────┘  |",
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
        "|                                   |",
        "-------------------------------------",
    ],
]

mapArt = [
    [  # Starter map
        "-------------------------------------------------------------",
        "|    (F)   (?)   (?)   (?)   (?)   (?)   (?)   (?)   (?)    |",
        "|    (?)   (?)   (?)   (?)   (?)   (?)   (?)   (?)   (?)    |",
        "|    (?)   (?)   (?)   (?)   (?)   (?)   (?)   (?)   (?)    |",
        "|    (?)   (?)   (?)   (?)   (?)   (?)   (?)   (?)   (?)    |",
        "|    (?)   (?)   (?)   (?)   (?)   (?)   (?)   (?)   (?)    |",
        "|    (?)   (?)   (?)   (?)   (?)   (?)   (?)   (?)   (?)    |",
        "|    (?)   (?)   (?)   (?)   (?)   (?)   (?)   (?)   (?)    |",
        "|    (?)   (?)   (?)   (?)   (?)   (?)   (?)   (?)   (?)    |",
        "|    (?)   (?)   (?)   (?)   (?)   (?)   (?)   (?)   (?)    |",
        "-------------------------------------------------------------",
    ],
    [  # Completed map
        "-------------------------------------------------------------",
        "|    (F)   (M)   (S)   (M)   (M)   (S)   (C)   (D)   (B)    |",
        "|    (S)   (C)   (C)   (S)   (S)   (M)   (C)   (C)   (M)    |",
        "|    (M)   (D)   (S)   (S)   (M)   (C)   (S)   (S)   (M)    |",
        "|    (C)   (S)   (M)   (C)   (C)   (M)   (C)   (M)   (S)    |",
        "|    (S)   (C)   (S)   (M)   (S)   (D)   (S)   (S)   (C)    |",
        "|    (D)   (S)   (M)   (C)   (M)   (S)   (M)   (C)   (D)    |",
        "|    (M)   (M)   (M)   (D)   (S)   (C)   (M)   (S)   (C)    |",
        "|    (C)   (M)   (C)   (C)   (S)   (M)   (S)   (C)   (S)    |",
        "|    (G)   (S)   (C)   (C)   (C)   (S)   (M)   (D)   (H)    |",
        "-------------------------------------------------------------",
    ],
]

map = {
    "0": ["F", "?", "?", "?", "?", "?", "?", "?", "?"],
    "1": ["?", "?", "?", "?", "?", "?", "?", "?", "?"],
    "2": ["?", "?", "?", "?", "?", "?", "?", "?", "?"],
    "3": ["?", "?", "?", "?", "?", "?", "?", "?", "?"],
    "4": ["?", "?", "?", "?", "?", "?", "?", "?", "?"],
    "5": ["?", "?", "?", "?", "?", "?", "?", "?", "?"],
    "6": ["?", "?", "?", "?", "?", "?", "?", "?", "?"],
    "7": ["?", "?", "?", "?", "?", "?", "?", "?", "?"],
    "8": ["?", "?", "?", "?", "?", "?", "?", "?", "?"],
}


mapDesc = [
    "The universe you first found yourself in after the accident. ",  # F
    "What you presume is your original universe... ",  # H
    "??? ",  # ?
    "A rich smelling universe. ",  # m (more money)
    "A universe that makes you feel more like yourself. ",  # s (reduced sanity)
    "A universe in which inflation never existed. ",  # c (cost reduction)
    "A universe full of funny little games to play. ",  # G (minigames)
    "A strange universe full of chaos and destruction. ",  # D (debuffs everything)
    "A happy universe where everything goes just right. ",  # B (buffs everything)
]

gn = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # amounts of each generator, this basically covers bought
bMpS = [
    0.5,
    6,
    24,
    60,
    200,
    750,
    1400,
    5500,
    18000,
    40000,
    125000,
]  # base money per second
MpS = []  # actual money per second
tMpS = 0.5  # total money per second
baseCost = [  # Starting Cost of Every Building
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
currentCost = copy.deepcopy(baseCost)
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
#(self, name, description, upgrades, upgDescription, upgCost, upgAb, prestige, prName, art, bMpS, cost):
market = Generator("Market Stand")
grocer = Generator("Green Grocer")
carWash = Generator("Car Wash")
mcdolands = Generator("McDolands")
mine = Generator("Mine")
shopCentre = Generator("Shopping Centre")
warehouse = Generator("Warehouse")
hotel = Generator("Hotel")
bank = Generator("Bank")
casino = Generator("Casino")
powerPlant = Generator("Power Plant")

money = 0
day = 0
page = 0
sanity = 100
costmult = 1
sanmult = 1  # sanity decrease multiplier
warp = 0


# where the running actually starts
