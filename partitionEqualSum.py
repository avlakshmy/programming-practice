def subsetSum(w, arr):
    n = len(arr)
    dp = [[False for _ in range(w+1)] for _ in range(n+1)]
    
    for i in range(n + 1):
        dp[i][0] = True
         
    for j in range(1, w + 1):
        dp[0][j]= False
             
    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if j < arr[i-1]:
                dp[i][j] = dp[i-1][j]
            if j >= arr[i-1]:
                dp[i][j] = (dp[i-1][j] or dp[i - 1][j - arr[i-1]])
     
    return dp[n][w]

def canPartition(nums):
    totSum = sum(nums)
    if totSum % 2 == 1:
        return False
    halfSum = totSum // 2 
    return subsetSum(halfSum, nums)
