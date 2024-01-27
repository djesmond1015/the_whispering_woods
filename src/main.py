# *********************************************************
# Program: The Whispering Woods (Text-Based Adventure Game)
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TL2L
# Year: 2023/24 Trimester 1
# Names: Chew Wei Zhi | Lee Jia Hee
# IDs: 1221108061 | 1221105751
# Emails: 1221108061@student.mmu.edu.my | 1221105751@student.mmu.edu.my
# Phones: +6016-3092896 | +6011-17764023
# *********************************************************

# Note: You may refer to the link below for the installation guide of the required packages:
# https://github.com/djesmond1015/the_whispering_woods?tab=readme-ov-file#prerequisites--installation-instructions


# This is the main file that will be executed to start the game
from configurations import handle_config, handle_config_dev

from app import AdventureGameEngine


def main():
    # Start the game engine (Entry point)
    app = AdventureGameEngine()
    app.start_game_engine()


if __name__ == "__main__":
    # Before starting the game, handle configurations based on the settings in settings.py
    handle_config()
    handle_config_dev()

    main()
