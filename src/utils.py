def destructure(array, *keys):
    return [array[k] if k in array else None for k in keys]


def formatted_datetime(datetime_obj):
    return datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
