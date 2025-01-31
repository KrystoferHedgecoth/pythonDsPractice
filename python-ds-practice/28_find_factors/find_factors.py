def find_factors(num):
    factors = []
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            factors.extend([i, num // i])
    
    factors.sort()
    
    return factors