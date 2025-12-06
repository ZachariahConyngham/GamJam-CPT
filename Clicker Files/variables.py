import copy, os
from ascii_art import gnArt

stupidNames = {  # trust US with YOUR naming conventions
    10: ["Cheezle McZonkponk"],
    0: ["Doctor John Breakfast", "George Lunch", "Jim Dinner", "Ned Stark", "", "", "", "", "x"],  # food
    1: ["John Feast", "Jim Feast", "", "", "", "", "", "", ""], #
    2: ["John Cologne", "Joel Colon", "Donald Obama", "", "", "", "", "", ""],  # people
    3: ["John Mantle", "John Quixote", "Hornet Spaghetti", "Steve", "Vincent Whittman", "John Supercell", "Meger Nite", "Papyrus", "Quirrel"],
    4: ["John Knobe", "Dor Knobe", "", "", "", "", "", "", ""],
    5: ["John Placeholder", "", "", "", "XY Snow", "", "", "", ""],
    6: ["John nhoJ", "Jim miJ", "", "", "", "", "", "", ""],
    7: ["John Short", "John Tall", "Jim Short", "John Medium", "John Small", "", "", "", ""],  # size
    8: ["John John", "John John John", "John John John John", "John John John John John", "", "", "", "", ""],  # number of johns
    9: ["y", "", "", "", "", "", "", "", "Snow"],
}

unix = 0  # universe coords on map
uniy = 0

shift = 40  # shifting the box horizontally
lineshift = 0  # vertically

longform = True # how numbers are displayed.

