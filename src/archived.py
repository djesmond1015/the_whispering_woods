import pickle

from pathlib import Path
import datetime, os


class GameState:
    def __init__(self, player, scene, path_name=None):
        self.player = player
        self.current_scene = scene
        self.directory = self.create_directory(path_name)
        self.initial_time = datetime.now()
        self.final_time = None

    def create_directory(self, path):
        pwd = os.getcwd()
        path = Path(pwd + f"/{path}")
        path.mkdir(parents=True, exist_ok=True)
        return path

    def get_file_path(self):
        return (
            self.directory
            / f"{self.player.name}_{self.player.unique_id}_game_state.pkl"
        )

    def save_game_state(self):
        with open(self.get_file_path(), "wb") as file:
            pickle.dump(self, file)

    def load_game_state(self):
        with open(self.get_file_path(), "rb") as file:
            return pickle.load(file)

    def delete_game_state(self):
        os.remove(self.get_file_path())

    def calculate_time_taken(self):
        self.final_time = datetime.now()

        time_lapsed = self.final_time - self.initial_time
        total_seconds = time_lapsed.total_seconds()

        hours = int(total_seconds // 3600)  # 3600 seconds in 1 hour
        minutes = int((total_seconds % 3600) // 60)  # 60 seconds in 1 minute
        seconds = int(total_seconds % 60)  # 60 seconds in 1 minute

        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def process_to_dictionary(self):
        self.load_game_state()

        player_dic = self.player.__dict__
        scene_dic = self.current_scene

        return {
            "player_id": player_dic["unique_id"],
            "player_name": player_dic["name"],
            "scene_name": scene_dic["name"],
            "start_game": self.initial_time,
            "time_taken": self.calculate_time_taken(),
        }


class TemporaryGameState(GameState):
    def __init__(self, player, state):
        path_name = "temporary_state"
        super().__init__(player, state, path_name)


class PermanentGameState(GameState):
    def __init__(self, player, state):
        path_name = "permanent_state"
        super().__init__(player, state, path_name)


def calculate_time_taken(self, old_time, latest_time):
    time_lapsed = latest_time - old_time
    total_seconds = time_lapsed.total_seconds()

    hours = int(total_seconds // 3600)  # 3600 seconds in 1 hour
    minutes = int((total_seconds % 3600) // 60)  # 60 seconds in 1 minute
    seconds = int(total_seconds % 60)  # 60 seconds in 1 minute

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
