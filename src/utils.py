from datetime import datetime, timedelta


def destructure(dictionary, *keys):
    return [dictionary[k] if k in dictionary else None for k in keys]


def formatted_datetime(datetime_obj):
    return datetime_obj.strftime("%Y-%m-%d %H:%M:%S")


# convert string 00:02:08 to timedelta
def formatted_datetime_to_timedelta(formatted_datetime) -> timedelta:
    try:
        return datetime.strptime(formatted_datetime, "%H:%M:%S") - datetime.strptime(
            "00:00:00", "%H:%M:%S"
        )
    except Exception as e:
        print("[formatted_datetime_to_timedelta error]")
        print(e)
        return
