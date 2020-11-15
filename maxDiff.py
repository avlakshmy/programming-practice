def maxDiff(num):
    numList = [int(x) for x in str(num)]
    poss = set()
    for x in range(0,10):
        for y in range(0,10):
            a = numList[:]
            for i in range(len(a)):
                if a[i] == x:
                    a[i] = y
            newNum = ''.join([str(d) for d in a])
            if not newNum[0] == '0' and not int(newNum) == 0:
                poss.add(int(newNum))
    return max(poss) - min(poss)
