def getHeight(adjList, n, root):
    visited = [False for _ in range(n)]
    height = [0 for _ in range(n)]
    queue = [root]
    height[root] = 1
    
    while len(queue) > 0:
        top = queue[0]
        queue.remove(top)
        if visited[top] == False:
            visited[top] = True
            for v in adjList[top]:
                if visited[v] == False:
                    queue.append(v)
                    height[v] = height[top] + 1
    
    return max(height)
