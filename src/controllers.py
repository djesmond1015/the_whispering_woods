import time
from datetime import datetime, timedelta


from settings import DEBUG
from adapters import GameStateAdapter
from utils import destructure as ds

gsa = GameStateAdapter()


class GameStateController:
    def __init__(self):
        self.data = gsa.load_game_state() if gsa else None
        # print(self.data)
        # time.sleep(5)
        # lambda x: x["scene_names"][-1] != WIN_SCENE
        # [{'player_id': 'eae476', 'player_name': 'sddfdfgdf', 'scene_names': ['enter forest', 'fireflies', 'ignore melody', 'ignore boat', 'exit', 'Escape woods'], 'start_game': datetime.datetime(2024, 1, 7, 21, 35, 6, 129931), 'updated_game': datetime.datetime(2024, 1, 7, 21, 44, 23, 103227), 'time_taken': '00:00:00'}, {'player_id': 'dfea1e', 'player_name': 'q', 'scene_names': [], 'start_game': datetime.datetime(2024, 1, 8, 9, 36, 51, 530456), 'updated_game': datetime.datetime(2024, 1, 8, 9, 36, 51, 530456), 'time_taken': '00:00:00'}]

    # Private methods
    def _handle_exception(self, error_flag: str, e: Exception, message: str = None):
        print(f'[{error_flag}] - {message or 'Something went wrong'}')
        print(e)

    # Handling multiple data
    def retrieve_multiple_data(self, condition=None, limit=False):
        try:
            if limit:
                limited_result = gsa.find(self.data, limit=limit)
                return limited_result
            elif condition:
                result = gsa.find(self.data, limit, condition=condition)
                return result
            else:
                return self.data
            
        except Exception as e:
            self._handle_exception("RETRIEVE_MULTIPLE_ERROR", e)

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
                'latest_load_time': None,
                "updated_game": initial_time,
                "time_taken": "00:00:00",
            }

            self.data.append(player)
            gsa.save_game_state(self.data)
        except Exception as e:
            self._handle_exception("CREATE_USER_ERROR", e)

    def update_data(self, unique_id, player_name, scene, is_load_game = False):
        try:
            if not unique_id or not player_name:
                raise Exception("[UPDATE_USER] - Invalid input")

            if DEBUG:
                print("finding data passed")

            latest_load_time = None
            
            if is_load_game:
                latest_load_time = datetime.now()
                
            
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
            
            time_taken_dict = {
                        'old_time': result["updated_game"],
                        'latest_time': latest_game,
                        'load_time': latest_load_time or result['latest_load_time'],
                        'time_taken': result["time_taken"]
                    }
                
            updated_player = {
                **result,
                "scene_names": [*result["scene_names"], scene["name"]],
                "updated_game": latest_game,
                'latest_load_time': latest_load_time or result['latest_load_time'],
                "time_taken": self.calculate_time_taken(
                    # result["updated_game"], latest_game, result["time_taken"]
                    time_taken_dict
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
    def calculate_time_taken(self, time_taken_dict):
        old_time, latest_time, load_time, time_taken = ds(
            time_taken_dict, 'old_time', 'latest_time', 'load_time', 'time_taken'
        )

        hours, minutes, seconds = map(int, time_taken.split(":"))
        previous_time_line_time_delta = timedelta(
            hours=hours, minutes=minutes, seconds=seconds
        )

        time_difference = latest_time - old_time

        if load_time:
            time_difference = latest_time - load_time
        else:
            time_difference = latest_time - old_time

        time_lapsed = time_difference + previous_time_line_time_delta

        new_hours = time_lapsed.seconds // 3600
        new_minutes = (time_lapsed.seconds % 3600) // 60
        new_seconds = time_lapsed.seconds % 60

        formatted_time = f"{new_hours:02}:{new_minutes:02}:{new_seconds:02}"

        return formatted_time




