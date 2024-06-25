def frequency(lst, search_term):
    """Return frequency of term in lst."""
    
    count = 0
    
    for item in lst:
        if item == search_term:
            count += 1
            
    return count