def restoreMatrix(rowSum, colSum):
    rows = len(rowSum)
    cols = len(colSum)
    matrix = [[-1 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == -1:
                r = rowSum[i]
                c = colSum[j]
                if r < c:
                    matrix[i][j] = r
                    rowSum[i] -= r
                    colSum[j] -= r
                    k = j+1
                    while k < cols:
                        matrix[i][k] = 0
                        k += 1
                else:
                    matrix[i][j] = c
                    rowSum[i] -= c
                    colSum[j] -= c
                    k = i+1
                    while k < rows:
                        matrix[k][j] = 0
                        k += 1
    return matrix
