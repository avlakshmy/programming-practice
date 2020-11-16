def dfsCycle(grid, i, j, visited, pi, pj):
    if visited[i][j] == True:
        return True
    visited[i][j] = True
    res = False
    adj = []
    rows = len(grid)
    cols = len(grid[0])
    if j <= cols-2 and grid[i][j] == grid[i][j+1] and (not [pi,pj] == [i,j+1]):
        adj.append([i,j+1])
    if i <= rows-2 and grid[i][j] == grid[i+1][j] and (not [pi,pj] == [i+1,j]):
        adj.append([i+1,j])
    if j >= 1 and grid[i][j] == grid[i][j-1] and (not [pi,pj] == [i,j-1]):
        adj.append([i,j-1])
    if i >= 1 and grid[i][j] == grid[i-1][j] and (not [pi,pj] == [i-1,j]):
        adj.append([i-1,j])
    for child in adj:
        ans = dfsCycle(grid, child[0], child[1], visited, i, j)
        res = res or ans
    return res
    
def containsCycle(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False for _ in range(cols)] for  _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if visited[i][j] == False:
                if dfsCycle(grid, i, j, visited, -1, -1) == True:
                    return True
    return False
