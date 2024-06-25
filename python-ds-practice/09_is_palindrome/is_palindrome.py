def is_palindrome(phrase):
    cleaned_phrase = ''.join(c for c in phrase if c.isalnum()).lower()
    
    return cleaned_phrase == cleaned_phrase[::-1]