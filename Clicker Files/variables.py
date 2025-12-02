import copy
from ascii_art import gnArt

stupidNames = {  # trust US with YOUR naming conventions
    10: ["Cheezle McZonkponk"],
    0: ["John Breakfast", "George Lunch", "Jim Dinner"],  # food
    1: ["John Feast", "Jim Feast"],
    2: ["John Cologne", "Joel Colon", "Donald Obama"],  # people
    3: ["John Mantle", "John Quixote", "Hornet Spaghetti", "Steve", "Vincent Whittman", "John Supercell", "Meger Nite", "Papyrus", ""],
    4: ["John Knobe", "Dor Knobe"],
    5: ["John Placeholder"],
    6: ["John nhoJ", "Jim miJ"],
    7: ["John Short", "John Tall", "Jim Short", "John Medium", "John Small", "John Creamer"],  # size
    8: ["", "", ],
    9: ["John John", "John John John", "John John John John", "John John John John John"],  # number of johns
}

unix = 0  # universe coords on map
uniy = 0

longform = True # how numbers are displayed.

dialogue = {
    1: [  # opening dialogue
        "...",
        "The world is spinning around you... ",
        "You feel like you are being pulled in every direction... ",
        "Every part of your body is screaming in agony... ",
        "...",
        "...",
        "...",
        "clear",
        "You awake to the sound of water running nearby. ",
        "You find yourself in a place that is vaguely familiar... ",
        "You decide to explore to find out where you have arrived... ",
        "clear",
        "You see the outline of a city in the distance... ",
        "You realise you remember nothing from before you woke up... ",
        "'Hey there, " + stupidNames[uniy][unix] + "'",
        "Something about the name you were called seems wrong but you can't figure out what it is...",
        "By the time you realise this the person who spoke is already walking away...",
    ],
    2: [  # Research station built
        "You have constructed the Research Station... ",
        "Maybe you can find out how you ended up here...",
    ],
    3: [  # satellite dialogue
        "As you stare upon the earth from your satelite... ",
        "You realise you can't deny it anymore...",
        "This world can't be your Earth... ",
        "Your portal must have worked... ",
        "",
    ],
    4: [  # portal dialogue
        "You have completed a device that should be able to send you to a different reality",
        "Whether that reality is your reality remains to be seen",
    ],
    0: [ # Your universe with correct name
        "As you exit the portal you hear a familiar voice...",
        "'Is that you ___?'",
        "You have finally found your home...",
        "Your journey is over...",
        "But some part of you doesn't want it to end yet...", # if user hasn't found their true name
        "That small part enjoyed the adventures you went on...",
        "The wealth you acquired...",
        "The friends you made...",
        "" # input "do you want to return to your previous life or ... Do you want to resume your journey of hopping between realities"
    ],
    5: [ # Your universe
        "As you exit the portal, you find yourself in a white room... ",
        "As you try to figure out where you are a voice speaks, seemingly from every direction...",
        "'What is your name?'", #input (what is your name)
    ],
    5.1: [
        "'Incorrect. Go back to your own reality'",
        "You feel a force pushing you back into the portal...",
        "You wake to find yourself where you originally woke up..."
        "Maybe if you found the right name the voice would let you through...",
    ],
    6: [ # undecided

    ]
}

select = 0  # y pos of cursor
selectcol = 0  # x pos of cursor



print()

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
    7: ["Breakfast Buffet", ""],
    8: ["Thousand Dollar Bills", "Monopoly Money"],
    9: ["Weighty Dice", ""],
    10: ["Radioactive Waste", ""],
}

