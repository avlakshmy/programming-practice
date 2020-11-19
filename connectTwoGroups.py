import math
def connectTwoGroups(cost):
    size1 = len(cost)
    size2 = len(cost[0])
    dp = [[0 for _ in range(1 << size2)] for _ in range(size1+1)]

    transpose = list(zip(*cost))
    mincost = [min(row) for row in transpose]

    # base case
    for mask in range(1 << size2):
        ans = 0
        for j in range(size2):
            if mask & (1 << j) == 0: # not set
                ans += mincost[j]
        dp[size1][mask] = ans

    for i in range(size1-1, -1, -1):
        for mask in range(1 << size2):
            ans = math.inf
            for j in range(size2):
                ans = min(ans, cost[i-1][j] + dp[i+1][mask | (1<<j)])
            dp[i][mask] = ans
    return dp[0][0]    
