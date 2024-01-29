# This is the module that handles the save and load game feature.
# In our case, the game state controller is used to as the immediate layer to handle the game state data between the game engine (use cases layer) and the game state persistance wrapper (adapter).

import time
from datetime import datetime, timedelta


from settings import DEBUG
from adapters import GameStateAdapter
from utils import destructure as ds

# Initialize the game state adapter
gsa = GameStateAdapter()


class GameStateController:
    def __init__(self):
        # Load the game state data from the file for further processing.
        self.data = gsa.load_game_state() if gsa else None
   
    # Utility methods
    
    # Private methods
    # Since this is the place where our application communicates with the external resources, we need to handle the exceptions wisely.
    # Handle exceptions without repeating the same code and keep consistency.
    def _handle_exception(self, error_flag: str, e: Exception, message: str = None):
        print(f'[{error_flag}] - {message or 'Something went wrong'}')
        print(e)

    def calculate_time_taken(self, time_taken_dict: dict) -> str:
        # Convert the string to datetime object to calculate the time difference, then convert it back to formatted time string.

        old_time, latest_time, load_time, time_taken = ds(
            time_taken_dict, 'old_time', 'latest_time', 'load_time', 'time_taken'
        )

        # Get the hours, minutes and seconds from the time_taken string
        hours, minutes, seconds = map(int, time_taken.split(":"))
        previous_timeline_time_delta = timedelta(
            hours=hours, minutes=minutes, seconds=seconds
        )

        # This is unnecessary because the time difference will be calculated based on the condition below. But just to be prevent any error happens in the time_lapsed variable, as the time_lapsed data type must be timedelta object, so we will set it to the time difference between the latest time and the old time. 
        time_difference = latest_time - old_time

        if load_time:
            time_difference = latest_time - load_time
        else:
            time_difference = latest_time - old_time

        time_lapsed = time_difference + previous_timeline_time_delta

        # Get the hours, minutes and seconds from the time_lapsed timedelta object
        new_hours = time_lapsed.seconds // 3600
        new_minutes = (time_lapsed.seconds % 3600) // 60
        new_seconds = time_lapsed.seconds % 60

        formatted_time = f"{new_hours:02}:{new_minutes:02}:{new_seconds:02}"

        return formatted_time
    

    # Main methods

    # Handling multiple data

    # By default, it will return all the data.
    # It retrieve multiple data with limiting and filtering functionality if needed.
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

    def delete_all_load_games(self, player_list):
        try:
            # Filter all the completed games.
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

    # Clear all the data in the game state file.
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
    # In our case, for the player data, we use composite key (unique_id, player_name) to identify the player.
            
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

            # player dictionary is the shape of the game state of the player that we want to store in the file.
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
            
            # is_load_game is the flag to check whether the player is loading the game or moving from one scene to another.
            if is_load_game:
                latest_load_time = datetime.now()
                
            
            latest_game = datetime.now()

            condition = (
                lambda x: x["player_id"] == unique_id
                and x["player_name"] == player_name
            )

            result = gsa.find(
                self.data, condition=condition, limit=1
            )  # return the player list with only one player dictionary

            if not result:
                raise Exception("[UPDATE_USER] - No data found")

            if DEBUG:
                print("finding result passed")

            # Remove the last scene name if it is the same as the current scene name. This might happen when the player resume to the game.
            if result["scene_names"]:
                if result["scene_names"][-1] == scene["name"]:
                    result["scene_names"].pop()
            
            time_taken_dict = {
                        'old_time': result["updated_game"],
                        'latest_time': latest_game,
                        # This handle two cases: 
                        # 1. The player is loading the game. 
                        # 2. The player is moving from one scene to another.
                        'load_time': latest_load_time or result['latest_load_time'],
                        'time_taken': result["time_taken"]
                    }
                
            updated_player = {
                **result,
                "scene_names": [*result["scene_names"], scene["name"]],
                "updated_game": latest_game,
                'latest_load_time': latest_load_time or result['latest_load_time'],
                "time_taken": self.calculate_time_taken(
                    time_taken_dict
                ),
            }

            if DEBUG:
                print("updating player passed")

            # Remove the old player data from the list and append the updated player data. This is to ensure that the data is not duplicated and make sure the data is in reverse chronological order. (The latest data will be at the top of the list)
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


