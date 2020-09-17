def ncr(n, r):
    dp = [[0 for j in range(r+1)] for i in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    for j in range(r+1):
        dp[0][j] = 1
    dp[0][0] = 0
    for i in range(1, n+1):
        for j in range(1, r+1):
            if j <= i:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

    return dp[n][r]

T = int(input())
for _ in range(T):
    N = int(input())
    print(ncr(2*N, N)//(N+1))
