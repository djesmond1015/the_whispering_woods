from configurations import handle_config, handle_config_dev

from app import AdventureGameEngine


def main():
    app = AdventureGameEngine()
    app.start_game_engine()


if __name__ == "__main__":
    handle_config()
    handle_config_dev()
    main()
