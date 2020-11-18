def longestCommonSubsequence(word1, word2):
    M = len(word1)
    N = len(word2)

    if M == 0 and N == 0:
        return 0

    lcs = [[0 for _ in range(N+1)] for _ in range(M+1)]

    for i in range(1, M+1):
        for j in range(1, N+1):
            if word1[i-1] == word2[j-1]:
                lcs[i][j] = lcs[i-1][j-1] + 1
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1], lcs[i-1][j-1])

    return lcs[-1][-1]
