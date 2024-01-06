display_menu = [
    "\t\tText Adventure Game",
    "\n",
    "\t\t1. Start Game",
    "\t\t2. Load Game",
    "\t\t3. Statistics",
    "\t\t4. Exit",
    "\n",
]

WIN_SCENE = "Escape woods"

# TODO: Turning scene dictionary into a class in the future
# scenes = {
#     "enter forest": {
#         "name": "enter forest",
#         "text": [
#             "You enter forest",
#             "Hear echoing whispers",
#             "See glimmering fireflies",
#             "Choose the path you want to continue: ",
#             "[1] - Follow echoing whispers",
#             "[2] - Follow glimmering fireflies",
#             "[3] - Climb up the hill",
#         ],
#         "choice": {
#             "1": "echoing whispers",
#             "2": "fireflies",
#             "3": "climb hill",
#         },
#         "continue": (False, None),
#     },
#     "echoing whispers": {
#         "name": "follow echoing whispers",
#         "text": [
#             "You follow the echoing whispers",
#             "Discover ancient marker",
#         ],
#         "choice": {},
#         "continue": (False, None),
#     },
#     "fireflies": {
#         "name": "fireflies",
#         "text": [
#             "You follow the glimmering fireflies",
#             "You see a lot of gold",
#             "Choose the path you want to continue: ",
#             "[1] - Ignore melody",
#             "[2] - Follow melody",
#         ],
#         "choice": {
#             "1": "ignore melody",
#             "2": "follow melody",
#         },
#         "continue": (False, None),
#     },
#     "climb hill": {
#         "name": "climb hill",
#         "text": ["You climb up the hill"],
#         "choice": {},
#         "continue": (False, None),
#     },
#     "follow melody": {
#         "name": "follow melody",
#         "text": ["You follow the melody"],
#         "choice": {},
#         "continue": (False, None),
#     },
#     "ignore melody": {
#         "name": "ignore melody",
#         "text": [
#             "You ignore the melody",
#             "You see a boat",
#             "Choose the path you want to continue: ",
#             "[1] - Take the boat",
#             "[2] - Ignore the boat",
#         ],
#         "choice": {
#             "1": "take boat",
#             "2": "ignore boat",
#         },
#         "continue": (False, None),
#     },
#     "take boat": {
#         "name": "take boat",
#         "text": [
#             "You take the boat",
#         ],
#         "choice": {},
#         "continue": (False, None),
#     },
#     "ignore boat": {
#         "name": "ignore boat",
#         "text": [
#             "You ignore the boat",
#         ],
#         "choice": {},
#         "continue": (True, "exit"),
#     },
#     "exit": {
#         "name": "exit",
#         "text": ["You exit"],
#         "choice": {},
#         "continue": (False, None),
#     },
# }

