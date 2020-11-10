def imageSmoother(M):
    rows = len(M)
    cols = len(M[0])
    smoothM = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            smoothM[i][j] += M[i][j]
            count = 1
            if j >= 1:
                smoothM[i][j] += M[i][j-1]
                count += 1
            if j <= cols-2:
                smoothM[i][j] += M[i][j+1]
                count += 1
            if i >= 1:
                smoothM[i][j] += M[i-1][j]
                count += 1
                if j >= 1:
                    smoothM[i][j] += M[i-1][j-1]
                    count += 1
                if j <= cols-2:
                    smoothM[i][j] += M[i-1][j+1]
                    count += 1
            if i <= rows-2:
                smoothM[i][j] += M[i+1][j]
                count += 1
                if j >= 1:
                    smoothM[i][j] += M[i+1][j-1]
                    count += 1
                if j <= cols-2:
                    smoothM[i][j] += M[i+1][j+1]
                    count += 1
            smoothM[i][j] = smoothM[i][j]//count
    return smoothM
