def multiple_letter_count(phrase):
    letter_counts = {}
    
    lower_phrase = phrase.lower()
    
    for char in lower_phrase:
        if char.isalpha():
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    
    return letter_counts