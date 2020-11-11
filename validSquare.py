def validSquare(p1, p2, p3, p4):
    d1 = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    d2 = math.sqrt((p2[0] - p3[0])**2 + (p2[1] - p3[1])**2)
    d3 = math.sqrt((p3[0] - p4[0])**2 + (p3[1] - p4[1])**2)
    d4 = math.sqrt((p4[0] - p1[0])**2 + (p4[1] - p1[1])**2)
    d5 = math.sqrt((p1[0] - p3[0])**2 + (p1[1] - p3[1])**2)
    d6 = math.sqrt((p2[0] - p4[0])**2 + (p2[1] - p4[1])**2)
    dist = [d1, d2, d3, d4, d5, d6]
    dist.sort()
    allSidesEqual = (dist[0] == dist[1] and dist[0] == dist[2] and dist[0] == dist[3])
    bothDiagonalsEqual = (dist[4] == dist[5])
    sideNotEqualToDiagonal = (not dist[0] == dist[4])
    diagonalToSideRatioTrue = (round(dist[4]*dist[4]) == round(2*dist[0]*dist[0]))
    if allSidesEqual and bothDiagonalsEqual and sideNotEqualToDiagonal and diagonalToSideRatioTrue:
        return True
    return False
