def findMinHeightTrees(n, edges):
    adjList = [[] for _ in range(n)]
    for edge in edges:
        adjList[edge[0]].append(edge[1])
        adjList[edge[1]].append(edge[0])

    nodes = set([i for i in range(n)])

    while len(nodes) > 2:
        leaves = set([i for i in range(n) if len(adjList[i]) == 1])
        nodes -= leaves
        for leaf in leaves:
            for adj in adjList[leaf]:
                if leaf in adjList[adj]:
                    adjList[adj].remove(leaf)

    return list(nodes)
