# Importing external modules
import uuid

# Importing built-in modules
import os, sys, time
from datetime import datetime

# Importing local modules
from dataset import scenes, WIN_SCENE
from utils import (
    destructure as ds,
    formatted_datetime as fd,
)
from settings import DEBUG
from controllers import GameStateController


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
    # The combination of player_id and player_name is unique for player identifying purpose
    def __init__(self, name, unique_id=None):
        self.name = name
        self.unique_id = unique_id or uuid.uuid4().hex[:6]


class GameMainMenu:
    def __init__(self):
        self.START_GAME = "1"
        self.LOAD_GAME = "2"
        self.STATISTICS = "3"
        self.EXIT_GAME = "4"
        self.menu = [
            "\t\tText Adventure Game",
            "\n",
            "\t\t1. Start Game",
            "\t\t2. Load Game",
            "\t\t3. Statistics",
            "\t\t4. Exit",
            "\n",
        ]


class LoadGameMenu:
    def __init__(self):
        self.exit = "[Q] - Return to menu"
        self.reset_game = "[R] - Reset game"
        self.game_list = self.get_game_list()
        self.load_game_menu = {
            "game_list": self.game_list,
            "reset_game": self.reset_game,
            "exit": self.exit,
        }

    def get_game_list(self):
        # the condition have issue because something the x['scene_names'] dict might be empty
        def condition(x):
            if x == []:
                return False
            else:
                return x["scene_names"][-1] != WIN_SCENE

        # condition = lambda x: x["scene_names"][-1] != WIN_SCENE
        # condition = (
        #     lambda x: x["scene_names"][-1] != WIN_SCENE or len(x["scene_names"]) == 0
        # )

        game_list = GameStateController().retrieve_multiple_data(
            condition=condition
        )  # retrieve all players with uncompleted games
        print("from game_list", game_list)
        # formatting the datetime for each player

        for game in game_list:
            game["start_game"] = fd(game["start_game"])
            game["updated_game"] = fd(game["updated_game"])

        if DEBUG:
            print(game_list)
            # time.sleep(10)

        return game_list

    def get_exit(self):
        return self.exit


