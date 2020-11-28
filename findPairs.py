def findPairs(nums, k):
    if len(nums) == 0:
        return 0
    if k == 0:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        vals = [val for val in freq.values() if val >= 2]
        return len(vals)
    pairs = set()
    for i in range(len(nums)-1):
        num = nums[i]
        poss1 = num+k
        if poss1 in nums[i+1:]:
            if poss1 < num:
                ans = (poss1, num)
            else:
                ans = (num, poss1)
            pairs.add(ans)
        poss2 = num-k
        if poss2 in nums[i+1:]:
            if poss2 < num:
                ans = (poss2, num)
            else:
                ans = (num, poss2)
            pairs.add(ans)
    return len(pairs)
