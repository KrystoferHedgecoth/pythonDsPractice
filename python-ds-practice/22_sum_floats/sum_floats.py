def sum_floats(nums):
    total = 0 

    for num in nums:
        if isinstance(num, float):
            total += num  

    return total