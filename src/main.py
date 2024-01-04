# TODO: Do not to show save message if the user win the game


from app import AdventureGameEngine


def main():
    app = AdventureGameEngine()
    app.start_game_engine()


if __name__ == "__main__":
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
