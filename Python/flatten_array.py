def flatten(iterable):
    flattened = []
    for item in iterable:
        if isinstance(item, int):
            flattened.append(item)
        elif isinstance(item, list):
            flattened += flatten(item)
        else:
            continue
    return flattened