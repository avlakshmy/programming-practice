def orientation(p, q, r):
    val = (q[1] - p[1])*(r[0] - q[0]) - (q[0] - p[0])*(r[1] - q[1])
    if val > 0:
        return 1 
    if val < 0:
        return 2
    return 0

def findLeftmostIndex(points):
    ind = 0
    for i in range(1, len(points)):
        if points[i][0] < points[ind][0]:
            ind = i
        elif points[i][0] == points[ind][0] and points[i][1] > points[ind][1]:
            ind = i
    return ind

def distance_sq(p, q):
    return (p[0] - q[0])*(p[0] - q[0]) + (p[1] - q[1])*(p[1] - q[1])

def outerTrees(points):
    # find convex hull of the tree coordinates
    points = [tuple(x) for x in points]

    n = len(points)
    if n < 3:
        return points

    convexHull = []
    l = findLeftmostIndex(points)
    p = l
    while True:
        convexHull.append(p)
        q = (p+1) % n
        for i in range(n):
            ori = orientation(points[p], points[i], points[q])
            if ori == 2 or (ori == 0 and distance_sq(points[i], points[p]) > distance_sq(points[q], points[p])):
                q = i
        p = q
        if p == l:
            break
    convexHull = [points[p] for p in convexHull]
    for point in points:
        if not point in convexHull:
            flag = -1
            for i in range(len(convexHull)):
                if not point == convexHull[i] and not point == convexHull[(i+1)%len(convexHull)] and orientation(convexHull[i], point, convexHull[(i+1)%len(convexHull)]) == 0:
                    flag = (i+1)%len(convexHull)
                    break
            if flag > -1:
                convexHull.insert(flag, point)
    return [list(x) for x in convexHull]
