def repeat(phrase, num):
    if not isinstance(num, int):
        return None
    
    num_str = str(num)
    
    repeated_phrase = phrase * num_str
    
    if num == 0:
        return ''
    
    return repeated_phrase