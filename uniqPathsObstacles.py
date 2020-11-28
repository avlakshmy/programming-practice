def uniquePathsWithObstacles(obstacleGrid):
    rows = len(obstacleGrid)
    cols = len(obstacleGrid[0])
    numPaths = [[0 for _ in range(cols)] for _ in range(rows)]
    if obstacleGrid[0][0] == 1:
        return 0
    numPaths[0][0] = 1
    for i in range(1,rows):
        if obstacleGrid[i-1][0] == 0 and obstacleGrid[i][0] == 0:
            numPaths[i][0] = 1
        else:
            break
    for j in range(1,cols):
        if obstacleGrid[0][j-1] == 0 and obstacleGrid[0][j] == 0:
            numPaths[0][j] = 1
        else:
            break
    for i in range(1, rows):
        for j in range(1, cols):
            if obstacleGrid[i][j] == 0:
                numPaths[i][j] = numPaths[i-1][j] + numPaths[i][j-1]

    return numPaths[rows-1][cols-1]
