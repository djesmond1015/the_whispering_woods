# The Whispering Forest

> A text-based adventure game written in Python

<br>

![Game Preview](docs/static/svg/game_preview_screen.svg)

## Table of Contents

- [The Whispering Forest](#the-whispering-forest)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Prerequisites \& Installation Instructions](#prerequisites--installation-instructions)
    - [Approach 1: Install standalone executable file](#approach-1-install-standalone-executable-file)
    - [Approach 2: Install using pip](#approach-2-install-using-pip)
  - [Game Play](#game-play)
    - [Game Flow](#game-flow)
    - [Game Main Menu](#game-main-menu)
    - [Game Load](#game-load)
    - [Game Statistics](#game-statistics)
    - [Game Export](#game-export)
  - [Acknowledgements](#acknowledgements)
  - [Author](#author)
  - [Contact](#contact)

<br>

## Introduction

The Whispering Forest is a text-based adventure game that is inspired by the classic text-based adventure games of the 1980s. The game is set in a fantasy world where the player must navigate through a woods to find a way to escape. The game is written in Python and is designed to be played in the terminal.

The game is designed to be played by a single player. The player will be able to navigate through the game by typing in commands.

What make the game unique are the following features:

1. Amazing game flow
2. Stylish text with Rich library
3. ChatGPT-like typewriter effect of text
4. Save and load game state
5. Game statistics of the completed game
6. Export dataset feature

<br>

## Prerequisites & Installation Instructions

### Approach 1: Install standalone executable file

1. Download the executable file (.exe) [here](https://github.com/djesmond1015/the_whispering_woods/blob/main/theWhisperingForest.zip).
2. Run the executable file.
3. Enjoy the game.

<br>

### Approach 2: Install using pip

1. Git clone the repository or download the zip file.

```bash
git clone https://github.com/djesmond1015/the_whispering_woods.git
```

<br>

2. Create a virtual environment. (optional)

We strongly recommend you to run the game in a virtual environment. You can create a virtual environment by typing the following command in the terminal.

```bash
python -m venv venv
```

<br>

Activate the virtual environment by typing the following command in the terminal.

If you are using Linux or macOS, type the following command in the terminal.

```bash
source venv/bin/activate
```

If you are using Windows, type the following command in the terminal.

```command prompt
venv\Scripts\activate
```

<br>

3. Install the dependencies using pip.

We assume that you have Python 3.6 or higher installed on your system. If not, please install it first.

```bash
pip install -r requirements.txt
```

<br>

4. Run the application.

Once the installation is complete, you can run the game by typing the following command in the terminal.

```bash
python -u src/main.py
```

<br>

## Game Play

### Game Flow

The game flow of The Whispering Forest is non-linear(multiple options) and is designed to be played multiple times with the same ending for each game.

You can find the game flow chart in Simple Form [here](docs/static/svg/game_flow_simple.svg) and Detailed Form [here](docs/static/svg/game_flow_detailed.svg).

**Pro tip: Open the flow chart in a new tab to view it in full size.**

<br>

### Game Main Menu

When you first run the game, you will be greeted with the Main Menu:
![Game Main Menu](docs/static/svg/main_menu.svg)

<br>

### Game Load

This is the place where you can load your saved game and resume your fantastic odyssey. Only uncompleted games will be shown. The latest start game will be shown at the top of the list.
![Game Load](docs/static/svg/game_load.svg)

<br>

### Game Statistics

This is the place where you can view your game statistics. Only completed games will be shown.
![Game Statistics](docs/static/svg/game_statistics.svg)

<br>

### Game Export

If you would like to export the dataset of the game flow as shown in the [Game Flow](#game-flow) section, you can do so by navigating to the About page and choosing the Export option. We support exporting the dataset in **JSON** and **TXT** formats.
![Game Export](docs/static/svg/game_export.svg)

<br>

Alternatively, you can find the game flow dataset in the dataset.py in the src folder. Please click [here](src/dataset.py#L57).

<br>

## Acknowledgements

1. [Grumpy Gamer - Puzzle Dependency Charts](https://grumpygamer.com/puzzle_dependency_charts)
2. [Text Adventure Game Design in 2020 | by Chris Ainsley | Medium](https://medium.com/@model_train/text-adventure-game-design-in-2020-608528ac8bda)
3. [EASY Typewriter Effect for BEGINNERS - Python ASCII Tutorial](https://youtu.be/EVudW0H_2T8?si=vhtljV73KEpJpqC8)

<br>

## Author

Made with ❤️ by Desmond Lee & Robin Chew

<br>

## Contact

If you have any questions, feel free to contact us at:

- Gmail: lee.desmond2016@gmail.com
- Github: [Desmond Lee](https://github.com/djesmond1015)

Don't forget to give us a star if you like this project! ⭐🥰
<br>
