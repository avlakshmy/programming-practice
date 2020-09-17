def LCSstr(X, Y, n, m):
    dp = [[0 for j in range(m+1)] for i in range(n+1)]
    maxlcs = 0
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif (X[i-1] == Y[j-1]): 
                dp[i][j] = dp[i-1][j-1] + 1
                maxlcs = max(maxlcs, dp[i][j]) 
            else: 
                dp[i][j] = 0
    return maxlcs

T = int(input())
for _ in range(T):
    nm = [int(x) for x in input().split()]
    n = nm[0]
    m = nm[1]
    X = list(input())
    Y = list(input())
    print(LCSstr(X, Y, n, m))
