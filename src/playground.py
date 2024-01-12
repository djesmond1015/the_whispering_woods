# from rich.table import Table, Column
# from rich.panel import Panel
# from rich.console import Console
# from rich import box

# console = Console()

# Export feature
# data such as the game state, and dataset can be exported to a file
# the data can be exported to a csv file and json file
# the exported file will be downloaded to the user's local machine
# for Windows, the file will be downloaded to the Downloads folder
# for Mac, the file will be downloaded to the Desktop folder
# for Linux, the file will be downloaded to the Home folder

# TODO: give a meaningful file name (timestamp?)
# TODO: how to implement in the frontend
# the file name will be the current date and time


# Sample data

import os, json
from pathlib import Path
from dataset import scenes
from enum import Enum


from controllers import GameStateController

gs = GameStateController()
data = gs.retrieve_multiple_data()


# get the path of the Downloads folder for Windows
def get_download_path_windows():
    import winreg

    sub_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders"

    downloads_guid = "{374DE290-123F-4565-9164-39C4925E467B}"
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
        location = winreg.QueryValueEx(key, downloads_guid)[0]
    return location


# get the path of the Downloads folder for Mac
def get_download_path_mac():
    location = os.path.join(Path.home(), "Desktop")
    return location


def convert_enum_to_str(data):
    if isinstance(data, Enum):
        return data.value
    elif isinstance(data, list):
        return [convert_enum_to_str(item) for item in data]
    elif isinstance(data, dict):
        return {
            convert_enum_to_str(key): convert_enum_to_str(value)
            for key, value in data.items()
        }
    else:
        return data


def convert_datetime_to_isoformat(data):
    from datetime import datetime

    if isinstance(data, datetime):
        return data.isoformat()
    elif isinstance(data, list):
        return [convert_datetime_to_isoformat(item) for item in data]
    elif isinstance(data, dict):
        return {
            convert_datetime_to_isoformat(key): convert_datetime_to_isoformat(value)
            for key, value in data.items()
        }
    else:
        return data


def create_file(file_name, file_format):
    try:
        return os.path.join(get_download_path_windows(), f"{file_name}.{file_format}")
    except:
        return os.path.join(get_download_path_mac(), f"{file_name}.{file_format}")


def export_data(data, file_name, file_format):
    converted_data = convert_enum_to_str(data)
    converted_data = convert_datetime_to_isoformat(converted_data)

    file_path = create_file(file_name, file_format)

    if file_format == "json":
        with open(file_path, "w") as f:
            json.dump(converted_data, f, indent=2)
    elif file_format == "txt":
        with open(file_path, "w") as f:
            f.write(str(converted_data))
    else:
        raise ValueError("Invalid file format, please choose from json or txt")

    print(f"Data exported to {file_path}")


export_data(scenes, "backup-data", "txt")
export_data(data, "game-state", "json")
