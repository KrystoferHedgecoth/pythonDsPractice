def friend_date(a, b):
    a_hobbies = set(a[2])  # Convert list to set for efficient comparison
    b_hobbies = set(b[2])
    
    if a_hobbies.intersection(b_hobbies):
        return True
    else:
        return False