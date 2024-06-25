def mode(nums):
    counts = {}
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    max_count = max(counts.values())

    modes = [num for num, count in counts.items() if count == max_count]

    return modes[0]