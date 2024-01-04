display_menu = [
    "\t\tText Adventure Game",
    "\n",
    "\t\t1. Start Game",
    "\t\t2. Load Game",
    "\t\t3. Exit",
    "\n",
]

scenes = {
    "enter forest": {
        "name": "enter forest",
        "text": [
            "You enter forest",
            "Hear echoing whispers",
            "See glimmering fireflies",
            "Choose the path you want to continue: ",
            "[1] - Follow echoing whispers",
            "[2] - Follow glimmering fireflies",
            "[3] - Climb up the hill",
        ],
        "choice": {
            "1": "echoing whispers",
            "2": "fireflies",
            "3": "climb hill",
        },
        "continue": (False, None),
    },
    "echoing whispers": {
        "name": "follow echoing whispers",
        "text": [
            "You follow the echoing whispers",
            "Discover ancient marker",
        ],
        "choice": {},
        "continue": (False, None),
    },
    "fireflies": {
        "name": "fireflies",
        "text": [
            "You follow the glimmering fireflies",
            "You see a lot of gold",
            "Choose the path you want to continue: ",
            "[1] - Ignore melody",
            "[2] - Follow melody",
        ],
        "choice": {
            "1": "ignore melody",
            "2": "follow melody",
        },
        "continue": (False, None),
    },
    "climb hill": {
        "name": "climb hill",
        "text": ["You climb up the hill"],
        "choice": {},
        "continue": (False, None),
    },
    "follow melody": {
        "name": "follow melody",
        "text": ["You follow the melody"],
        "choice": {},
        "continue": (False, None),
    },
    "ignore melody": {
        "name": "ignore melody",
        "text": [
            "You ignore the melody",
            "You see a boat",
            "Choose the path you want to continue: ",
            "[1] - Take the boat",
            "[2] - Ignore the boat",
        ],
        "choice": {
            "1": "take boat",
            "2": "ignore boat",
        },
        "continue": (False, None),
    },
    "take boat": {
        "name": "take boat",
        "text": [
            "You take the boat",
        ],
        "choice": {},
        "continue": (False, None),
    },
    "ignore boat": {
        "name": "ignore boat",
        "text": [
            "You ignore the boat",
        ],
        "choice": {},
        "continue": (True, "exit"),
    },
    "exit": {
        "name": "exit",
        "text": ["You exit"],
        "choice": {},
        "continue": (False, None),
    },
}
