def maxProduct(nums):
    ans = nums[0]
    prevMaxProd = nums[0]
    prevMinProd = nums[0]
    currMaxProd = nums[0]
    currMinProd = nums[0]
    for i in range(1, len(nums)):
        currMaxProd = max(prevMaxProd*nums[i], prevMinProd*nums[i], nums[i])
        currMinProd = min(prevMaxProd*nums[i], prevMinProd*nums[i], nums[i])
        ans = max(ans, currMaxProd)
        prevMaxProd = currMaxProd
        prevMinProd = currMinProd
    return ans