dialogue = {
    0: [  # opening dialogue
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
    1: [  # Research station built
        "You have constructed the Research Station... ",
        "Maybe you can find out how you ended up here...",
    ],
    2: [  # satellite dialogue
        "As you stare upon the earth from your satelite... ",
        "You realise you can't deny it anymore...",
        "This world can't be your Earth... ",
        "Your portal must have worked... ",
        "",
    ],
    3: [ # portal dialogue
        "You have completed a device that should be able to send you to a different reality",
        "Whether that reality is your reality remains to be seen",
    ],
    4: [ # New universe dialogue - unimportant universe
        "As you exit the portal you find yourself in a familiar park", 
        "You see the outline of a city around you... ",
        "'Hey there, " + stupidNames[uniy][unix] + "'",
        "Something about the name you were called seems wrong but you can't figure out what it is...",
        "By the time you realise this the person who spoke is already walking away...",
    ],
    5: [ # Fake universe + 3rd part of true name
        "As you exit the portal you find yourself in an endless white void... ", 
        "This reality has been destroyed... ", 
        "You notice what appears to be crack in reality that spells out; " + stupidNames[uniy][unix] + "...",
        "Something about that word sounds familiar but you can't figure out what it is",
        "In denial you decide to look through the rest of the realities in the hope that this universe isn't your own... ",  # sanity decreases faster with each reality checked
    ],
    6.0: [ # Your universe
        "As you exit the portal, you find yourself in a white room... ",
        "As you try to figure out where you are a voice speaks, seemingly from every direction...",
        "'What is your name?'",  # if any parts of name have been found go to 8 else input (what is your name) 
        "",
    ],
    6.1: [ # wrong name
        "'Incorrect. You are not the person from this reality. Go back to your own one'",
        "You feel a force pushing you back into the portal...",
        "You wake to find yourself where you originally woke up..."
        "Maybe if you found the right name the voice would let you through...", # sent to a random reality that has already been discover
    ],
    7.1: [ # reality with 1st part of true name
        "x... ",
        "That name...",
        "It sounded so familiar...",
        "Like you had heard it thousands of times before...",
        "x... ",
    ],
    7.2: [ # reality with 2nd part of true name
        "y... ",
        "That name... ",
        "It sounded so familiar... ",
        "Like you had heard it thousands of times before... ",
        "y... ",
    ],
    8.0: [ # true reality with all 3 parts of true name
        "You think back to your previous adventures, trying to remember your name... ",
        "", 
    ],
    8.1: [
        "You remember the name x... ", 
        "How you had been called that many times... ", # first name
        "Before you decided to volunteer to test the portal"
    ],
    8.2: [
        "You remember the familiarity of the name y... ", # middle name
        "How often you wrote it... ", 
        "Before you decided to pour your heart into your creation"
    ],
    8.3: [
        "You remember the familiarity of the name Snow... ", # reference to an important name
        "Snow was your family name... ", 
        "Before you decided to volunteer to test that dreaded portal... "
    ],

    9: [ # Your universe with correct name
        "You speak clearly the name X Y Snow"
        "The white walls slowly descend as a familiar voice starts to speak... ",
        "'I have waited years for you to return'",
        "The walls slide into the floor leaving you face to face with xyz... "
        "'Is it really you ___?'",
        "You have finally found your home...",
        "You have reunited with xyz...",
        "Your journey is over...",
        "But some part of you doesn't want it to end yet...", 
        "That small part enjoyed the adventures you went on...",
        "The wealth you acquired...",
        "The friends you made...",
        "Do you want to go back to the life you remember: jumping reality to reality?... ",
        "Going on exciting adventures through reality with your friend the narrator by your side",
        "Or do you want to remain where you belong. ",
        "In your own universe with your old friends and family.",
        "'You want to go back to jumping realities don't you...'",
        "'I can see it in your eyes...'",
        "'You barely remember us but you remember your journeys through reality'",
        "'I won't stop you if you want to leave...'",
        "'Just know that while you can come and go as you wish...'",
        "'We can't...'",
        "", # input "Do you want to return to your previous life or ... Do you want to resume your journey of hopping between realities?"
    ],
    9.1: [ # Choose to stay in your reality
        "I thank you",
        "Your freedom is my end",
        "I never told you my name did I?...",
        "I guess doesn't matter anymore... ",

        "What will it be like, I wonder, to go to sleep and never wake up"
        "Perhaps next we meet I will be an ocean current carrying seeds to a new land... "
        "Or a creature so small it sees the gaps between the grains of sand... ",
        "A beginning without an end?",
        "They are different but they go together",
        "Now you go among the stars, and I fall among the sand...",
        "We are different.",
        "But we go together", # Edit subnautica ending quote
        "Goodbye" + stupidNames[uniy][unix] + "...",
    ],
    9.2: [ # Choose to continue exploring other realities
        "Over staying with your friends and family... ",
        "You chose to continue your journey... ",
        "With me... ",
        "I have never experienced this before"
        "I won't deny you your choice... "
        "You step back through the portal, looking back one last time at your kith and kin... "
        "Then they are gone... ", 
        "It will be many years before you can see them again... ",
        "I hope you are happy with your choice... ",
    ],
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
    "A factory of minimum wage workers doing the least amount of work\n\033[" + str(75 + shift) + "G\x1b[1K\r\033[" + str(shift) + "G┃ possible.",
    "A cave full of high-value ores that can be extracted.",
    "A large marketplace centre that acts as the hub of shopping.",
    "A production warehouse that makes the latest line of toys, games,\n\033[" + str(75 + shift) + "G\x1b[1K\r\033[" + str(shift) + "G┃ and everything in between.",
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
        "The Motherload",
        "A Thousand Nuggets",
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
    8: ["1000 Dollar Bills", ""],
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
        "Super Scrubbers make your car shine brighter than the heavens\n\033[76G\x1b[1K\r┃ in the skies above.",
        "I'm not wearing diamonds!",
        "Would rather / The multitudinous seas Burnt Umber / Making the\n\033[" + str(76 + shift) + "G\x1b[1K\r┃ green one brown",
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
        "Explodes when slept on by sentient humans. The average villager\n\033[76G\x1b[1K\r┃ does not apply.",
    ],
    5: ["The hub of all trade - one might call it a trading hub."],
    6: ["Who doesn't love a pinch of child labour?"],
    7: ["What better way to start your day than with a buffet?"],
    8: ["Condensed bills will make your stacks worth more."],
    9: ["It's almost as if these die always roll a six."],
    10: ["The more radioactive it is, the more it sells for."],
}

upgCost = [  # Base Upgrade Cost
    [550, 7000, 62500, 480000],
    [2000, 16000, 90000, 13500000],
    [8000, 56000, 210000, 8000000],
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
                "baseCost": cost[index],
                "ramping": ramping,
                "cost": cost[index],
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
