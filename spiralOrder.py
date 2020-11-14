def spiralOrder(matrix):
    if matrix == []:
        return []
    if matrix == [[]]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    if cols == 0:
        return []

    if rows == 1:
        return matrix[0]
    if cols == 1:
        ans = []
        for row in matrix:
            ans.append(row[0])
        return ans

    ans = []
    # top row
    for j in range(cols):
        ans.append(matrix[0][j])
    for i in range(1, rows):
        ans.append(matrix[i][cols-1])
    for j in range(cols-2, -1, -1):
        ans.append(matrix[rows-1][j])
    for i in range(rows-2, 0, -1):
        ans.append(matrix[i][0])

    submatrix = [[matrix[i][j] for j in range(1, cols-1)] for i in range(1, rows-1)]
    ans.extend(self.spiralOrder(submatrix))

    return ans
