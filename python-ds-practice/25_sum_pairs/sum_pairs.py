def sum_pairs(nums, goal):
    num_set = set()
    for i, num in enumerate(nums):
        complement = goal - num
        if complement in num_set:
            return (complement, num)
        num_set.add(num)
    return ()