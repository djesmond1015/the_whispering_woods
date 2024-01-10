from rich.table import Table, Column
from rich.panel import Panel
from rich.console import Console
from rich import box

console = Console()

# # # Text
# # console.print("Hello world", style="bold red")
# # console.print("[u]Hello[/u] [bold cyan]Jesse[/bold cyan]")

# # # Emoji
# # console.print("I :heart: coding :smiley:")


# # Table
# table = Table(
#     show_header=True,
#     header_style="bold cyan",
#     title="Load Game",
#     title_style="bold magenta",
#     show_lines=False,
#     box=box.SIMPLE,
#     expand=True,
# )

# # Define Column with less dim style
# table.add_column("No", style="grey7", width=20)
# table.add_column("Player", style="grey7", width=20)
# table.add_column("Current Scene", style="grey7", width=20)
# table.add_column("Start Game", style="grey7", width=20)
# table.add_column("Time Taken", style="grey7", width=20)

# # Add your Data into the Rows
# table.add_row("1", "Jesse", "Scene 1", "2021-01-01 00:00:00", "00:00:00")
# table.add_row("1", "Jesse", "Scene 1", "2021-01-01 00:00:00", "00:00:00")

# console.print(table, justify="center")


# show_header=True: Indicates that the table will have a header row.
# header_style="bold cyan": Specifies the style of the header text, making it bold and colored in cyan.
# title="Load Game": Sets a title for the table as "Load Game".
# title_style="bold magenta": Defines the style for the table title, making it bold and colored in magenta.
# show_lines=True: Displays lines separating the table cells.
# box=box.SIMPLE: Sets the box style of the table to a simple border.
# expand=True: Allows the table to expand to fit the available space in the terminal.

# from controllers import GameStateController

# data = GameStateController().retrieve_multiple_data()

# print(data)

# from utils import formatted_datetime as fd

# data = [
#     {
#         "player_id": "420c33",
#         "player_name": "ldfjkldfj",
#         "scene_names": ["enter forest", "fireflies", "follow melody", "Escape woods"],
#         "start_game": datetime.datetime(2024, 1, 9, 17, 37, 5, 551508),
#         "latest_load_time": datetime.datetime(2024, 1, 9, 17, 45, 15, 433054),
#         "updated_game": datetime.datetime(2024, 1, 9, 17, 45, 51, 225248),
#         "time_taken": "00:02:22",
#     },
#     {
#         "player_id": "18123b",
#         "player_name": "gfgfdfghdfhg",
#         "scene_names": [
#             "enter forest",
#             "fireflies",
#             "ignore melody",
#             "take boat",
#             "Escape woods",
#         ],
#         "start_game": datetime.datetime(2024, 1, 9, 17, 49, 23, 223834),
#         "latest_load_time": datetime.datetime(2024, 1, 9, 17, 50, 27, 858722),
#         "updated_game": datetime.datetime(2024, 1, 9, 17, 50, 58, 956654),
#         "time_taken": "00:02:08",
#     },
#     {
#         "player_id": "420c33",
#         "player_name": "ldfjkldfj",
#         "scene_names": ["enter forest", "fireflies", "follow melody", "Escape woods"],
#         "start_game": datetime.datetime(2024, 1, 9, 17, 33, 5, 551508),
#         "latest_load_time": datetime.datetime(2024, 1, 9, 17, 45, 15, 433054),
#         "updated_game": datetime.datetime(2024, 1, 9, 17, 45, 51, 225248),
#         "time_taken": "00:02:22",
#     },
# ]

# sorted_data = sorted(data, key=lambda player: fd(player["start_game"]), reverse=True)

# print(sorted_data)

# [
#     {
#         "player_id": "18123b",
#         "player_name": "gfgfdfghdfhg",
#         "scene_names": [
#             "enter forest",
#             "fireflies",
#             "ignore melody",
#             "take boat",
#             "Escape woods",
#         ],
#         "start_game": datetime.datetime(2024, 1, 9, 17, 49, 23, 223834),
#         "latest_load_time": datetime.datetime(2024, 1, 9, 17, 50, 27, 858722),
#         "updated_game": datetime.datetime(2024, 1, 9, 17, 50, 58, 956654),
#         "time_taken": "00:02:08",
#     },
#     {
#         "player_id": "420c33",
#         "player_name": "ldfjkldfj",
#         "scene_names": ["enter forest", "fireflies", "follow melody", "Escape woods"],
#         "start_game": datetime.datetime(2024, 1, 9, 17, 37, 5, 551508),
#         "latest_load_time": datetime.datetime(2024, 1, 9, 17, 45, 15, 433054),
#         "updated_game": datetime.datetime(2024, 1, 9, 17, 45, 51, 225248),
#         "time_taken": "00:02:22",
#     },
#     {
#         "player_id": "420c33",
#         "player_name": "ldfjkldfj",
#         "scene_names": ["enter forest", "fireflies", "follow melody", "Escape woods"],
#         "start_game": datetime.datetime(2024, 1, 9, 17, 33, 5, 551508),
#         "latest_load_time": datetime.datetime(2024, 1, 9, 17, 45, 15, 433054),
#         "updated_game": datetime.datetime(2024, 1, 9, 17, 45, 51, 225248),
#         "time_taken": "00:02:22",
#     },
# ]

# data = [
#     {
#         "player_id": "eae476",
#         "player_name": "sddfdfgdf",
#         "scene_names": ["ff", "ssss"],
#     },
#     {
#         "player_id": "dfea1e",
#         "player_name": "q",
#         "scene_names": ["ff", "fsf"],
#     },
#     {
#         "player_id": "dfewa1e",
#         "player_name": "w",
#         "scene_names": [],
#     },
# ]
# player_with_highest_num_of_scene = max(
#     data, key=lambda x: len(x["scene_names"]) if "scene_names" in x else 0
# )

# print(player_with_highest_num_of_scene)


# # TODO: Truncate the name
# # make_truncated_name = lambda name: name[:10] + "..." if len(name) > 10 else name
