def trap(height):
    if len(height) == 0:
        return 0
    maxSoFar = [height[0]]
    for i in range(1, len(height)):
        maxSoFar.append(max(maxSoFar[-1], height[i]))

    rheight = height[::-1]
    rmaxSoFar = [rheight[0]]
    for i in range(1, len(rheight)):
        rmaxSoFar.append(max(rmaxSoFar[-1], rheight[i]))
    rmaxSoFar[:] = rmaxSoFar[::-1]

    water = 0
    i = 0
    while i < len(height):
        j = i+1
        while j < len(height) and maxSoFar[j] == maxSoFar[i]:
            j += 1
        if j < len(height):
            start = i+1
            end = j-1
            for k in range(start, end+1):
                water += (maxSoFar[i] - height[k])
        else:
            start = i+1
            end = len(height)-1
            for k in range(start, end+1):
                water += (rmaxSoFar[k] - height[k])

        i = j

    return water
