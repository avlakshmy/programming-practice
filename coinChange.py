def ways(n, coins):
    m = len(coins)
    dp = [[0 for _ in range(n+1)] for _ in range(m)]
    for i in range(m):
        dp[i][0] = 1
    for j in range(1,n+1):
        if j%coins[0] == 0:
            dp[0][j] = 1
    for i in range(1,m):
        for j in range(n+1):
            val = dp[i-1][j]
            if j >= coins[i]:
                val += dp[i][j-coins[i]]
            dp[i][j] = val
    return dp[m-1][n]
