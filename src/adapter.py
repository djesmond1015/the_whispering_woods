import os, pickle
from datetime import datetime
from pathlib import Path


class GameStateAdapter:
    def __init__(self, path_name="state_manager"):
        self.PLAYER_LIST = []
        self.directory = self.create_directory(path_name)
        self.initial_time = datetime.now()
        self.final_time = None

    def create_directory(self, path):
        pwd = os.getcwd()
        path = Path(pwd + f"/{path}")
        path.mkdir(parents=True, exist_ok=True)
        return path

    def get_file_path(self):
        return self.directory / f"game_state.pkl"

    def initialize_game_state(self):
        self.save_game_state(self.PLAYER_LIST)

    def save_game_state(self, data):
        with open(self.get_file_path(), "wb") as file:
            pickle.dump(data, file)

    def load_game_state(self):
        with open(self.get_file_path(), "rb") as file:
            return pickle.load(file)

    def delete_game_state(self):
        os.remove(self.get_file_path())

    # Utility functions
    def find(self, iterable, default=None, condition=lambda x: True, limit=None):
        try:
            if limit == 1:
                return next(x for x in iterable if condition(x))
            elif limit is False:
                return [x for x in iterable if condition(x)]
            else:
                return [x for x in iterable if condition(x)][:limit]
        except StopIteration:
            if default is not None and condition(default):
                return default
            else:
                raise