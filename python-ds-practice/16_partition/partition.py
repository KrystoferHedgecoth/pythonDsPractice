def partition(lst, fn):
    true_list = []
    false_list = []

    for item in lst:
        if fn(item):
            true_list.append(item)
        else:
            false_list.append(item)

    return [true_list, false_list]