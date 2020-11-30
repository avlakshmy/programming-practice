def getHint(secret, guess):
    numBulls = 0
    secretIndicesGuessedCorrectly = []
    secretWrong = []
    guessWrong = []
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            secretIndicesGuessedCorrectly.append(i)
            numBulls += 1
        else:
            secretWrong.append(secret[i])
            guessWrong.append(guess[i])
    secretWrong.sort()
    guessWrong.sort()
    numCows = 0
    i = 0
    j = 0
    numWrong = len(secretWrong)
    while i < numWrong and j < numWrong:
        if secretWrong[i] == guessWrong[j]:
            i += 1
            j += 1
            numCows += 1
        elif secretWrong[i] < guessWrong[j]:
            i += 1
        else: # secretWrong[i] > guessWrong[j]
            j += 1
    return '{}A{}B'.format(numBulls, numCows)
