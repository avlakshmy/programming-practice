def islandPerimeter(grid):
    perim = 0
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                if i == 0:
                    perim += 1
                if j == 0:
                    perim += 1
                if i == rows - 1:
                    perim += 1
                if j == cols - 1:
                    perim += 1
                if i >= 1 and grid[i-1][j] == 0:
                    perim += 1
                if i <= rows-2 and grid[i+1][j] == 0:
                    perim += 1
                if j >= 1 and grid[i][j-1] == 0:
                    perim += 1
                if j <= cols-2 and grid[i][j+1] == 0:
                    perim += 1
    return perim
