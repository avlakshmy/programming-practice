def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
    if len(envelopes) == 0:
        return 0
       
    # sort in increasing order of widths, decreasing order of heights
    envelopes.sort(key = lambda x: (x[0], -x[1])) 

    # apply longest increasing subsequence with respect to heights
    dp = [1]
    for i in range(1, len(envelopes)):
        ans = 0
        for j in range(i):
            if envelopes[i][1] > envelopes[j][1]:
                ans = max(ans, dp[j])
        dp.append(ans + 1)
    return max(dp)
