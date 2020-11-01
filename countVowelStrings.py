def countVowelStrings(n):
    dp = [[0 for _ in range(n+1)] for _ in range(6)]
    for j in range(1, n+1):
        dp[1][j] = 1
    for i in range(1, 6):
        dp[i][1] = i
    for i in range(2, 6):
        for j in range(2, n+1):
            dp[i][j] = dp[i][j-1] + dp[i-1][j]
    return dp[5][n]
