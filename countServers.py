def countServers(grid):
    rows = len(grid)
    cols = len(grid[0])
    serversInRow = [0 for _ in range(rows)]
    serversInCol = [0 for _ in range(cols)]
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                serversInRow[row] += 1
                serversInCol[col] += 1
    count = 0        
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                if serversInRow[row] > 1:
                    count += 1
                elif serversInCol[col] > 1:
                    count += 1
    return count
