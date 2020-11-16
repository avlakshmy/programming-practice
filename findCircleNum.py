def dfs(i, visited, M, n):
    visited[i] = True
    for j in range(n):
        if j != i and M[i][j] == 1 and visited[j] == False:
            dfs(j, visited, M, n)

def findCircleNum(M):
    n = len(M)
    count = 0
    visited = [False for i in range(n)]
    for i in range(n):
        if visited[i] == False:
            dfs(i, visited, M, n)
            count += 1
    return count
