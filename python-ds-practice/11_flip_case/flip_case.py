def flip_case(phrase, to_swap):
    result = ""
    for char in phrase:
        if char.lower() == to_swap.lower():
            if char.isupper():
                result += char.lower()
            else:
                result += char.upper()
        else:
            result += char
    return result