# TODO: Do not to show save message if the user win the game
import config

from app import AdventureGameEngine


def main():
    app = AdventureGameEngine()
    app.start_game_engine()


if __name__ == "__main__":
    if config.INITIALIZE_GAME_STATE:
        from app import GameStateAdapter

        GameStateAdapter().initialize_game_state()
        print("Game state initialized")

        initial_game_state = GameStateAdapter().load_game_state()
        print(initial_game_state)
        print("Game state loaded")

    if config.DELETE_PLAYER_GAME_STATE:
        from app import GameStateAdapter

        GameStateAdapter().delete_game_state()
        print("Game state file deleted")

    main()


# Save and load game feature in high level explanation:

# The user can have many player name for the game
# The game is saved automatically when the user choose to quit and return to the menu
# User can resume the game by enter the command "load game" in the menu
# A list of saved games will be displayed, allowing the user to choose which game to resume


# Once the user win the game, the time taken to complete the game, and the number of scenes the user has been through for each completed game will be recorded in a permanent file. The game state will be reset, the saved game file will be deleted.

# In the permanent file, the user can view all:
# the time taken to complete the game for each completed game
# the number of scenes the user has been through for each completed game
# the shortest time taken to complete the game
# the longest time taken to complete the game
# the average time taken to complete the game
# the numbers of times the user has won the game
# the highest number of scenes the user has been through
# the lowest number of scenes the user has been through


# ------------------------------------

# Configuration
# disable key down event the print function is running


# Display menu:
# 1. Start Game
# 2. Load Game
# 3. Statistics
# 4. Exit

# 2. Load Game
# Display list of saved games
# Show player name with unique id
# Show the scene name
# Show the time he left the game based on the system time
# Show the time he has been through the game
# Display the return to menu option [Q]
# User choose which game to load [1, 2, 3, n]
# Game state will be loaded

# Calculate time taken to complete the game
# system time

# How to get the time


{
    "player": {"name": "dafsdsa", "unique_id": "62678c"},
    "scene": {
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
        "choice": {"1": "echoing whispers", "2": "fireflies", "3": "climb hill"},
        "continue": (False, None),
    },
}


load_game_menu = {
    "player_list": [
        {
            "player_id": 1,
            "player_name": "John",
            "scene_name": "enter forest",
            "start_game": "2020-12-12 12:12:12",
            "time_taken": "00:00:00",
        },
        {
            "player_id": 2,
            "player_name": "Mary",
            "scene_name": "enter forest",
            "start_game": "2020-12-12 12:12:12",
            "time_taken": "00:00:00",
        },
    ],
    "exit": "[Q] - Return to menu",
}


# Game state save and load flow:
# hit the save_game function - extract the data (player_id, player_name, scene_name, start_game, time_taken)
# save the data into a file using pickle
# user return to menu
# user choose load game
# this trigger the process_game_menu function that show up the screen - get player_list pickle file
# user choose the game that he want to load by entering the number
# this trigger load_game function - get player_list from Game State class


# 3. Statistics
