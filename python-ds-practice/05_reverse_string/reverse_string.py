def reverse_string(phrase):
    char_list = list(phrase)
    
    reversed_char_list = char_list[::-1]
    
    reversed_phrase = ''.join(reversed_char_list)
    
    return reversed_phrase