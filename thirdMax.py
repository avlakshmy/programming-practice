import math
def thirdMax(nums):
    MININF = -math.inf
    largest = MININF
    secondLargest = MININF
    thirdLargest = MININF
    flag = 0
    for num in nums:
        if num > largest:
            thirdLargest = secondLargest
            secondLargest = largest
            largest = num
        elif num < largest and num > secondLargest:
            thirdLargest = secondLargest
            secondLargest = num
        elif num < secondLargest and num > thirdLargest:
            thirdLargest = num
            flag = 1
    if thirdLargest == MININF:
        return largest
    return thirdLargest
