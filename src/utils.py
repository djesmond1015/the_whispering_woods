def destructure(dictionary, *keys):
    return [dictionary[k] if k in dictionary else None for k in keys]


def formatted_datetime(datetime_obj):
    return datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