class AdventureGameEngine:
    def __init__(self):
        self.keep_running = True
        self.initial_time = None
        self.printer = Printer()
        self.current_scene = self.get_scene("enter forest")
        self.player = None
        self.main_menu = GameMainMenu()
        self.main_menu_choice = None
        self.load_game_menu = None

    # Private methods
    def get_scene(self, scene_name):
        try:
            return list(filter(lambda x: x["name"] == scene_name, scenes))[0]
        except IndexError as e:
            print("[GET_SCENE_ERROR] - Invalid scene name")
            print(e)
            return

    # Utility methods
    def validate_name(self, name):
        # validate name - name must be at least 6 characters long and cannot contain numbers
        has_num = list(filter(lambda x: x.isdigit(), name))
        if len(name) < 6 or has_num:
            return False
        return True

    # Presentation methods
    def clear_screen(self):
        try:
            os.system("cls")
        except:
            os.system("clear")

    def display_main_menu(self, time_delay):
        self.printer.print_list_steps(self.main_menu.menu, time_delay)

    def display_saved_games(self, time_delay=0.02):
        self.printer.print_text_typewriter(
            "\n[S] - Save and back to menu?\n", time_delay
        )

    def display_scene(self, scene, time_delay=0.02):
        self.clear_screen()

        scene_text = scene["text"]
        # if that is only a choice
        if type(scene_text) != list:
            self.printer.print_text_typewriter(scene_text)

        # if that is a list of choices
        else:
            self.printer.print_text_lists_typewriter(scene_text, time_delay)

    def display_load_game(self, formatted_game_list, exit_text, reset_game):
        formatted_menu_list = [
            "\t\tSaved Games",
            "\n",
            "\tIndex \t\tPlayer \t\tCurrent Scene\t\tStart Game\t\tTime Taken",
            # print the player list
            *map(
                lambda x: f"\t{x['index']}\t\t{x['player_name']}\t{x['scene_names'][-1]}\t{x['start_game']}\t{x['time_taken']}",
                formatted_game_list,
            ),
            "\n",
            reset_game,
            exit_text,
        ]

        self.printer.print_list_once(formatted_menu_list)

    # Business logic methods
    def back_to_menu(self):
        self.clear_screen()
        self.display_main_menu(0.05)

    def handle_player_name_input(self):
        print("\nPlease enter a valid name (at least 6 characters long)")
        print("\n[Q] - Return to menu")

        player_name = input("Enter your name: ").strip()
        return player_name

    def register_player(self):
        # Enter player name
        player_name = self.handle_player_name_input()

        while not self.validate_name(player_name):
            # if player enter q or Q, return to menu
            if player_name == "q" or player_name == "Q":
                self.back_to_menu()
                return
                # break

            self.clear_screen()

            print(
                "[Invalid name - name must be at least 6 characters long and cannot contain numbers]"
            )

            player_name = self.handle_player_name_input()

        return player_name

    # The match_choice, is_game_completed and process_scene methods are three methods that are tightly coupled together to handle the game flow, the main feature of the game. The main method is the process_scene method and match choice method, while the other two methods are helper methods.
    def match_choice(self, user_choice, scene):
        self.clear_screen()

        # If the choice is in the choice list(multiple choice case), go to the next scene
        if user_choice in scene["choice"]:
            decision = scene["choice"][user_choice]

            self.current_scene = self.get_scene(decision)
            self.process_scene(self.current_scene)

        # If the choice is in the continue list(one choice case), continue to the next scene
        elif user_choice in scene["continue"]:
            self.current_scene = self.get_scene(user_choice)
            self.process_scene(self.current_scene)
        # If the choice is not in the choice list, the choice is invalidate, return False
        else:
            return False

        return True

    def is_game_completed(self, scene):
        if scene["choice"] == {} and scene["continue"][0] == False:
            return True

    def process_scene(self, scene, is_load_game=False):
        if is_load_game:
            GameStateController().update_data(
                self.player.unique_id,
                self.player.name,
                scene,
                is_load_game=is_load_game,
            )

            if DEBUG:
                result = GameStateController().retrieve_data(
                    self.player.unique_id, self.player.name
                )
                print("load_game_process_scene", result)
                time.sleep(5)

        self.display_scene(scene, 0.02)

        # Update game state after each scene
        GameStateController().update_data(
            self.player.unique_id, self.player.name, scene
        )

        if DEBUG:
            result = GameStateController().retrieve_data(
                self.player.unique_id, self.player.name
            )
            print(result)
            # time.sleep(5)

        # If the game is completed and the player win, save the game state and reset the game scene
        # return
        if self.is_game_completed(scene):
            self.current_scene = self.get_scene("enter forest")

            GameStateController().update_data(
                self.player.unique_id, self.player.name, {"name": WIN_SCENE}
            )

            if DEBUG:
                result = GameStateController().retrieve_data(
                    self.player.unique_id, self.player.name
                )
                print(result)
                # time.sleep(10)

            print("You win!")
            time.sleep(2)

            return

        while True:
            print("\n")
            self.display_saved_games(0.02)

            # In this If-else statement block, we handle two different cases of user input.
            # If there is no choice, show the continue to the next scene message
            if scene["continue"][0] == True:
                print("\n")
                is_save_and_back_to_menu = input("Press enter to continue...")

                # If player press enter, continue to the next scene, else save and back to menu
                choice = is_save_and_back_to_menu or scene["continue"][1]

            else:
                choice = input("Enter your choice: ").strip()

            # If player press s or S, return to menu
            if choice == "s" or choice == "S":
                self.back_to_menu()
                break

            # Check if the choice is valid, if not, show the scene again and print invalid choice message
            is_valid_choice = self.match_choice(choice, scene)

            if is_valid_choice:
                break
            else:
                self.display_scene(scene, 0)
                print("\n")
                print("[Invalid choice]")

    # # The process_load_game and format_saved_game_list methods are two methods that are tightly coupled together to handle the load game feature. The main method is the process_load_game method, while the other method is a helper method.
    def format_saved_game_list(self, game_list):
        formatted_game_list = list(
            map(
                lambda x: {
                    "index": x[0] + 1,
                    "player_id": x[1]["player_id"],
                    "player_name": x[1]["player_name"],
                    "scene_names": x[1]["scene_names"],
                    "start_game": x[1]["start_game"],
                    "time_taken": x[1]["time_taken"],
                },
                enumerate(game_list),
            )
        )

        return formatted_game_list

    def process_load_game(self):
        self.clear_screen()
        self.load_game_menu = LoadGameMenu()

        # Get the raw data from the load_game_menu
        game_menu_data = self.load_game_menu.load_game_menu

        game_list, exit, reset_game = ds(
            game_menu_data, "game_list", "reset_game", "exit"
        )

        # Format the player list from the raw data before displaying the load game menu
        formatted_game_list = self.format_saved_game_list(game_list)
        self.display_load_game(formatted_game_list, exit, reset_game)

        # Get the last scene of each player
        last_scenes = list(map(lambda x: x["scene_names"][-1], game_list))

        while True:
            choice = input("Enter game number: ").strip()

            # Check the reserved keyword for exit and reset game
            if choice == "q" or choice == "Q":
                self.back_to_menu()

                return

            elif choice == "r" or choice == "R":
                GameStateController().delete_all_load_games(game_list)

                self.clear_screen()
                print("Resetting game ...")
                time.sleep(2)

                self.back_to_menu()

                return

            # Check if the choice is valid, if not, show the load game menu again and print invalid choice message
            try:
                is_valid_choice = int(choice) in range(1, len(last_scenes) + 1)

                if not is_valid_choice:
                    raise ValueError

                # Dealing with 2 tasks:
                # 1. Get the last scene of the selected game
                # 2. Get the information of the player
                formatted_choice = int(choice) - 1  # index start from 0

                selected_scene = last_scenes[
                    formatted_choice
                ]  # get the last scene of the selected game

                # Get the load scene and return it to the main menu controller
                load_scene = self.get_scene(selected_scene)

                load_game_choice = int(choice)  # User choice
                load_game_dictionary = formatted_game_list[
                    load_game_choice - 1
                ]  # Get the load game dictionary from the load data based on the user choice

                # get the player object from the player list by matching the player_id and player_name as [player_id, player_name] is unique
                load_player = list(
                    filter(
                        lambda x: x["player_id"] == load_game_dictionary["player_id"]
                        and x["player_name"] == load_game_dictionary["player_name"],
                        game_list,
                    )
                )[0]

                # Initialize player object before loading the game
                self.player = Player(
                    load_player["player_name"], load_player["player_id"]
                )

                self.clear_screen()
                print("Loading game ...")
                time.sleep(2)

                return load_scene

            except ValueError:
                self.clear_screen()
                self.display_load_game(formatted_game_list, exit, reset_game)

                print("\n")
                print("[Invalid choice]")

    # Game Engine Local Controller methods
    def main_menu_controller(self):
        self.main_menu_choice = input("Enter your choice: ").strip()

        match self.main_menu_choice:
            case self.main_menu.START_GAME:
                self.clear_screen()

                # User registration
                player_name = self.register_player()

                # If player enter q or Q, return to menu
                if not player_name:
                    return

                # Initialize game state
                self.player = Player(player_name)
                self.initial_time = datetime.now()

                GameStateController().create_data(self.player, self.initial_time)

                if DEBUG:
                    response = GameStateController().retrieve_data(
                        self.player.unique_id,
                        self.player.name,
                    )
                    print(response)
                    # time.sleep(10)

                self.clear_screen()
                print("Starting game...")
                time.sleep(2)

                self.process_scene(self.current_scene)

            case self.main_menu.LOAD_GAME:
                load_scene = self.process_load_game()

                # If load_scene is None, return to menu
                if not load_scene:
                    return

                self.process_scene(load_scene, is_load_game=True)

            case self.main_menu.STATISTICS:
                print("Loading statistics ...")
                time.sleep(2)

            case self.main_menu.EXIT_GAME:
                print("See you next time!")
                time.sleep(2)
                self.clear_screen()
                self.keep_running = False

            case _:
                print("Invalid input, please try again.")
                time.sleep(1)

    # Main methods - single entry point
    def start_game_engine(self):
        self.clear_screen()
        self.display_main_menu(0.05)

        while self.keep_running:
            self.main_menu_controller()

            # Clear the screen before showing the menu again
            self.clear_screen()
            self.display_main_menu(0)

        # Clear the screen after exit the game
        self.clear_screen()


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
