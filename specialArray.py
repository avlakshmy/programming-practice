def specialArray(nums):
    nums.sort()
    maxval = max(nums)
    counts = [0 for _ in range(maxval+1)]
    for i in range(len(nums)):
        counts[nums[i]] += 1
    last = counts[-1]
    j = maxval - 1
    while j >= 0:
        counts[j] += last
        last = counts[j]
        j -= 1
    for i in range(maxval+1):
        if counts[i] == i:
            return i
    return -1
        
