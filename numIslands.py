def adj(i, j, grid):
    ans = []
    rows = len(grid)
    cols = len(grid[0])
    if i+1 < rows and grid[i+1][j] == "1":
        ans.append((i+1,j))
    if i-1 >= 0 and grid[i-1][j] == "1":
        ans.append((i-1,j))
    if j+1 < cols and grid[i][j+1] == "1":
        ans.append((i,j+1))
    if j-1 >= 0 and grid[i][j-1] == "1":
        ans.append((i,j-1))
    return ans

def dfs(i, j, grid, visited):
    visited.add((i,j))
    adjacency = adj(i, j, grid)
    for node in adjacency:
        if not node in visited:
            dfs(node[0], node[1], grid, visited)

def numIslands(grid):
    count = 0
    landPieces = []
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1":
                landPieces.append((i,j))
    visited = set()
    for landPiece in landPieces:
        if not landPiece in visited:
            dfs(landPiece[0], landPiece[1], grid, visited)
            count += 1
    return count
