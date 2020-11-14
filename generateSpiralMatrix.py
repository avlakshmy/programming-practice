def generateMatrix(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    values = list(range(1, n*n + 1))
    k = 0

    i = 0
    j = 0

    layer = 0

    while k < n*n:
        while k < n*n and j < n-layer:
            matrix[i][j] = values[k]
            k += 1
            j += 1

        j -= 1
        i += 1

        while k < n*n and i < n-layer:
            matrix[i][j] = values[k]
            k += 1
            i += 1

        i -= 1
        j -= 1

        while k < n*n and j >= layer:
            matrix[i][j] = values[k]
            k += 1
            j -= 1

        j += 1
        i -= 1

        while k < n*n and i > layer:
            matrix[i][j] = values[k]
            k += 1
            i -= 1

        i += 1
        j += 1

        layer += 1

    return matrix