scenes = {
    "enter forest": {
        "name": "enter forest",
        "text": [
            "Enter forest sentence 1",
            "Enter forest sentence 2",
            "Enter forest sentence 3",
        ],
        "choice": {},
        "continue": (True, "echoing whispers and glimmering fireflies"),
    },
    "echoing whispers and glimmering fireflies": {
        "name": "echoing whispers and glimmering fireflies",
        "text": [
            "Echoing whispers and glimmering fireflies sentence 1",
            "Echoing whispers and glimmering fireflies sentence 2",
            "Echoing whispers and glimmering fireflies sentence 3",
            "[1] - Follow echoing whispers",
            "[2] - Follow glimmering fireflies",
            "[3] - Climb up the hill",
        ],
        "choice": {
            "1": "follow echoing whispers",
            "2": "follow glimmering fireflies",
            "3": "climb hill",
        },
        "continue": (False, None),
    },
    "follow echoing whispers": {
        "name": "follow echoing whispers",
        "text": [
            "Follow echoing whispers sentence 1",
            "Follow echoing whispers sentence 2",
            "Follow echoing whispers sentence 3",
        ],
        "choice": {},
        "continue": (True, "discover ancient marker"),
    },
    "follow glimmering fireflies": {
        "name": "follow glimmering fireflies",
        "text": [
            "Follow glimmering fireflies sentence 1",
            "Follow glimmering fireflies sentence 2",
            "Follow glimmering fireflies sentence 3",
        ],
        "choice": {},
        "continue": (True, "descend into darkness"),
    },
    "climb hill": {
        "name": "climb hill",
        "text": [
            "Ignore all, climb hill sentence 1",
            "Ignore all, climb hill sentence 2",
            "Ignore all, climb hill sentence 3",
        ],
        "choice": {},
        "continue": (True, "discover hidden altar"),
    },
    "discover ancient marker": {
        "name": "discover ancient marker",
        "text": [
            "Discover ancient marker sentence 1",
            "Discover ancient marker sentence 2",
            "Discover ancient marker sentence 3",
        ],
        "choice": {},
        "continue": (True, "traverse though bushes"),
    },
    "traverse through bushes": {
        "name": "traverse though bushes",
        "text": [
            "Traverse though bushes sentence 1",
            "Traverse though bushes sentence 2",
            "Traverse though bushes sentence 3",
        ],
        "choice": {},
        "continue": (True, "hear rustling in nearby foliage"),
    },
    "descend into darkness": {
        "name": "descend into darkness",
        "text": [
            "Descend into darkness sentence 1",
            "Descend into darkness sentence 2",
            "Descend into darkness sentence 3",
        ],
        "choice": {},
        "continue": (True, "hear rustling in nearby foliage"),
    },
    "hear rustling in nearby foliage": {
        "name": "hear rustling in nearby foliage",
        "text": [
            "Hear rustling in nearby foliage sentence 1",
            "Hear rustling in nearby foliage sentence 2",
            "Hear rustling in nearby foliage sentence 3",
        ],
        "choice": {},
        "continue": (True, "discover overgrown trail"),
    },
    "discover overgrown trail": {
        "name": "discover overgrown trail",
        "text": [
            "Discover overgrown trail sentence 1",
            "Discover overgrown trail sentence 2",
            "Discover overgrown trail sentence 3",
        ],
        "choice": {},
        "continue": (True, "uncover old map"),
    },
    "uncover old map": {
        "name": "uncover old map",
        "text": [
            "Uncover old map sentence 1",
            "Uncover old map sentence 2",
            "Uncover old map sentence 3",
        ],
        "choice": {},
        "continue": (True, "hear a distant melody"),
    },
    "discover hidden altar": {
        "name": "discover hidden altar",
        "text": [
            "Discover hidden altar sentence 1",
            "Discover hidden altar sentence 2",
            "Discover hidden altar sentence 3",
        ],
        "choice": {},
        "continue": (True, "solve altar puzzle"),
    },
    "solve altar puzzle": {
        "name": "solve altar puzzle",
        "text": [
            "Solve altar puzzle sentence 1",
            "Solve altar puzzle sentence 2",
            "Solve altar puzzle sentence 3",
        ],
        "choice": {},
        "continue": (True, "unlock secret passage"),
    },
    "unlock secret passage": {
        "name": "unlock secret passage",
        "text": [
            "Unlock secret passage sentence 1",
            "Unlock secret passage sentence 2",
            "Unlock secret passage sentence 3",
        ],
        "choice": {},
        "continue": (True, "encounter ancient guardian"),
    },
    "encounter ancient guardian": {
        "name": "encounter ancient guardian",
        "text": [
            "Encounter ancient guardian sentence 1",
            "Encounter ancient guardian sentence 2",
            "Encounter ancient guardian sentence 3",
        ],
        "choice": {},
        "continue": (True, "escape from Guardian's lair"),
    },
    "escape from Guardian's lair": {
        "name": "escape from Guardian's lair",
        "text": [
            "Escape from Guardian's lair sentence 1",
            "Escape from Guardian's lair sentence 2",
            "Escape from Guardian's lair sentence 3",
        ],
        "choice": {},
        "continue": (True, "find abandoned path"),
    },
    "hear a distant melody": {
        "name": "hear a distant melody",
        "text": [
            "Hear a distant melody sentence 1",
            "Hear a distant melody sentence 2",
            "Hear a distant melody sentence 3",
            "[1] - Ignore melody",
            "[2] - Follow melody",
        ],
        "choice": {
            "1": "ignore melody",
            "2": "follow melody",
        },
        "continue": (False, None),
    },
    "ignore melody": {
        "name": "ignore melody",
        "text": [
            "Ignore melody sentence 1",
            "Ignore melody sentence 2",
            "Ignore melody sentence 3",
        ],
        "choice": {},
        "continue": (True, "find abandoned path"),
    },
    "follow melody": {
        "name": "follow melody",
        "text": [
            "Follow melody sentence 1",
            "Follow melody sentence 2",
            "Follow melody sentence 3",
        ],
        "choice": {},
        "continue": (True, "discover abandoned path"),
    },
    "find abandoned path": {
        "name": "find abandoned path",
        "text": [
            "Find abandoned path sentence 1",
            "Find abandoned path sentence 2",
            "Find abandoned path sentence 3",
        ],
        "choice": {},
        "continue": (True, "spot glowing object with peculiar markings"),
    },
    "spot glowing object with peculiar markings": {
        "name": "spot glowing object with peculiar markings",
        "text": [
            "Spot glowing object with peculiar markings sentence 1",
            "Spot glowing object with peculiar markings sentence 2",
            "Spot glowing object with peculiar markings sentence 3",
            "[1] - Ignore object",
            "[2] - Check out object",
        ],
        "choice": {
            "1": "ignore object",
            "2": "check out object",
        },
        "continue": (False, None),
    },
    "ignore object": {
        "name": "ignore object",
        "text": [
            "Ignore object sentence 1",
            "Ignore object sentence 2",
            "Ignore object sentence 3",
        ],
        "choice": {},
        "continue": (True, "follow faint trail"),
    },
    "follow faint trail": {
        "name": "follow faint trail",
        "text": [
            "Follow faint trail sentence 1",
            "Follow faint trail sentence 2",
            "Follow faint trail sentence 3",
        ],
        "choice": {},
        "continue": (True, "reach hidden cave with split paths"),
    },
    "reach hidden cave with split paths": {
        "name": "reach hidden cave with split paths",
        "text": [
            "Reach hidden cave with split paths sentence 1",
            "Reach hidden cave with split paths sentence 2",
            "Reach hidden cave with split paths sentence 3",
            "[1] - Follow along left path",
            "[2] - Follow along right path",
        ],
        "choice": {
            "1": "follow along left path",
            "2": "follow along right path",
        },
        "continue": (False, None),
    },
    "check out object": {
        "name": "check out object",
        "text": [
            "Check out object sentence 1",
            "Check out object sentence 2",
            "Check out object sentence 3",
        ],
        "choice": {},
        "continue": (True, "sucked into vortex"),
    },
    "sucked into vortex": {
        "name": "sucked into vortex",
        "text": [
            "Sucked into vortex sentence 1",
            "Sucked into vortex sentence 2",
            "Sucked into vortex sentence 3",
        ],
        "choice": {},
        "continue": (True, "reach magical grove"),
    },
    "reach magical grove": {
        "name": "reach magical grove",
        "text": [
            "Reach magical grove sentence 1",
            "Reach magical grove sentence 2",
            "Reach magical grove sentence 3",
        ],
        "choice": {},
        "continue": (True, "path ahead blocked by ancient trees"),
    },
    "path ahead blocked by ancient trees": {
        "name": "path ahead blocked by ancient trees",
        "text": [
            "Path ahead blocked by ancient trees sentence 1",
            "Path ahead blocked by ancient trees sentence 2",
            "Path ahead blocked by ancient trees sentence 3",
            '[1] - "Continue ahead"',
            '[2] - "Try to find a way out"',
        ],
        "choice": {"1": "continue ahead", "2": "try to find a way out"},
        "continue": (False, None),
    },
    "continue ahead": {
        "name": "continue ahead",
        "text": [
            "Continue ahead sentence 1",
            "Continue ahead sentence 2",
            "Continue ahead sentence 3",
        ],
        "choice": {},
        "continue": (True, "decipher order of words trees are whispering"),
    },
    "decipher order of words trees are whispering": {
        "name": "decipher order of words trees are whispering",
        "text": [
            "Decipher order of words trees are whispering sentence 1",
            "Decipher order of words trees are whispering sentence 2",
            "Decipher order of words trees are whispering sentence 3",
        ],
        "choice": {},
        "continue": (True, "tress part"),
    },
    "tress part": {
        "name": "tress part",
        "text": [
            "Tress part sentence 1",
            "Tress part sentence 2",
            "Tress part sentence 3",
        ],
        "choice": {},
        "continue": (True, "find a small pathway"),
    },
    "try to find a way out": {
        "name": "try to find a way out",
        "text": [
            "Try to find a way out sentence 1",
            "Try to find a way out sentence 2",
            "Try to find a way out sentence 3",
        ],
        "choice": {},
        "continue": (True, "find a small pathway"),
    },
    "find a small pathway": {
        "name": "find a small pathway",
        "text": [
            "Find a small pathway sentence 1",
            "Find a small pathway sentence 2",
            "Find a small pathway sentence 3",
        ],
        "choice": {},
        "continue": (True, "path blocked by Celestial guardian"),
    },
    "path blocked by Celestial guardian": {
        "name": "path blocked by Celestial guardian",
        "text": [
            "Path blocked by Celestial guardian sentence 1",
            "Path blocked by Celestial guardian sentence 2",
            "Path blocked by Celestial guardian sentence 3",
        ],
        "choice": {},
        "continue": (True, "answer riddle given by Guardian"),
    },
    "answer riddle given by Guardian": {
        "name": "answer riddle given by Guardian",
        "text": [
            "Answer riddle given by Guardian sentence 1",
            "Answer riddle given by Guardian sentence 2",
            "Answer riddle given by Guardian sentence 3",
        ],
        "choice": {},
        "continue": (True, "glowing vertex reappears"),
    },
    "glowing vertex reappears": {
        "name": "glowing vertex reappears",
        "text": [
            "Glowing vertex reappears sentence 1",
            "Glowing vertex reappears sentence 2",
            "Glowing vertex reappears sentence 3",
        ],
        "choice": {},
        "continue": (True, "reach hidden cave with split paths"),
    },
    "follow along left path": {
        "name": "follow along left path",
        "text": [
            "Follow along left path sentence 1",
            "Follow along left path sentence 2",
            "Follow along left path sentence 3",
        ],
        "choice": {},
        "continue": (True, "discover ancient monument"),
    },
    "discover ancient monument": {
        "name": "discover ancient monument",
        "text": [
            "Discover ancient monument sentence 1",
            "Discover ancient monument sentence 2",
            "Discover ancient monument sentence 3",
            "[1] - Check out monument",
            "[2] - Ignore monument",
        ],
        "choice": {"1": "check out monument", "2": "ignore monument"},
        "continue": (False, None),
    },
    "follow along right path": {
        "name": "follow along right path",
        "text": [
            "Follow along right path sentence 1",
            "Follow along right path sentence 2",
            "Follow along right path sentence 3",
        ],
        "choice": {},
        "continue": (True, "reach end of cave"),
    },
    "ignore monument": {
        "name": "ignore monument",
        "text": [
            "Ignore monument sentence 1",
            "Ignore monument sentence 2",
            "Ignore monument sentence 3",
        ],
        "choice": {},
        "continue": (True, "reach end of cave"),
    },
    "reach end of cave": {
        "name": "reach end of cave",
        "text": [
            "Reach end of cave sentence 1",
            "Reach end of cave sentence 2",
            "Reach end of cave sentence 3",
        ],
        "choice": {},
        "continue": (True, "find a boat"),
    },
    "find a boat": {
        "name": "find a boat",
        "text": [
            "Find a boat sentence 1",
            "Find a boat sentence 2",
            "Find a boat sentence 3",
        ],
        "choice": {},
        "continue": (True, "solve a puzzle"),
    },
    "solve a puzzle": {
        "name": "solve a puzzle",
        "text": [
            "Solve a puzzle sentence 1",
            "Solve a puzzle sentence 2",
            "Solve a puzzle sentence 3",
        ],
        "choice": {},
        "continue": (True, "boat engine starts"),
    },
    "boat engine starts": {
        "name": "boat engine starts",
        "text": [
            "Boat engine starts sentence 1",
            "Boat engine starts sentence 2",
            "Boat engine starts sentence 3",
        ],
        "choice": {},
        "continue": (True, "cross the river"),
    },
    "check out monument": {
        "name": "check out monument",
        "text": [
            "Check out monument sentence 1",
            "Check out monument sentence 2",
            "Check out monument sentence 3",
        ],
        "choice": {},
        "continue": (True, "encounter mysterious mist"),
    },
    "encounter mysterious mist": {
        "name": "encounter mysterious mist",
        "text": [
            "Encounter mysterious mist sentence 1",
            "Encounter mysterious mist sentence 2",
            "Encounter mysterious mist sentence 3",
        ],
        "choice": {"1": "try to turn back", "2": "go through the mist"},
        "continue": (False, None),
    },
    "try to turn back": {
        "name": "try to turn back",
        "text": [
            "Try to turn back sentence 1",
            "Try to turn back sentence 2",
            "Try to turn back sentence 3",
        ],
        "choice": {},
        "continue": (True, "stumble upon hidden path"),
    },
    "stumble upon hidden path": {
        "name": "stumble upon hidden path",
        "text": [
            "Stumble upon hidden path sentence 1",
            "Stumble upon hidden path sentence 2",
            "Stumble upon hidden path sentence 3",
        ],
        "choice": {},
        "continue": (True, "discover cryptic note"),
    },
    "discover cryptic note": {
        "name": "discover cryptic note",
        "text": [
            "Discover cryptic note sentence 1",
            "Discover cryptic note sentence 2",
            "Discover cryptic note sentence 3",
        ],
        "choice": {},
        "continue": (True, "encounter old cabin"),
    },
    "go through the mist": {
        "name": "go through the mist",
        "text": [
            "Go through the mist sentence 1",
            "Go through the mist sentence 2",
            "Go through the mist sentence 3",
        ],
        "choice": {},
        "continue": (True, "stumble upon enchanted glade"),
    },
    "stumble upon enchanted glade": {
        "name": "stumble upon enchanted glade",
        "text": [
            "Stumble upon enchanted glade sentence 1",
            "Stumble upon enchanted glade sentence 2",
            "Stumble upon enchanted glade sentence 3",
        ],
        "choice": {},
        "continue": (True, "meet fairy"),
    },
    "meet fairy": {
        "name": "meet fairy",
        "text": [
            "Meet fairy sentence 1",
            "Meet fairy sentence 2",
            "Meet fairy sentence 3",
            "[1] - Ignore fairy, continue walking",
            "[2] - Interact with fairy",
        ],
        "choice": {"1": "ignore fairy, continue walking", "2": "interact with fairy"},
        "continue": (False, None),
    },
    "ignore fairy, continue walking": {
        "name": "ignore fairy, continue walking",
        "text": [
            "Ignore fairy, continue walking sentence 1",
            "Ignore fairy, continue walking sentence 2",
            "Ignore fairy, continue walking sentence 3",
        ],
        "choice": {},
        "continue": (True, "encounter old cabin"),
    },
    "encounter old cabin": {
        "name": "encounter old cabin",
        "text": [
            "Encounter old cabin sentence 1",
            "Encounter old cabin sentence 2",
            "Encounter old cabin sentence 3",
        ],
        "choice": {},
        "continue": (True, "investigate old cabin"),
    },
    "investigate old cabin": {
        "name": "investigate old cabin",
        "text": [
            "Investigate old cabin sentence 1",
            "Investigate old cabin sentence 2",
            "Investigate old cabin sentence 3",
        ],
        "choice": {},
        "continue": (True, "find distress flare"),
    },
    "find distress flare": {
        "name": "find distress flare",
        "text": [
            "Find distress flare sentence 1",
            "Find distress flare sentence 2",
            "Find distress flare sentence 3",
        ],
        "choice": {},
        "continue": (True, "meet rescue team"),
    },
    "meet rescue team": {
        "name": "meet rescue team",
        "text": [
            "Meet rescue team sentence 1",
            "Meet rescue team sentence 2",
            "Meet rescue team sentence 3",
        ],
        "choice": {},
        "continue": (False, None),
    },
    "interact with fairy": {
        "name": "interact with fairy",
        "text": [
            "Interact with fairy sentence 1",
            "Interact with fairy sentence 2",
            "Interact with fairy sentence 3",
        ],
        "choice": {},
        "continue": (True, "journey to ancient ruin"),
    },
    "journey to ancient ruin": {
        "name": "journey to ancient ruin",
        "text": [
            "Journey to ancient ruin sentence 1",
            "Journey to ancient ruin sentence 2",
            "Journey to ancient ruin sentence 3",
        ],
        "choice": {},
        "continue": (True, "uncover ancient artifact"),
    },
    "uncover ancient artifact": {
        "name": "uncover ancient artifact",
        "text": [
            "Uncover ancient artifact sentence 1",
            "Uncover ancient artifact sentence 2",
            "Uncover ancient artifact sentence 3",
        ],
        "choice": {},
        "continue": (True, "decrypt ancient language"),
    },
    "decrypt ancient language": {
        "name": "decrypt ancient language",
        "text": [
            "Decrypt ancient language sentence 1",
            "Decrypt ancient language sentence 2",
            "Decrypt ancient language sentence 3",
        ],
        "choice": {},
        "continue": (True, "decode symbols for clues"),
    },
    "decode symbols for clues": {
        "name": "decode symbols for clues",
        "text": [
            "Decode symbols for clues sentence 1",
            "Decode symbols for clues sentence 2",
            "Decode symbols for clues sentence 3",
        ],
        "choice": {},
        "continue": (True, "discover a hidden bridge"),
    },
    "discover a hidden bridge": {
        "name": "discover a hidden bridge",
        "text": [
            "Discover a hidden bridge sentence 1",
            "Discover a hidden bridge sentence 2",
            "Discover a hidden bridge sentence 3",
        ],
        "choice": {},
        "continue": (True, "cross the river"),
    },
    "cross the river": {
        "name": "cross the river",
        "text": [
            "Cross the river sentence 1",
            "Cross the river sentence 2",
            "Cross the river sentence 3",
        ],
        "choice": {},
        "continue": (False, None),
    },
}
