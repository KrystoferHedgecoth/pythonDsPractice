def min_max_keys(d):
    keys = (k for k in d.keys())
    
    min_key = min(keys)
    max_key = max(keys)
    
    return min_key, max_key