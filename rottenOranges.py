def orangesRotting(grid):
    rows = len(grid)
    cols = len(grid[0])
    freshOrangePos = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                freshOrangePos.append((i,j))
    minutes = 0
    while len(freshOrangePos) > 0:
        becomeRotten = []
        for orange in freshOrangePos:
            i = orange[0]
            j = orange[1]
            if i <= rows-2 and grid[i+1][j] == 2:
                becomeRotten.append((i,j))
            elif i >= 1 and grid[i-1][j] == 2:
                becomeRotten.append((i,j))
            elif j <= cols-2 and grid[i][j+1] == 2:
                becomeRotten.append((i,j))
            elif j >= 1 and grid[i][j-1] == 2:
                becomeRotten.append((i,j))
        if len(becomeRotten) == 0:
            return -1
        for rot in becomeRotten:
            freshOrangePos.remove(rot)
            grid[rot[0]][rot[1]] = 2
        minutes += 1
    return minutes
