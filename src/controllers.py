import datetime

from settings import DEBUG
from adapters import GameStateAdapter
from utils import ds

gsa = GameStateAdapter()


class GameStateController:
    def __init__(self):
        self.data = gsa.load_game_state() if gsa else None

    def _handle_exception(self, error_flag: str, e: Exception, message: str = None):
        print(f'[{error_flag}] - {message or 'Something went wrong'}')
        print(e)

    # Handling multiple data
    def retrieve_multiple_data(self, limit=False, condition=False):
        try:
            if limit:
                limited_result = gsa.find(self.data, limit=limit)
                return limited_result
            elif condition:
                result = gsa.find(self.data, condition=condition, limit=False)
                return result
            else:
                return self.data
            
        except Exception as e:
            self._handle_exception("RETRIEVE_ALL_ERROR", e)

    def reset_game(self):
        try:
            gsa.save_game_state([])
        except Exception as e:
            self._handle_exception("RESET_GAME_ERROR", e)

    def delete_file(self):
        try:
            gsa.delete_game_state()
        except Exception as e:
            self._handle_exception("DELETE_FILE_ERROR", e)
    # Handling single data
    def retrieve_data(self, unique_id, player_name):
        try:
            condition = (
                lambda x: x["player_id"] == unique_id
                and x["player_name"] == player_name
            )
            result = gsa.find(self.data, condition=condition, limit=1)
            return result
        except Exception as e:
            self._handle_exception("RETRIEVE_USER_ERROR", e)

    def create_data(self, player, initial_time):
        try:
            player_id, player_name = ds(player.__dict__, "unique_id", "name")

            player = {
                "player_id": player_id,
                "player_name": player_name,
                "scene_names": [],
                "start_game": initial_time,
                "updated_game": initial_time,
                "time_taken": "00:00:00",
            }

            self.data.append(player)
            gsa.save_game_state(self.data)
        except Exception as e:
            self._handle_exception("CREATE_USER_ERROR", e)

    def update_data(self, unique_id, player_name, scene):
        try:
            if not unique_id or not player_name:
                raise Exception("[UPDATE_USER] - Invalid input")

            if DEBUG:
                print("finding data passed")

            latest_game = datetime.now()

            condition = (
                lambda x: x["player_id"] == unique_id
                and x["player_name"] == player_name
            )

            result = gsa.find(
                self.data, condition=condition
            )  # return the player list with only player dictionary
            result = result[0]  # return the player dictionary

            if not result:
                raise Exception("[UPDATE_USER] - No data found")

            if DEBUG:
                print("finding result passed")

            # Remove the last scene name if it is the same as the current scene name
            if result["scene_names"]:
                if result["scene_names"][-1] == scene["name"]:
                    result["scene_names"].pop()

            updated_player = {
                **result,
                "scene_names": [*result["scene_names"], scene["name"]],
                "updated_game": latest_game,
                "time_taken": self.calculate_time_taken(
                    result["updated_game"], latest_game
                ),
            }

            if DEBUG:
                print("updating player passed")

            filtered_data = list(
                filter(
                    (
                        lambda x: x["player_id"] != unique_id
                        and x["player_name"] != player_name
                    ),
                    self.data,
                )
            )

            if DEBUG:
                print("filtering data passed")

            filtered_data.append(updated_player)

            if DEBUG:
                print("appending data passed")

            gsa.save_game_state(filtered_data)

        except Exception as e:
            self._handle_exception("UPDATE_USER_ERROR", e)
    def delete_all_load_games(self, player_list):
        try:
            filtered_data = list(
                filter(
                    lambda x: x["player_name"]
                    not in [player["player_name"] for player in player_list]
                    and x["player_id"]
                    not in [player["player_name"] for player in player_list],
                    self.data,
                )
            )

            self.reset_game()

            gsa.save_game_state(filtered_data)

        except Exception as e:
            self._handle_exception("DELETE_USER_ERROR", e)

    # Utility methods
    def calculate_time_taken(self, old_time, latest_time):
        time_lapsed = latest_time - old_time
        total_seconds = time_lapsed.total_seconds()

        hours = int(total_seconds // 3600)  # 3600 seconds in 1 hour
        minutes = int((total_seconds % 3600) // 60)  # 60 seconds in 1 minute
        seconds = int(total_seconds % 60)  # 60 seconds in 1 minute

        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"



