def checkStraightLine(coordinates):
    firstX = coordinates[1][0] - coordinates[0][0]
    firstY = coordinates[1][1] - coordinates[0][1]
    for i in range(2, len(coordinates)):
        diffX = coordinates[i][0] - coordinates[i-1][0]
        diffY = coordinates[i][1] - coordinates[i-1][1]
        check = diffY*firstX - diffX*firstY
        if not check == 0:
            return False
    return True
