def reconstructMatrix(upper, lower, colsum):
    cols = len(colsum)
    matrix = [[0 for _ in range(cols)] for _ in range(2)]
    for j in range(cols):
        if colsum[j] == 2:
            if upper >= 1 and lower >= 1:
                matrix[0][j] = 1
                matrix[1][j] = 1
                colsum[j] = 0
                upper -= 1
                lower -= 1
            else:
                return []
    for j in range(cols):
        if colsum[j] == 1:
            if upper >= 1:
                matrix[0][j] = 1
                colsum[j] = 0
                upper -= 1
            elif lower >= 1:
                matrix[1][j] = 1
                colsum[j] = 0
                lower -= 1
            else:
                return []
    if upper == 0 and lower == 0 and all([x == 0 for x in colsum]):
        return matrix
    return []
