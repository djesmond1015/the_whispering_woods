# This is the module handle export functionality of the application.

import json
import os
from pathlib import Path
from enum import Enum


class Exporter:
    def __init__(self):
        pass

    # Get the path of the Downloads folder for Windows using Windows Registry (winreg) module
    # More info: https://stackoverflow.com/questions/35851281/python-get-path-to-downloads-folder-windows
    def get_download_path_windows(self):
        import winreg

        sub_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders"

        downloads_guid = "{374DE290-123F-4565-9164-39C4925E467B}"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location

    # Get the path of the Downloads folder for Mac
    # More info: https://stackoverflow.com/questions/40295823/how-to-get-the-downloads-folder-in-python
    def get_download_path_mac(self):
        location = os.path.join(Path.home(), "Desktop") or os.path.join(
            os.path.expanduser("~"), "downloads"
        )
        return location

    # Two convert functions below are used to convert data to the appropriate format before exporting the data to a file.

    # Convert enum to string
    def convert_enum_to_str(self, data):
        if isinstance(data, Enum):
            return data.value
        elif isinstance(data, list):
            return [self.convert_enum_to_str(item) for item in data]
        elif isinstance(data, dict):
            return {
                self.convert_enum_to_str(key): self.convert_enum_to_str(value)
                for key, value in data.items()
            }
        else:
            return data

    # Convert datetime to isoformat
    def convert_datetime_to_isoformat(self, data):
        from datetime import datetime

        if isinstance(data, datetime):
            return data.isoformat()
        elif isinstance(data, list):
            return [self.convert_datetime_to_isoformat(item) for item in data]
        elif isinstance(data, dict):
            return {
                self.convert_datetime_to_isoformat(
                    key
                ): self.convert_datetime_to_isoformat(value)
                for key, value in data.items()
            }
        else:
            return data

    # After converting the data to the appropriate format, the data will be exported which is handled by the export_data function and create_file function.

    # Create file path for the exported file
    def create_file(self, file_name, file_format):
        try:
            return os.path.join(
                self.get_download_path_windows(), f"{file_name}.{file_format}"
            )
        except:
            return os.path.join(
                self.get_download_path_mac(), f"{file_name}.{file_format}"
            )

    # Main function to export data to a file
    def export_data(self, data, file_name, file_format):
        converted_data = self.convert_enum_to_str(data)
        converted_data = self.convert_datetime_to_isoformat(converted_data)

        file_path = self.create_file(file_name, file_format)

        if file_format == "json":
            with open(file_path, "w") as f:
                json.dump(converted_data, f, indent=2)
        elif file_format == "txt":
            with open(file_path, "w") as f:
                f.write(str(converted_data))
        else:
            raise ValueError("Invalid file format, please choose from json or txt")

        print(f"Data exported to {file_path}")
