import settings


def handle_config():
    if settings.INITIALIZE_GAME_STATE:
        from app import GameStateAdapter

        GameStateAdapter().initialize_game_state()
        print("Game state initialized")

        initial_game_state = GameStateAdapter().load_game_state()
        print(initial_game_state)
        print("Game state loaded")

    if settings.DELETE_PLAYER_GAME_STATE:
        from app import GameStateAdapter

        GameStateAdapter().delete_game_state()
        print("Game state file deleted")
