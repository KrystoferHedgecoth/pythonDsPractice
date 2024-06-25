def sum_range(nums, start=0, end=None):
    if end is None:
        end = len(nums)
    
    actual_start = max(0, start)
    actual_end = min(len(nums), end)
    
    return sum(nums[actual_start:actual_end])