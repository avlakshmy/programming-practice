def getWinner(arr, k):
    currWinner = arr[0]
    currRounds = 0
    maxVal = max(arr)
    while currRounds < k:
        if currWinner == maxVal:
            return maxVal
        if arr[0] > arr[1]:
            currRounds += 1
            temp = arr[1]
            arr.remove(temp)
            arr.append(temp)
        else:
            currWinner = arr[1]
            currRounds = 1
            temp = arr[0]
            arr.remove(temp)
            arr.append(temp)
    return currWinner
