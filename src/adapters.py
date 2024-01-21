# The adapter.py module is used to handle the game state persistance data.
# In our case we are using pickle module as external storage to save the game state data.
# With this module, we can save, load and delete the game state data.
# Besides that, this can make dependency injection easier in the future.


import os, pickle
from datetime import datetime
from pathlib import Path


class GameStateAdapter:
    def __init__(self, path_name="stateManager"):
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

    # The find function is used to find or filter the data from the list of data.
    # It handles 3 cases:
    # 1. Find only one item (find first)
    # 2. Find all items
    # 3. Find n items (limit)

    def find(self, iterable: list, default=None, condition=lambda x: True, limit=None):
        try:
            # Find only one item by using next() function which returns only the next item if the condition is met.
            if limit == 1:
                return next(x for x in iterable if condition(x))
            # Find all items
            elif limit is False:
                return [x for x in iterable if condition(x)]
            # Find n items
            else:
                return [x for x in iterable if condition(x)][:limit]

        # This is the trick to handle the find first case if the condition is not met.
        except StopIteration:
            # Return default value if condition is not met
            if default is not None and condition(default):
                return default
            # Raise error if default value is not provided
            else:
                raise

        except Exception as e:
            print(f"[ADAPTER_FIND_ERROR] - Something went wrong", e)
            return
