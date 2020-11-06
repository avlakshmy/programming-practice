def numberOfSets(n, k):
    # (n+k-1)C(2*k)
    MOD = 1000000007        
    dp = [[0 for _ in range(2*k+1)] for _ in range(n+k)]
    for i in range(n+k):
        dp[i][0] = 1
    for j in range(2*k+1):
        dp[0][j] = 1
    dp[0][0] = 0
    for i in range(1, n+k):
        for j in range(1, 2*k + 1):
            if j <= i:
                dp[i][j] = (dp[i-1][j] + dp[i-1][j-1])
    return (dp[n+k-1][2*k] % MOD)
