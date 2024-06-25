def compact(lst):
    """Return a copy of lst with non-true elements removed."""
    return [item for item in lst if bool(item)]