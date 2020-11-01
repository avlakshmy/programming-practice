def furthestBuilding(heights, bricks, ladders):
    diff = []
    for i in range(1, len(heights)):
        if heights[i-1] < heights[i]:
            diff.append(heights[i] - heights[i-1])
    diff.sort()
    brickcases = []
    count = 0
    i = 0
    while i < len(diff):
        count += diff[i]
        if count > bricks:
            break
        brickcases.append(diff[i])
        i += 1
    # print(brickcases)
    if len(brickcases) > 0:
        brickmax = brickcases[-1]
    else:
        brickmax = 0
    curr = 0
    while curr < len(heights) - 1:
        if heights[curr] >= heights[curr+1]:
            curr += 1
        else:
            difference = heights[curr+1] - heights[curr]
            if difference <= brickmax:
                if bricks >= difference:
                    bricks -= difference
                    curr += 1
                elif ladders >= 1:
                    ladders -= 1
                    curr += 1
                else:
                    break
            else:
                if ladders >= 1:
                    ladders -= 1
                    curr += 1
                elif bricks >= difference:
                    bricks -= difference
                    curr += 1
                else:
                    break
    return curr
