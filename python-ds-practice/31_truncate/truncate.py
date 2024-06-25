def truncate(phrase, n):
    if n < 3:
        return 'Truncation must be at least 3 characters.'
    
    if len(phrase) <= n:
        return phrase
    
    return phrase[:n] + '...'