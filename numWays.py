def numWays(s):
    n = len(s)
    oneInd = []
    for i in range(n):
        if s[i] == '1':
            oneInd.append(i)
    if len(oneInd) == 0:
        return (((n-1)*(n-2))//2)%1000000007
    if len(oneInd) % 3 == 1 or len(oneInd) % 3 == 2:
        return 0
    numOnes = len(oneInd)//3
    firstPart = oneInd[:numOnes]
    secondPart = oneInd[numOnes:numOnes*2]
    thirdPart = oneInd[numOnes*2:]
    bet1n2 = secondPart[0] - firstPart[-1] - 1
    bet2n3 = thirdPart[0] - secondPart[-1] - 1
    return ((bet1n2 + 1)*(bet2n3 + 1))%1000000007
