import uuid

import os, sys, time
from datetime import datetime

from dataset import display_menu as dm, scenes
from utils import destructure as ds
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
    def __init__(self, name):
        self.name = name
        self.unique_id = uuid.uuid4().hex[:6]


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
    def retrieve_multiple_data(self, limit=False):
        if limit:
            data = gsa.load_game_state()
            limited_result = gsa.find(data, limit=limit)
            return limited_result
        else:
            data = gsa.load_game_state()

        return data

    def reset_game(self):
        gsa.save_game_state([])

    def delete_file(self):
        gsa.delete_game_state()

    # Handling single data
    def retrieve_data(self, unique_id, player_name):
        data = gsa.load_game_state()

        condition = (
            lambda x: x["player_id"] == unique_id and x["player_name"] == player_name
        )
        result = gsa.find(data, condition=condition)

        return result

    def create_data(self, player, scene, initial_time):
        player_id, player_name = ds(player.__dict__, "unique_id", "name")
        scene_name = scene["name"]

        player_list = {
            "player_id": player_id,
            "player_name": player_name,
            "scene_name": scene_name,
            "start_game": initial_time,
            "time_taken": "00:00:00",
        }

        data = gsa.load_game_state()
        data.append(player_list)
        gsa.save_game_state(data)

    def update_data(self, unique_id, player_name, new_data):
        pass

    def delete_data(self, unique_id, player_name):
        pass

    # Utility methods
    def calculate_time_taken(self):
        pass


class LoadGameMenu:
    def __init__(self):
        self.exit = "[Q] - Return to menu"
        self.player_list = []
        self.load_game_menu = {
            "player_list": self.player_list,
            "exit": self.exit,
        }

    def get_player_list(self):
        return self.player_list

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

    def display_load_game(self):
        load_game_menu = LoadGameMenu()
        player_list = load_game_menu.get_player_list()

        # "player_id": 1,
        #     "player_name": "John",
        #     "scene_name": "enter forest",
        #     "start_game": "2020-12-12 12:12:12",
        #     "time_taken": "00:00:00",
        # TODO: Add index to the player list
        formatted_menu_list = [
            "\t\tSaved Games",
            "\n",
            "\t\tPlayer \t\tScene Name\t\tStart Game\t\tTime Taken",
            *player_list,
            "\n",
            load_game_menu.get_exit(),
        ]

        self.printer.print_list_once(formatted_menu_list)

    def process_load_game(self):
        self.clear_screen()
        self.display_load_game()

        while True:
            choice = input("Enter game number: ")

            if choice == "q" or choice == "Q":
                self.back_to_menu()
                break

            valid_choice = self.choice_match(choice, scene)
            if valid_choice:
                break
            else:
                self.show_scene(scene)
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
        self.game_state.save_game_state()

        if scene["choice"] == {} and scene["continue"][0] == False:
            self.current_scene = scenes["enter forest"]
            # TODO: Delete the saved game state file and add the game state to the permanent file
            print("You win!")
            time.sleep(2)
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

                initial_scene = self.current_scene
                self.player = Player(player_name)
                self.initial_time = datetime.now()

                GameStateController().create_data(
                    self.player, initial_scene, self.initial_time
                )

                self.clear_screen()
                print("Starting game...")
                time.sleep(2)

                self.process_scene(self.current_scene)
            case self.LOAD_GAME:
                print("Loading game ...")
                time.sleep(2)
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

        time.sleep(2)

        while self.keep_running:
            self.process_menu_navigation()
            # Clear the screen before showing the menu again
            self.clear_screen()
            self.display_menu(dm, 0)

        # Clear the screen after exit the game
        self.clear_screen()
