import math
def updateMatrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    cost = [[math.inf for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                cost[i][j] = 0

    for i in range(0,rows):
        for j in range(0,cols):
            options = [math.inf]
            if i >= 1:
                options.append(cost[i-1][j])
            if j >= 1:
                options.append(cost[i][j-1])
            cost[i][j] = min(cost[i][j], min(options) + 1)

    for i in range(rows-1,-1,-1):
        for j in range(cols-1,-1,-1):
            options = [math.inf]
            if i <= rows-2:
                options.append(cost[i+1][j])
            if j <= cols-2:
                options.append(cost[i][j+1])
            cost[i][j] = min(cost[i][j], min(options) + 1)

    return cost
