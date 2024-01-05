def destructure(array, *keys):
    return [array[k] if k in array else None for k in keys]
