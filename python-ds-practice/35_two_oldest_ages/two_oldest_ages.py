def two_oldest_ages(ages):
    sorted_ages = sorted(ages, reverse=True)
    
    return (sorted_ages[1], sorted_ages[0])  