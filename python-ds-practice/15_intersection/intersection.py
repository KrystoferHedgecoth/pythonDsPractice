def intersection(l1, l2):
    set_l1 = set(l1)
    set_l2 = set(l2)
    
    intersection_set = set_l1 & set_l2
    
    return list(intersection_set)