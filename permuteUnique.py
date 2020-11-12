def permuteUnique(nums):
    n = len(nums)
    if n == 1:
        return [nums]
    if n == 2:
        if nums == nums[::-1]:
            return [nums]
        return [nums, nums[::-1]]
    ans = set()
    for num in nums:
        temparr = nums[:]
        temparr.remove(num)
        perms = self.permuteUnique(temparr)
        arr = [tuple([num] + x) for x in perms]
        for a in arr:
            ans.add(a)
    return [list(x) for x in ans]
