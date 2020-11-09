def numWaterBottles(numBottles, numExchange):
    count = 0
    numFillBottles = numBottles
    numEmptyBottles = 0
    while numFillBottles > 0:
        # drink operation
        count += numFillBottles
        numEmptyBottles += numFillBottles
        numFillBottles = 0

        # exchange operation
        numFillBottles = numEmptyBottles//numExchange 
        numEmptyBottles = numEmptyBottles%numExchange

    count += numFillBottles
    return count
