# This is the module handle configurations of the application.
# It takes variables from settings.py and executes the functions in configurations.py to alter the behaviour of the application.

import settings


def handle_config():
    if settings.INITIALIZE_GAME_STATE:
        from adapters import GameStateAdapter

        GameStateAdapter().initialize_game_state()
        print("Game state initialized")

        initial_game_state = GameStateAdapter().load_game_state()
        print(initial_game_state)
        print("Game state loaded")

    if settings.DELETE_PLAYER_GAME_STATE:
        from adapters import GameStateAdapter

        GameStateAdapter().delete_game_state()
        print("Game state file deleted")


def handle_config_dev():
    if settings.ENABLE_EXPORT:
        if settings.EXPORT_GAME_STATE:
            from controllers import GameStateController
            from export import Exporter

            file_format = settings.EXPORT_GAME_STATE[0]
            data = GameStateController().retrieve_multiple_data()

            Exporter().export_data(data, "theWhisperingWoods_game_state", file_format)

        if settings.EXPORT_GAME_DATASET:
            from dataset import scenes
            from export import Exporter

            file_format = settings.EXPORT_GAME_DATASET[0]
            data = scenes

            Exporter().export_data(data, "theWhisperingWoods_dataset", file_format)
    else:
        print("Export is disabled")
