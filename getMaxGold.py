def findMaxGold(grid, i, j, rows, cols, visited):
    if i < 0 or i > rows-1 or j < 0 or j > cols-1:
        return 0
    if grid[i][j] == 0:
        return 0
    if visited[i][j] == True:
        return 0
    visited[i][j] = True
    gold1 = findMaxGold(grid, i+1, j, rows, cols, visited)
    gold2 = findMaxGold(grid, i-1, j, rows, cols, visited)
    gold3 = findMaxGold(grid, i, j+1, rows, cols, visited)
    gold4 = findMaxGold(grid, i, j-1, rows, cols, visited)
    visited[i][j] = False
    return grid[i][j] + max(gold1, gold2, gold3, gold4)

def getMaximumGold(grid):
    if grid == None:
        return 0
    if len(grid) == 0:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    bestScore = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] > 0:
                # perform dfs from here to identify all possible paths from here
                # and update bestScore if a better scoring path is found
                visited = [[False for _ in range(cols)] for _ in range(rows)]
                gold = findMaxGold(grid, i, j, rows, cols, visited) 
                if gold > bestScore:
                    bestScore = gold
    return bestScore
                        
