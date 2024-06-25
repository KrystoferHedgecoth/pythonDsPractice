def vowel_count(phrase):
    vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    lower_phrase = phrase.lower()

    for char in lower_phrase:
        if char in vowel_counts:
            vowel_counts[char] += 1

    return vowel_counts