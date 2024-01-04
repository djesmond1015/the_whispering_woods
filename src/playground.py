import keyboard
import time
from src.app import Printer

display_menu = [
    "\t\tText Adventure Game",
    "\n",
    "\t\t1. Start Game",
    "\t\t2. Load Game",
    "\t\t3. Exit",
    "\n",
]

printer = Printer()


def print_with_keyboard_blocked(text):
    keyboard.block_key("*")  # Block all keys
    printer.print_text_lists_typewriter(text)
    keyboard.unblock_key("*")  # Unblock all keys


def main():
    print_with_keyboard_blocked(display_menu)
    time.sleep(2)
    resault = input("Press enter to continue...")


main()
