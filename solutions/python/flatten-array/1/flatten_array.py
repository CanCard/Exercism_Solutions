def mlatten(iterable):
    result = []
    for item in iterable:
        if isinstance(item, list) and item is not None:
            result.extend(mlatten(item))
        elif item is not None:
            result.append(item)
    return result

def flatten(iterable):
    return mlatten(iterable)