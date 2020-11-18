def minimumDeleteSum(word1, word2):
    M = len(word1)
    N = len(word2)

    if M == 0 and N == 0:
        return 0

    score = [[0 for _ in range(N+1)] for _ in range(M+1)]

    for j in range(N-1, -1, -1):
        score[M][j] = score[M][j+1] + ord(word2[j])

    for i in range(M-1, -1, -1):
        score[i][N] = score[i+1][N] + ord(word1[i])

    for i in range(M-1, -1, -1):
        for j in range(N-1, -1, -1):
            if word1[i] == word2[j]:
                score[i][j] = score[i+1][j+1]
            else:
                score[i][j] = min(score[i+1][j] + ord(word1[i]), score[i][j+1] + ord(word2[j]))

    return score[0][0]
