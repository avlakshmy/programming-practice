def productExceptSelf(nums):
    n = len(nums)
    lproducts = [1 for _ in range(n)]
    rproducts = [1 for _ in range(n)]
    for i in range(1, len(nums)):
        lproducts[i] = lproducts[i-1] * nums[i-1]
    for i in range(len(nums)-2, -1, -1):
        rproducts[i] = rproducts[i+1] * nums[i+1]
    ans = []
    for i in range(n):
        ans.append(lproducts[i] * rproducts[i])
    return ans
