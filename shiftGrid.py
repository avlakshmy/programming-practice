def shiftGrid(grid, k):
    arr = []
    rows = len(grid)
    cols = len(grid[0])
    n = rows * cols
    if k%n == 0:
        return grid
    shift = k%n
    for i in range(rows):
        for j in range(cols):
            arr.append(grid[i][j])
    newarr = arr[-shift:] + arr[:-shift]
    for i in range(rows):
        for j in range(cols):
            grid[i][j] = newarr[(i*cols) + j]
    return grid
