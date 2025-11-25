import copy
from ascii_art import gnArt

opnDialogue = [
    "...",
    "(You haven't bothered to add any dialogue intro yet.)",
    "(Very smart.)",
]
select = 0  # y pos of cursor
selectcol = 0  # x pos of cursor
location = "???"

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

placeNames = [  # placeholder names
    "market",
    "grocer",
    "carWash",
    "mcdolands",
    "mine",
    "shopCentre",
    "warehouse",
    "hotel",
    "bank",
    "casino",
    "plant",
]

gnDesc = [  # generator descriptions
    "A small market stand that will earn you some cash.",
    "A store that sells vegetables for a modest price.",
    "A new brand of Crystal Car Wash that will earn you some bucks.",
    "A factory of minimum wage workers doing the least amount of work possible.",
    "A cave full of high-value ores that can be extracted.",
    "A large marketplace centre that acts as the hub of shopping.",
    "A production warehouse that makes the latest line of toys, games, and everything in between.",
    "A luxurious hotel fit only for the richest.",
    "A definitely-not-a-scam bank that prints hard cash.",
    "An illegal gambling facility, only for the elite.",
    "A nuclear power plant. Makes money one way or another.",
]

upg = {  # upgrade names for each generator
    0: ["Fresh Fruit", "Pesticides", "Selective Cultivar", "Tomacco", "GMF"],
    1: [
        "Leafy Greens",
        "12hr Shifts",
        "The Openestest",
        "Life Debt Contract",
        "Deal With The Manager",
    ],
    2: [
        "Exquisite Soap",
        "SSS",
        "Diamond-Cutting-Water-Pressure-Jets",
        "Great Neptune's Ocean Wash This Dirt From My Car",
        "Nuclear Explosion Dried Cars",
    ],
    3: [
        "All Day Open",
        "Open 25/8",
        "Fat Load Order",
        "One Thousand Nuggets",
        "Roland McDoland's Obesity House",
    ],
    4: [
        "Powerful Picks",
        "Drilling Machines",
        "Galindo Drill",
        "Mammoth Drill",
        "Bed Bombers",
    ],
    5: ["Trading Hub", ""],  # kai add whatever you need in these ones
    6: ["Child Labour", ""],
    7: ["Room Service", ""],
    8: ["Thousand Dollar Bills", "Monopoly Money"],
    9: ["Weighty Dice", ""],
    10: ["Radioactive Waste", ""],
    11: ["More Cash", "Increased Profits"],  # increases all
}

upgDesc = {  # upgrade descriptions
    0: [
        "Fresher Fruit = More Money",
        "Pesticides are the Besticides",
        "Only the best",
        "It's smooth and mild, and refreshingly addictive!",
        "Genetically Modified Fruit: Now with toys inside!",
    ],
    1: [
        "Leafy Greens instead of Leafy Browns",
        "A long day",
        "A longer day and night",
        "You're never paying this off...",
        "Unfair deal: Give your soul to the manager",
    ],
    2: [
        "A bubble bath for cars.",
        "Super Scrubbers make your car shine brighter than the heavens in the skies above.",
        "I'm not wearing diamonds!",
        "Would rather / The multitudinous seas Burnt Umber / Making the green one brown",
        "Daily dose of Gamma Rays and free neutrons!",
    ],
    3: [
        "No downtime, no weaknesses.",
        "An extra hour to keep your workers busy.",
        "Can I have 36 Big Macs, 24 large Cokes...",
        "At least they said 'please'...",
        "The most honest marketping campaign in the big two five.",
    ],
    4: [
        "A sharpened pickaxe that cuts through ore like butter.",
        "A powerful drill designed to cleave through stone.",
        "The ultimate Mining Incorporated midgame mining machine.",
        "Unnecessarily large for an excavation of that size.",
        "Explodes when slept on by sentient humans. The average villager does not apply.",
    ],
    5: ["Excavate through the stone even faster."],
    6: ["The hub of all trade - one might call it a trading hub."],
    7: ["Who doesn't love a pinch of child labour?"],
    8: ["Yes yes when the yes yes"],
    9: ["Condensed bills will make your stacks worth more."],
    10: ["It's almost as if these die always roll a six."],
    11: ["The more radioactive it is, the more it sells for."],
}

upgCost = [  # Base Upgrade Cost
    500,
    2000,
    8000,
    30000,
    160000,
    1300000,
    24000000,
    144000000,
    750000000,
    900000000,
    85000000000,
    [500, 240000000000],
]
upgMult = [  # on second thought i lowk might leave it
    # also can we STOP PINGING ME IN THE CODE BRO 😭😭😭😭😭 IT DOESN'T EVEN DO ANYTHING
    "0-2",
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
    "0-3",
]

prName = [  # displays as Marketing I, Fresh Fruit I etc.
    "Advertising",
    "Variety",
    "Expensive Cars",
    "Minerals",
    "Efficiency",
    "Marketing",
    "Machinery",
    "Customer service",
    "Money Printing",
    "Fast Dealers",
    "Nuclear Efficiency",
]

map = {  # What is this for Zach? maybe put this somewhere else like below all of the generator variables
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

gn = [
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
]  # amounts of each generator, this basically covers bought

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
MpS = [
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
ramping = 1.25  # Base cost ramping

minigames = [
    "Guess the Number",
    "Roshambo",
    "Hangman",
    "Blackjack",
    "Snakes and Ladders",
    "Battleships",
]


def initiate_generators(name, placeholder_name):
    index = gnNames.index(name)
    generator_template = {
        placeholder_name: {
            "name": name,
            "index": index,
            "desc": gnDesc[index],
            "art": gnArt[index],
            "Money": {
                "baseCost": baseCost[index],
                "ramping": ramping,
                "cost": baseCost[index],
                "bought": gn[index],
                "bMpS": bMpS[index],
                "MpS": MpS[index],
            },
            "Upgrades": {
                "upg": upg[index],
                "desc": upgDesc[index],
                "cost": upgCost[index],
                "mult": upgMult[index],
            },
            "Prestige": {"lvl": 0, "name": prName[index]},
        }
    }
    return generator_template


generators = {
    **initiate_generators("Market Stand", "market"),
    **initiate_generators("Green Grocer", "grocer"),
    **initiate_generators("Car Wash", "carWash"),
    **initiate_generators("McDolands", "mcdolands"),
    **initiate_generators("Mine", "mine"),
    **initiate_generators("Shopping Centre", "shopCentre"),
    **initiate_generators("Warehouse", "warehouse"),
    **initiate_generators("Hotel", "hotel"),
    **initiate_generators("Bank", "bank"),
    **initiate_generators("Casino", "casino"),
    **initiate_generators("Power Plant", "plant"),
}

money = 0
day = 0
page = 0
sanity = 100
costmult = 1
sanmult = 1  # sanity decrease multiplier
warp = 0
