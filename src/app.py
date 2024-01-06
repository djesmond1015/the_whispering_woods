import uuid

import os, sys, time
from datetime import datetime

from dataset import display_menu as dm, scenes, WIN_SCENE
from utils import (
    destructure as ds,
    formatted_datetime as fd,
)
from adapter import GameStateAdapter

gsa = GameStateAdapter()


class Printer:
    def __init__(self):
        pass

    def print_list_once(self, list):
        for item in list:
            print(item)

    def print_list_steps(self, list, time_delay=1):
        for item in list:
            print(item)
            time.sleep(time_delay)

    def print_text_typewriter(self, text, time_delay=0.05):
        for char in text:
            sys.stdout.write(
                char
            )  # write the next character same as print built-in function
            sys.stdout.flush()
            time.sleep(time_delay)

    def print_text_lists_typewriter(self, list, time_delay=0.05):
        for item in list:
            for char in item:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(time_delay)
            print()


class Player:
    def __init__(self, name, unique_id=None):
        self.name = name
        self.unique_id = unique_id or uuid.uuid4().hex[:6]


# All GameStateController methods:
# 1. retrieve all data [GET]
# 3. reset the game (empty the file) [DELETE] (this will never be used)
# 2. delete all data (delete file) [DELETE] (this will never be used)

# 1. retrieve particular data [GET] - (unique_id, player_name)
# 2. insert or create data [POST] - (player, scene)
# 3. update data [PUT] - (player, scene)
# 4. delete data [DELETE] - list of (unique_id, player_name)


