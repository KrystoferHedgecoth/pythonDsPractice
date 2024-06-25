def titleize(phrase):
    words = phrase.split()
    
    capitalized_words = [word.capitalize() for word in words]
    
    result = ''.join(capitalized_words)
    
    return result