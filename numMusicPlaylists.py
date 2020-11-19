def numMusicPlaylists(N, L, K):
    dp = [[0 for _ in range(N+1)] for _ in range(L+1)]
    dp[1][1] = 1
    for i in range(2, L+1):
        for j in range(1, N+1):
            if j <= i:
                dp[i][j] += dp[i-1][j-1]*j
            if i > K:
                dp[i][j] += dp[i-1][j]*(j-K)
    return dp[L][N] % 1000000007