upgDesc = {  # upgrade descriptions
    0: [
        "Fresher fruit means happier customers means more money.",
        "Pesticides are the Besticides!",
        "Only the best cultivar used for your store.",
        "It's smooth and mild, and refreshingly addictive!",
        "Genetically Modified Fruit: Now with toys inside!",
    ],
    1: [
        "Leafy Greens instead of Leafy Browns.",
        "A long day for the workers.",
        "The most openiest and unclosiest maybe possibly clopen store.",
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
    5: ["The hub of all trade - one might call it a trading hub."],
    6: ["Who doesn't love a pinch of child labour?"],
    7: ["What better way to start your day than with a buffet?"],
    8: ["Condensed bills will make your stacks worth more."],
    9: ["It's almost as if these die always roll a six."],
    10: ["The more radioactive it is, the more it sells for."],
}

upgCost = [  # Base Upgrade Cost
    [5500, 7000],
    [2000, 16000],
    [8000, 56000],
    [30000, 112000],
    [160000, 800000],
    [1300000, 9000000],
    [24000000, 172000000],
    [144000000],
    [750000000],
    [9000000000],
    [85000000000],
]

upgBought = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Upgrades that have been bought for each tier

prestige = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

prName = [
    "Advertising",
    "Variety",
    "Shiny Soap",
    "Minerals",
    "Efficiency",
    "Marketing",
    "Machinery",
    "Customer Service",
    "Money Printing",
    "Gambling",
    "Nuclear Efficiency",
]

map = {  # What is this for Zach? maybe put this somewhere else like below all of the generator variables
    0: [1, 0, 0, 0, 0, 0, 0, 0, 0],
    1: [0, 0, 0, 0, 0, 0, 0, 0, 0],
    2: [0, 0, 0, 0, 0, 0, 0, 0, 0],
    3: [0, 0, 0, 0, 0, 0, 0, 0, 0],
    4: [0, 0, 0, 0, 0, 0, 0, 0, 0],
    5: [0, 0, 0, 0, 0, 0, 0, 0, 0],
    6: [0, 0, 0, 0, 0, 0, 0, 0, 0],
    7: [0, 0, 0, 0, 0, 0, 0, 0, 0],
    8: [0, 0, 0, 0, 0, 0, 0, 0, 0],
    9: [0, 0, 0, 0, 0, 0, 0, 0, 0],
    10: [0, 0, 0, 0, 0, 0, 0, 0, 8],
}

mapKeys = ["?", "F", "M", "S", "C", "G", "D", "B", "H"]


mapDesc = [
    "??? ",  # ?
    "The universe you first found yourself in after the accident. ",  # F
    "A rich smelling universe. ",  # m (more money)
    "A universe that makes you feel more like yourself. ",  # s (reduced sanity)
    "A universe in which inflation never existed. ",  # c (cost reduction)
    "A universe full of funny little games to play. ",  # G (minigames)
    "A strange universe full of chaos and destruction. ",  # D (debuffs everything)
    "A happy universe where everything goes just right. ",  # B (buffs everything)
    "What you presume is your original universe... ",  # H
]

gn = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # amounts of each generator, this basically covers bought

bMpS = [0.5, 6, 24, 60, 200, 750, 1400, 5500, 18000, 40000, 125000]  # base money per second
MpS = [0.5, 6, 24, 60, 200, 750, 1400, 5500, 18000, 40000, 125000]  # actual money per second
tMpS = 0.5  # total money per second
baseCost = [2, 60, 900, 8500, 55000, 240000, 3500000, 50000000, 444444444, 7000000000, 80000000000] # Starting Cost of Every Building
cost = [2, 60, 900, 8500, 55000, 240000, 3500000, 50000000, 444444444, 7000000000, 80000000000]

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

suffixes = [  # for shortening numbers
    "", "k", " million", " billion", " trillion", " quadrillion", " quintillion", " sextillion", " septillion", " octillion", " nonillion", " decillion",
    " undecillion", " duodecillion", " tredecillion", " quattuordecillion", " quindecillion", " sexdecillion", " septendecillion", " octodecillion", " novemdecillion", " vigintillion",
    " unvigintillion", " duovigintillion", " trevigintillion", " quattuorvigintillion", " quinvigintillion", " sexvigintillion", " septvigintillion", " octovigintillion", " novemvigintillion", " trigintillion",
    " untrigintillion", " duotrigintillion", " tretrigintillion", " quattuortrigintillion", " quintrigintillion", " sestrigintillion", " septentrigintillion", " octotrigintillion", " noventrigintillion", " quadragintillion",
    " unquadragintillion", " duoquadragintillion", " trequadragintillion", " quattuorquadragintillion", " quinquadragintillion", " sesquadragintillion", " septenquadragintillion", " octoquadragintillion", " novemquadragintillion", " quinquagintillion",
    " unquinquagintillion", " duoquinquagintillion", " trequinquagintillion", " quattuorquinquagintillion", " quinquinquagintillion", " sesquinquagintillion", " septenquinquagintillion", " octoquinquagintillion", " novemquinquagintillion", " sexagintillion",
    " unsexagintillion", " duosexagintillion", " tresexagintillion", " quattuorsexagintillion", " quinsexgintillion", " sessexagintillion", " septensexagintillion", " octosexagintillion", " novensexagintillion",  " septuagintillion",
    " unseptuagintillion", " duoseptuagintillion", " treseptuagintillion", " quattuorseptuagintillion", " quinseptuagintillion", " sesseptuagintillion", " octoseptuagintillion", " novenseptuagintillion", " octagintillion",
    " unoctagintillion", " duooctagintillion", " treoctagintillion", " quattuoroctagintillion", " quinoctagintillion", " sesoctagintillion", " septenoctagintillion", " octooctagintillion", " novenoctagintillion", " nonagintillion",
    " unnonagintillion", " duononagintillion", " trenonagintillion" , " quattuornonagintillion", " quinnonagintillion", " sesnonagintillion", " septennonagintillion", " octononagintillion", " novennonagintillion", " centillion",
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
            },
            "Prestige": {"lvl": prestige[index], "name": prName[index]},
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
