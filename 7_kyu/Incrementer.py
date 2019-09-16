def incrementer(nums):
    return [(nums[i] + i + 1) % 10 for i in range(0,len(nums))]