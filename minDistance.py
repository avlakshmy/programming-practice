def minDistance(word1, word2):
    M = len(word1)
    N = len(word2)

    if M == 0 and N == 0:
        return 0

    score = [[0 for _ in range(N+1)] for _ in range(M+1)]
    
    for j in range(N+1):
        score[0][j] = j

    for i in range(M+1):
        score[i][0] = i

    for i in range(1, M+1):
        for j in range(1, N+1):
            if word1[i-1] == word2[j-1]:
                cost = score[i-1][j-1]
            else:
                cost = score[i-1][j-1] + 2
            score[i][j] = min(score[i][j-1]+1, score[i-1][j]+1, cost)

    return score[-1][-1]
