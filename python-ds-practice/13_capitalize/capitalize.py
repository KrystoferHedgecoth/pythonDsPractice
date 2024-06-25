def capitalize(phrase):
    words = phrase.split()
    
    words[0] = words[0].lower().capitalize() + words[1:]  # This effectively joins the first word with the rest
    
    result = ' '.join(words)
    
    return result.lstrip()