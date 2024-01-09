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
