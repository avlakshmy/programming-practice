def numIdenticalPairs(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    count = 0
    for num,n in freq.items():
        if n >= 2:
            count += ((n*(n-1))//2)
    return count
