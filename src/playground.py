from rich.table import Table, Column
from rich.panel import Panel
from rich.console import Console
from rich import box

console = Console()

[
    "\t\tText Adventure Game - ",
    "\t\tThe Whispering Woods" "\n",
    "\t\t1. Start Game",
    "\t\t2. Load Game",
    "\t\t3. Statistics",
    "\t\t4. Exit",
    "\n",
]

menu = ["1. Start Game", "2. Load Game", "3. Statistics", "4. Exit"]

# Remake the menu using rich

console.print(
    "Text Adventure Game - [bold magenta]The Whispering Woods",
    end="",
    style="yellow",
    justify="center",
)
print()
console.print(*menu, sep="\n", style="bold green", justify="center")