class GameStateController:
    def __init__(self):
        pass

    # Handling all data
    def retrieve_multiple_data(self, limit=False, condition=False):
        try:
            if limit:
                data = gsa.load_game_state()
                limited_result = gsa.find(data, limit=limit)
                return limited_result
            elif condition:
                data = gsa.load_game_state()
                result = gsa.find(data, condition=condition, limit=False)
                return result
            else:
                data = gsa.load_game_state()

            return data
        except Exception as e:
            print("[RETRIEVE_ALL_ERROR] - Something went wrong")
            print(e)

    def reset_game(self):
        try:
            gsa.save_game_state([])
        except Exception as e:
            print("[RESET_GAME_ERROR] - Something went wrong")
            print(e)

    def delete_file(self):
        try:
            gsa.delete_game_state()
        except Exception as e:
            print("[DELETE_FILE_ERROR] - Something went wrong")
            print(e)

    # Handling single data
    def retrieve_data(self, unique_id, player_name):
        try:
            data = gsa.load_game_state()

            condition = (
                lambda x: x["player_id"] == unique_id
                and x["player_name"] == player_name
            )
            result = gsa.find(data, condition=condition, limit=1)

            return result
        except Exception as e:
            print("[RETRIEVE_USER_ERROR] - Something went wrong")
            print(e)

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

            data = gsa.load_game_state()
            data.append(player)
            gsa.save_game_state(data)
        except Exception as e:
            print("[CREATE_USER_ERROR] - Something went wrong")
            print(e)

    def update_data(self, unique_id, player_name, scene):
        try:
            if not unique_id or not player_name:
                raise Exception("[UPDATE_USER] - Invalid input")

            print("finding data passed")

            data = gsa.load_game_state()
            latest_game = datetime.now()

            condition = (
                lambda x: x["player_id"] == unique_id
                and x["player_name"] == player_name
            )

            result = gsa.find(
                data, condition=condition
            )  # return the player list with only player dictionary
            result = result[0]  # return the player dictionary

            if not result:
                raise Exception("[UPDATE_USER] - No data found")

            print("finding result passed")

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

            print("updating player passed")
            filtered_data = list(
                filter(
                    (
                        lambda x: x["player_id"] != unique_id
                        and x["player_name"] != player_name
                    ),
                    data,
                )
            )

            print("filtering data passed")
            filtered_data.append(updated_player)
            print("appending data passed")
            gsa.save_game_state(filtered_data)

        except Exception as e:
            print("[UPDATE_USER_ERROR] - Something went wrong")
            print(e)

    def delete_data(self, unique_id, player_name):
        pass

    # Utility methods
    def calculate_time_taken(self, old_time, latest_time):
        time_lapsed = latest_time - old_time
        total_seconds = time_lapsed.total_seconds()

        hours = int(total_seconds // 3600)  # 3600 seconds in 1 hour
        minutes = int((total_seconds % 3600) // 60)  # 60 seconds in 1 minute
        seconds = int(total_seconds % 60)  # 60 seconds in 1 minute

        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


class LoadGameMenu:
    def __init__(self):
        # {
        #     "player_id": player_id,
        #     "player_name": player_name,
        #     "scene_names": [],
        #     "start_game": initial_time,
        #     "updated_game": initial_time,
        #     "time_taken": "00:00:00",
        # }

        self.exit = "[Q] - Return to menu"
        self.player_list = self.get_player_list()
        self.load_game_menu = {
            "player_list": self.player_list,
            "exit": self.exit,
        }

    def get_player_list(self):
        condition = lambda x: x["scene_names"][-1] != WIN_SCENE

        players = GameStateController().retrieve_multiple_data(
            condition=condition
        )  # retrieve all players with uncompleted games

        # formatting the datetime for each player
        for player in players:
            player["start_game"] = fd(player["start_game"])
            player["updated_game"] = fd(player["updated_game"])

        return players

    def get_exit(self):
        return self.exit


class GameStatistics:
    def __init__(self):
        pass

    def get_time_taken(self):
        pass

    def get_number_of_scenes(self):
        pass

    def get_highest_number_of_scenes(self):
        pass

    def get_lowest_number_of_scenes(self):
        pass

    def get_average_time_taken(self):
        pass

    def get_shortest_time_taken(self):
        pass

    def get_longest_time_taken(self):
        pass

    def get_number_of_wins(self):
        pass


class AdventureGameEngine:
    def __init__(self):
        self.START_GAME = "1"
        self.LOAD_GAME = "2"
        self.STATISTICS = "3"
        self.EXIT_GAME = "4"
        self.keep_running = True
        self.initial_time = None
        self.printer = Printer()
        self.current_scene = scenes["enter forest"]
        self.player = None

    def clear_screen(self):
        try:
            os.system("cls")
        except:
            os.system("clear")

    def display_menu(self, display_menu, time_delay):
        self.printer.print_list_steps(display_menu, time_delay)

    def display_saved_games(self, time_delay):
        self.printer.print_text_typewriter(
            "\n[S] - Save and back to menu?\n", time_delay
        )

    def display_load_game(self, load_game_menu):
        player_list, exit = ds(load_game_menu, "player_list", "exit")

        load_data = list(
            map(
                lambda x: {
                    "index": x[0] + 1,
                    "player_id": x[1]["player_id"],
                    "player_name": x[1]["player_name"],
                    "scene_names": x[1]["scene_names"],
                    "start_game": x[1]["start_game"],
                    "time_taken": x[1]["time_taken"],
                },
                enumerate(player_list),
            )
        )

        formatted_menu_list = [
            "\t\tSaved Games",
            "\n",
            "\tIndex \t\tPlayer \t\tCurrent Scene\t\tStart Game\t\tTime Taken",
            # print the player list
            *map(
                lambda x: f"\t{x['index']}\t\t{x['player_name']}\t{x['scene_names'][-1]}\t\t{x['start_game']}\t{x['time_taken']}",
                load_data,
            ),
            "\n",
            exit,
        ]

        self.printer.print_list_once(formatted_menu_list)

        return load_data

    def process_load_game(self):
        self.clear_screen()

        load_game_menu = LoadGameMenu()
        load_game_menu = load_game_menu.load_game_menu

        # self.load_game_menu = {
        #     "player_list": self.player_list,
        #     "exit": self.exit,
        # }
        # {
        #     "player_id": player_id,
        #     "player_name": player_name,
        #     "scene_names": [],
        #     "start_game": initial_time,
        #     "updated_game": initial_time,
        #     "time_taken": "00:00:00",
        # }

        load_data = self.display_load_game(load_game_menu)

        player_list = load_game_menu["player_list"]

        last_scenes = list(map(lambda x: x["scene_names"][-1], player_list))

        while True:
            choice = input("Enter game number: ").strip()

            if choice == "q" or choice == "Q":
                self.back_to_menu()

                break

            if int(choice) in range(1, len(last_scenes) + 1):
                formatted_choice = int(choice) - 1

                selected_scene = last_scenes[formatted_choice]

                scene = scenes[selected_scene]

                load_game_choice = int(choice)
                load_game_object = load_data[load_game_choice - 1]

                # get the player from the player_list using player_name and player_id from the load_game_object
                load_player = list(
                    filter(
                        lambda x: x["player_id"] == load_game_object["player_id"]
                        and x["player_name"] == load_game_object["player_name"],
                        player_list,
                    )
                )[0]

                print("player", load_player)
                time.sleep(5)

                self.player = Player(
                    load_player["player_name"], load_player["player_id"]
                )

                print("Loading game ...")
                time.sleep(2)

                self.process_scene(scene)

                break

            else:
                self.clear_screen()
                self.display_load_game(load_game_menu)

                print("\n")
                print("[Invalid choice]")

    def back_to_menu(self):
        self.clear_screen()
        self.display_menu(dm, 0.05)

    def validate_name(self, name):
        has_num = any(type(char) == int for char in name)
        if len(name) < 6 or has_num:
            return False
        return True

    def print_choices(self, message, time_delay=0.02):
        if type(message) != list:
            self.printer.print_text_typewriter(message)
        else:
            self.printer.print_text_lists_typewriter(message, time_delay)

    def show_scene(self, scene, time_delay=0):
        self.clear_screen()
        self.print_choices(scene["text"], time_delay)

    def choice_match(self, user_choice, scene):
        self.clear_screen()

        if user_choice in scene["choice"]:
            decision = scene["choice"][user_choice]
            self.current_scene = scenes[decision]
            self.process_scene(self.current_scene)
        elif user_choice in scene["continue"]:
            self.current_scene = scenes[user_choice]
            self.process_scene(self.current_scene)
        else:
            return False

        return True

    def process_scene(self, scene):
        self.show_scene(scene, 0.02)
        GameStateController().update_data(
            self.player.unique_id, self.player.name, scene
        )

        result = GameStateController().retrieve_data(
            self.player.unique_id, self.player.name
        )

        print(result)
        time.sleep(10)

        if scene["choice"] == {} and scene["continue"][0] == False:
            self.current_scene = scenes["enter forest"]

            GameStateController().update_data(
                self.player.unique_id, self.player.name, {"name": WIN_SCENE}
            )

            result = GameStateController().retrieve_data(
                self.player.unique_id, self.player.name
            )
            print(result)
            print("You win!")
            time.sleep(10)
            return

        self.display_saved_games(0.02)

        while True:
            if scene["continue"][0] == True:
                print("\n")
                input("Press enter to continue...")
                choice = scene["continue"][1]

            else:
                choice = input("Enter your choice: ")

            if choice == "s" or choice == "S":
                self.back_to_menu()
                break

            valid_choice = self.choice_match(choice, scene)
            if valid_choice:
                break
            else:
                self.show_scene(scene)
                print("\n")
                print("[Invalid choice]")

    def process_menu_navigation(self):
        self.menu_choice = input("Enter your choice: ")

        match self.menu_choice:
            case self.START_GAME:
                self.clear_screen()
                print("Please enter a valid name (at least 6 characters long)")
                player_name = input("Enter your name: ").strip()

                while not self.validate_name(player_name):
                    self.clear_screen()
                    print(
                        "[Invalid name - name must be at least 6 characters long and cannot contain numbers]"
                    )
                    print("\nPlease enter a valid name (at least 6 characters long)")
                    player_name = input("Enter your name: ").strip()

                # initial_scene = self.current_scene
                self.player = Player(player_name)
                self.initial_time = datetime.now()

                GameStateController().create_data(self.player, self.initial_time)

                response = GameStateController().retrieve_data(
                    self.player.unique_id,
                    self.player.name,
                )
                print(response)
                time.sleep(10)

                self.clear_screen()
                print("Starting game...")
                time.sleep(2)

                self.process_scene(self.current_scene)
            case self.LOAD_GAME:
                self.process_load_game()

            case self.STATISTICS:
                print("Loading statistics ...")
                time.sleep(2)
            case self.EXIT_GAME:
                print("See you next time!")
                time.sleep(2)
                self.clear_screen()
                self.keep_running = False
            case _:
                print("Invalid input, please try again.")
                time.sleep(1)

    def start_game_engine(self):
        self.clear_screen()
        self.display_menu(dm, 0.05)

        while self.keep_running:
            self.process_menu_navigation()
            # Clear the screen before showing the menu again
            self.clear_screen()
            self.display_menu(dm, 0)

        # Clear the screen after exit the game
        self.clear_screen()
