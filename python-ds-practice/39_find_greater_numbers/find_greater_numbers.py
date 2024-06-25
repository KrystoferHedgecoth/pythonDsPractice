def find_greater_numbers(nums):
    count = 0
    
    if len(nums) == 0:
        return 0
    
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            count += 1
    
    return count