import uuid, pickle

import os, sys, time
from pathlib import Path

from dataset import display_menu as dm, scenes


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


class GameState:
    def __init__(self, player, state):
        self.player = player
        self.current_state = state
        self.directory = self.create_directory()

    def create_directory(self):
        pwd = os.getcwd()
        path = Path(pwd + "/state_manager")
        path.mkdir(parents=True, exist_ok=True)
        return path

    def get_file_path(self):
        return self.directory / f"{self.unique_id}_{self.player.name}_game_state.pkl"

    def save_game_state(self):
        with open(self.get_file_path(), "wb") as file:
            pickle.dump(self, file)

    def load_game_state(self):
        with open(self.get_file_path(), "rb") as file:
            return pickle.load(file)


class AdventureGameEngine:
    def __init__(self):
        self.START_GAME = "1"
        self.LOAD_GAME = "2"
        self.EXIT_GAME = "3"
        self.keep_running = True
        self.current_scene = scenes["enter forest"]
        self.printer = Printer()
        # self.game_state = GameState()

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

    def back_to_menu(self):
        self.clear_screen()
        self.display_menu(dm, 0.05)

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

        if scene["choice"] == {} and scene["continue"][0] == False:
            self.current_scene = scenes["enter forest"]
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
                print("Starting game...")
                time.sleep(2)
                self.process_scene(self.current_scene)
            case self.LOAD_GAME:
                print("Loading game ...")
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
