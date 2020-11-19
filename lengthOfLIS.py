def lengthOfLIS(nums):
    if len(nums) == 0:
        return 0
    dp = [1]
    for i in range(1, len(nums)):
        ans = 0
        for j in range(i):
            if nums[i] > nums[j]:
                ans = max(ans, dp[j])
        dp.append(ans + 1)
    return max(dp)
