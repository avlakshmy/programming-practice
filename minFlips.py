def isZeroMatrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] != 0:
                return False
    return True

def flip(mat, i, j):
    rows = len(mat)
    cols = len(mat[0])
    mat[i][j] = 1 - mat[i][j]
    if i+1 <= rows-1:
        mat[i+1][j] = 1 - mat[i+1][j]
    if j+1 <= cols-1:
        mat[i][j+1] = 1 - mat[i][j+1]
    if i-1 >= 0:
        mat[i-1][j] = 1 - mat[i-1][j]
    if j-1 >= 0:
        mat[i][j-1] = 1 - mat[i][j-1]

def minFlips(mat):
    m = len(mat)
    n = len(mat[0])
    minFlipsCount = m*n + 1
    locns = [[i,j] for i in range(m) for j in range(n)]
    combos = [[int(x) for x in list(bin(i)[2:].zfill(m*n))] for i in range(1 << (m*n))]
    for combo in combos:
        mat2 = [row[:] for row in mat]
        for i in range(m*n):
            if combo[i] == 1:
                flip(mat2, locns[i][0], locns[i][1])
        if isZeroMatrix(mat2):
            flips = combo.count(1)
            if flips < minFlipsCount:
                minFlipsCount = flips
    if minFlipsCount > m*n:
        return -1
    return minFlipsCount
