# This is the module that contains all the helper or utility functions that are used across multiple parts of the application.
# This can keep the code organized by grouping together functions that don't fit neatly into a specific module or class but are still used in various places throughout the application.
# Besides that, this can prevent the code from being duplicated. (DRY - Don't Repeat Yourself)


from datetime import datetime, timedelta


# Destructure dictionary to get the values of the particular keys
# This is the same as the javascript object destructuring
# By doing so, this can archive immutability of the data and get the necessary data from the dictionary.
# More info of object destructuring: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment#object_destructuring
def destructure(dictionary: dict, *keys) -> list:
    return [dictionary[k] if k in dictionary else None for k in keys]


# Convert datetime to string with format YYYY-MM-DD HH:MM:SS
def formatted_datetime(datetime_obj: datetime) -> str:
    return datetime_obj.strftime("%Y-%m-%d %H:%M:%S")


# Convert formatted datetime to timedelta
def formatted_datetime_to_timedelta(formatted_datetime: str) -> timedelta:
    try:
        return datetime.strptime(formatted_datetime, "%H:%M:%S") - datetime.strptime(
            "00:00:00", "%H:%M:%S"
        )
    except Exception as e:
        print("[formatted_datetime_to_timedelta error]")
        print(e)
        return


# Truncate the name to 10 characters if the name is longer than 10 characters
def truncate_name(name):
    truncated_name = ""

    if len(name) > 10:
        truncated_name = name[:10] + "..."
    else:
        truncated_name = name

    return truncated_name
