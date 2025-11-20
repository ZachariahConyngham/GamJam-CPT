import os, time, math, sys, copy
import msvcrt


opndialogue = [
    "...",
    "(You haven't bothered to add any dialogue intro yet.)",
    "(Very smart.)",
]
select = 0  # y pos of cursor
selectcol = 0  # x pos of cursor
location = "???"


gnnames = [  # generator names
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
gndesc = [  # generator descriptions
    "A small market stand that will earn you some cash.",
    "A store that sells vegetables for a modest price.",
    "A new brand of Crystal Car Wash that will earn you some bucks.",
    "A factory of minimum wage workers doing the least amount of work possible.",
    "A cave full of high-value ores that can easily be extracted.",
    "A large marketplace centre that acts as the hub of shopping.",
    "A production warehouse that makes the latest line of toys, games, and everything in between.",
    "A manky has-been hotel that somehow still attracts visitors.",
    "A definitely-not-a-scam bank that prints hard cash.",
    "An illegal gambling facility, only for the elite.",
    "A nuclear power plant. Makes money one way or another.",
]

upg = {  # upgrade names for each generator
    0: ["Marketing Increase"],
    1: ["Fresh Fruit", "Pesticides", "Selective Cultivar", "GMF", "Peak Hours"],
    2: ["Exquisite Soap", ""],
    3: ["16 Hour Shifts", ""],
    4: ["Powerful Picks", ""],
    5: ["Trading Hub", ""],
    6: ["Child Labour", ""],
    7: ["Room Service", ""],
    8: ["Thousand Dollar Bills", "Monopoly Money"],
    9: ["Weighty Dice", ""],
    10: ["Radioactive Waste", ""],
    11: ["More Cash", "Increased Profits"],
}
upgdesc = {  # upgrade descriptions
    0: ["Produce a little more money."],
    1: ["The better your marketing is, the more you'll make."],
    2: ["Finer fruits sell for more profits."],
    3: ["These cars are gonna be eaten off when you're done with them."],
    4: ["There's no way this is legal."],
    5: ["Excavate through the stone even faster."],
    6: ["The hub of all trade - one might call it a trading hub."],
    7: ["Who doesn't love a pinch of child labour?"],
    8: ["Yes yes when the yes yes"],
    9: ["Condensed bills will make your stacks worth more."],
    10: ["It's almost as if these die always roll a six."],
    11: ["The more radioactive it is, the more it sells for."],
}
upgcost = {  # upgrade costs
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
upgab = [  # upgrade effects (1st is generator it affects (a is all), 2nd is amount - e.g 0-2 is market stand x2)
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

prestige = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
prnames = [  # displays as Marketing I, Fresh Fruit I etc.
    "Marketing",
    "Fresh Fruit",
    "Soap",
    "Minimum Wage",
    "Efficiency",
    "Shop Center",
    "Hard Work",
    "Housing",
    "Money Printing",
    "Gambling",
    "Radiation",
]


gnart = [  # Depending on how many buildings, they buy, there will be a small animation that plays (like candybox2)
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
        "|  |       (_Shop Centre_)       |  |",  # add stalls
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


mapart = [
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


mapdesc = [
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

gn = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # amounts of each generator
bmps = [
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
mps = [
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
]  # actual money per second
tmps = 0.5  # total money per second
cost = [  # Starting Cost of Every Building
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


money = 0
day = 0
page = 0
sanity = 100
costmult = 1
sanmult = 1  # sanity decrease multiplier
warp = 0


# where the running actually starts
