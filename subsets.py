def subsets(nums):
    n = len(nums)
    combos = (1<<n)
    bins = [bin(i)[2:] for i in range(combos)]
    for i in range(len(bins)):
        if len(bins[i]) < n:
            bins[i] = ("0"*(n-len(bins[i]))) + bins[i]
    ans = []
    for comb in bins:
        arr = []
        for j in range(len(comb)):
            if comb[j] == '1':
                arr.append(nums[j])
        ans.append(arr)

    return ans
