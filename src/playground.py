from rich.table import Table, Column
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
#     show_lines=True,
#     box=box.SIMPLE,
#     padding=(0, 1),
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

# console.print(table)


from controllers import GameStateController
from datetime import datetime
import time

# data = GameStateController().retrieve_data(unique_id="081539", player_name="dfddsffds")
# print(data)
# {'player_id': '081539', 'player_name': 'dfddsffds', 'scene_names': ['enter forest', 'fireflies', 'follow melody', 'Escape woods'], 'start_game': datetime.datetime(2024, 1, 8, 15, 1, 41, 783384), 'updated_game': datetime.datetime(2024, 1, 8, 15, 2, 32, 750412), 'time_taken': '00:00:00'}
# {
#     "player_id": "83b239",
#     "player_name": "ddfdsaaaaaa",
#     "scene_names": ["enter forest"],
#     "start_game": datetime.datetime(2024, 1, 8, 15, 9, 58, 517295),
#     "updated_game": datetime.datetime(2024, 1, 8, 15, 10, 4, 332258),
#     "time_taken": "00:00:05",
# }
# {
#     "player_id": "83b239",
#     "player_name": "ddfdsaaaaaa",
#     "scene_names": ["enter forest", "fireflies"],
#     "start_game": datetime.datetime(2024, 1, 8, 15, 9, 58, 517295),
#     "updated_game": datetime.datetime(2024, 1, 8, 15, 10, 21, 441190),
#     "time_taken": "00:00:17",
# }
# {
#     "player_id": "83b239",
#     "player_name": "ddfdsaaaaaa",
#     "scene_names": ["enter forest", "fireflies", "ignore melody"],
#     "start_game": datetime.datetime(2024, 1, 8, 15, 9, 58, 517295),
#     "updated_game": datetime.datetime(2024, 1, 8, 15, 10, 37, 936576),
#     "time_taken": "00:00:16",
# }
# {
#     "player_id": "83b239",
#     "player_name": "ddfdsaaaaaa",
#     "scene_names": ["enter forest", "fireflies", "ignore melody", "ignore boat"],
#     "start_game": datetime.datetime(2024, 1, 8, 15, 9, 58, 517295),
#     "updated_game": datetime.datetime(2024, 1, 8, 15, 10, 53, 151528),
#     "time_taken": "00:00:15",
# }
# Game_win time_taken = 00:00:00


from datetime import datetime, timedelta
import time


def time_taken(initial_time, late_time, previous_time_line):
    # Convert string to timedelta
    hours, minutes, seconds = map(int, previous_time_line.split(":"))
    time_delta = timedelta(hours=hours, minutes=minutes, seconds=seconds)

    # Calculate time difference
    new_time = (late_time - initial_time) + time_delta

    # Format the result
    hours = new_time.seconds // 3600
    minutes = (new_time.seconds % 3600) // 60
    seconds = new_time.seconds % 60
    formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"

    return formatted_time


# Get initial time
initial_time = datetime.now()
time.sleep(5)  # Simulating a delay of 5 seconds
late_time = datetime.now()

previous_time_line = "00:10:05"

result = time_taken(initial_time, late_time, previous_time_line)
print(result)  # Output will be the formatted time taken
