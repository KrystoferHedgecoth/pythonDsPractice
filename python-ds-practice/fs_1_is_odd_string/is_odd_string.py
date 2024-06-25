def is_odd_string(word):
    total = 0
    for char in word:
        if char.islower():
            total += ord(char) - 96
        elif char.isupper():
            total += ord(char) - 64
    return total % 2 == 1