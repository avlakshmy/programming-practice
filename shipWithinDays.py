def canShip(weights, capacity, D):
    daysNeeded = 1
    currWeight = 0
    for w in weights:
        currWeight += w
        if currWeight > capacity:
            daysNeeded += 1
            currWeight = w
    if daysNeeded <= D:
        return True
    return False

def shipWithinDays(weights, D):
    low = max(weights)
    high = sum(weights)

    while low < high:
        mid = low + (high - low) // 2
        if canShip(weights, mid, D):
            high = mid
        else:
            low = mid + 1

    return high
