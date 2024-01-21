# This is the game settings file.
# This file is used to configure the game settings.
# This is handle when the game is in development mode.
# The variables in this file will be used in the application through the execution of the functions in configurations.py.


# The main settings of the application.

INITIALIZE_GAME_STATE = False

DELETE_PLAYER_GAME_STATE = False

DEBUG = False


# Export data - game state and dataset
# Supported file formats: json, txt
# Note: this is used for development only

ENABLE_EXPORT = False

EXPORT_GAME_STATE = ["json", "txt"]

EXPORT_GAME_DATASET = ["json", "txt"]


# Any URL related to the application (e.g. github repo, documentation, etc.)

SOURCE_CODE_URL = "https://github.com/djesmond1015/text_adventure_game_sp"
