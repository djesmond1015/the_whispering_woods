# *********************************************************
# Program: app.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TL2L
# Year: 2023/24 Trimester 1
# Names: Chew Wei Zhi | Lee Jia Hee
# IDs: 1221108061 | 1221105751
# Emails: 1221108061@student.mmu.edu.my | 1221105751@student.mmu.edu.my
# Phones: +6016-3092896 | +6011-17764023
# *********************************************************


from configurations import handle_config, handle_config_dev

from app import AdventureGameEngine


def main():
    app = AdventureGameEngine()
    app.start_game_engine()


if __name__ == "__main__":
    handle_config()
    handle_config_dev()
    main()
