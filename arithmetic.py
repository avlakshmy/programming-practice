T = int(input())
for i in range(T):
    N = int(input())
    arr = [int(x) for x in input().split()]
    if N < 2:
        lenArith = 0
    else:
        dp = [0 for j in range(N)]
        dp[0] = 0
        dp[1] = 2
        for j in range(2,N):
            if arr[j] - arr[j-1] == arr[j-1] - arr[j-2]:
                dp[j] = dp[j-1] + 1
            else:
                dp[j] = 2
        lenArith = max(dp)
    print('Case #{}: {}'.format(i+1, lenArith))
