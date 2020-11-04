def optimalTime(pointA, pointB):
    # move diagonally as far as possible, then move straight up or to the side
    x1 = pointA[0]
    y1 = pointA[1]
    x2 = pointB[0]
    y2 = pointB[1]
    if x1 > x2:
        x1,y1,x2,y2 = x2,y2,x1,y1
    # (x1,y1) is to the left of (x2,y2)
    count = 0
    if y1 < y2:
        while x1 < x2 and y1 < y2:
            x1 += 1
            y1 += 1
            count += 1
        if x1 == x2:
            count = count + (y2-y1)
        else:
            count = count + (x2-x1)
    else:
        while x1 < x2 and y1 > y2:
            x1 += 1
            y1 -= 1
            count += 1
        if x1 == x2:
            count = count + (y1-y2)
        else:
            count = count + (x2-x1)
    return count

def minTimeToVisitAllPoints(points):
    count = 0
    for i in range(len(points)-1):
        count += optimalTime(points[i], points[i+1])
    return count
