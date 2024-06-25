def two_list_dictionary(keys, values):
    result = {key: value for key, value in zip(keys, values)}
    
    if len(keys) > len(values):
        for key in keys[len(values):]:
            result[key] = None
    
    return result