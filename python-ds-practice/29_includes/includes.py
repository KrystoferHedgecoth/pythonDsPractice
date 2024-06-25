def includes(collection, sought, start=None):
    if isinstance(collection, dict):
        return sought in collection
    elif isinstance(collection, (list, str, tuple)):
        if start is not None:
            collection = collection[start:]
        return sought in collection
    elif isinstance(collection, set):
        return sought in collection
    else:
        raise TypeError(f"Unsupported collection type: {type(collection)}")